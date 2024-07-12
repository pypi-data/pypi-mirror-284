import logging
import os
from typing import Callable, Generator, Mapping, Optional, Sequence

import numpy as np
import pandas as pd
import requests
import result
from requests import Response

from lastmile_eval.rag.debugger.common import core
from lastmile_eval.rag.debugger.common.types import (
    APIToken,
    BaseURL,
    CreatorID,
    OrganizationID,
    ProjectName,
    Res,
)
from lastmile_eval.rag.debugger.common.utils import (
    DEFAULT_PROJECT_NAME,
    get_project_id,
    load_project_name,
    WEBSITE_BASE_URL,
)

from ..offline_evaluation import evaluation_lib
from ..offline_evaluation.evaluation_lib import (
    BatchDownloadParams,
    BatchOutputsWithOTELTraceIds,
    BatchTraceDownloadParams,
    EvaluatorTuple,
    clean_rag_query_tracelike_df,
    wrap_with_tracer,
)

logger = logging.getLogger(__name__)
logging.basicConfig()


# TODO(b7r6): probably move these definitions to a common module
# that's accessible to both our code and user code
Evaluator = evaluation_lib.Evaluator
Aggregator = evaluation_lib.Aggregator
SaveOptions = evaluation_lib.SaveOptions


def list_example_sets(
    take: int = 10,
    timeout: int = 60,
    lastmile_api_token: Optional[str] = None,
) -> core.JSONObject:
    """
    Get a list of test sets from the LastMile API.

    Args:
        take: The number of test sets to return. The default is 10.
        lastmile_api_token: The API token for the LastMile API. If not provided,
            will try to get the token from the LASTMILE_API_TOKEN
            environment variable.
            You can create a token from the "API Tokens" section from this website:
            {WEBSITE_BASE_URL}/settings?page=tokens
        timeout: The maximum time in seconds to wait for the request to complete.
            The default is 60.

    Returns:
        A dictionary containing the test sets.
    """
    lastmile_api_token = core.token(lastmile_api_token)
    endpoint_with_params = f"evaluation_example_sets/list?pageSize={str(take)}"
    lastmile_url = os.path.join(WEBSITE_BASE_URL, "api", endpoint_with_params)

    response: Response = requests.get(
        lastmile_url,
        headers={"Authorization": f"Bearer {lastmile_api_token}"},
        timeout=timeout,
    )
    # TODO(jll): Handle response errors
    return response.json()


def get_traces(
    project_name: Optional[str] = None,
    trace_ids: Optional[str | list[str]] = None,
    take: Optional[int] = None,
    search_filter: Optional[str] = None,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
    lastmile_api_token: Optional[str] = None,
) -> Generator[pd.DataFrame, None, None]:
    """
    Download traces as a DataFrame.

    Args:
        project_name: The name of the project the traces were logged to. If not provided,
            will read from the LASTMILE_PROJECT_NAME environment variable. If that is not set,
            and no trace_ids are provided, will use the DEFAULT project.
        trace_ids: Optional filter by IDs
        take: Number of traces to download per request. The maximum is 50.
        search_filter: A substring search to match any property in the trace metadata.
        start_time: Start unix timestamp (GMT seconds) to filter traces >= start_time.
        end_time: End unix timestamp (GMT seconds) to filter traces <= end_time.
        lastmile_api_token: The API token for the LastMile API. If not provided,
            will try to get the token from the LASTMILE_API_TOKEN
            environment variable.
            You can create a token from the "API Tokens" section from this website:
            https://lastmileai.dev/settings?page=tokens

    Returns:
        A DataFrame containing the trace data.
    """
    base_url = WEBSITE_BASE_URL
    lastmile_api_token = core.token(lastmile_api_token)
    trace_project_name = (
        ProjectName(project_name)
        if project_name is not None
        else load_project_name()
    )

    project_id = get_project_id(
        project_name=trace_project_name or DEFAULT_PROJECT_NAME,
        lastmile_api_token=APIToken(lastmile_api_token),
    )

    trace_ids_list = [trace_ids] if isinstance(trace_ids, str) else trace_ids
    if trace_ids_list is not None:
        trace_ids_list = [
            core.RAGQueryTraceID(trace_id) for trace_id in trace_ids_list
        ]

    download_params: Res[BatchTraceDownloadParams] = result.do(
        result.Ok(
            BatchTraceDownloadParams(
                project_id=project_id_ok,
                trace_ids=trace_ids_list,
                take=take,
                search_filter=search_filter,
                start_time=start_time,
                end_time=end_time,
            )
        )
        for project_id_ok in project_id
    )

    generator = result.do(
        evaluation_lib.download_rag_query_traces_helper(
            BaseURL(base_url),
            APIToken(lastmile_api_token),
            download_params_ok,
        )
        for download_params_ok in download_params
    )

    match (generator):
        case result.Ok(generator_ok):
            for batch in generator_ok:
                yield batch.map(clean_rag_query_tracelike_df).unwrap_or_raise(
                    ValueError
                )
        case result.Err(e):
            raise ValueError(e)


def download_rag_events(
    project_name: Optional[str] = None,
    batch_limit: Optional[int] = None,
    substring_filter: Optional[str] = None,
    creator_id: Optional[str] = None,
    organization_id: Optional[str] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    event_name: Optional[str] = None,
    lastmile_api_token: Optional[str] = None,
) -> Generator[pd.DataFrame, None, None]:
    HARD_BATCH_LIMIT = 50
    if batch_limit is None:
        batch_limit = HARD_BATCH_LIMIT

    if batch_limit < 1 or batch_limit > HARD_BATCH_LIMIT:
        raise ValueError(
            f"batch_limit must be between 1 and {HARD_BATCH_LIMIT}"
        )
    base_url = WEBSITE_BASE_URL
    lastmile_api_token = core.token(lastmile_api_token)
    project_id = (
        get_project_id(
            project_name=ProjectName(project_name),
            lastmile_api_token=APIToken(lastmile_api_token),
        )
        if project_name is not None
        else result.Ok(None)
    )

    download_params: Res[BatchDownloadParams] = result.do(
        result.Ok(
            BatchDownloadParams(
                batch_limit=batch_limit,
                search=substring_filter,
                creator_id=(
                    CreatorID(creator_id) if creator_id is not None else None
                ),
                project_id=project_id_ok,
                organization_id=(
                    OrganizationID(organization_id)
                    if organization_id is not None
                    else None
                ),
                start_timestamp=start_time,
                end_timestamp=end_time,
                event_name=event_name,
            )
        )
        for project_id_ok in project_id
    )

    generator = result.do(
        evaluation_lib.download_rag_events_helper(
            BaseURL(base_url),
            APIToken(lastmile_api_token),
            download_params_ok,
        )
        for download_params_ok in download_params
    )

    match (generator):
        case result.Ok(generator_ok):
            for batch in generator_ok:
                yield batch.unwrap_or_raise(ValueError)
        case result.Err(e):
            raise ValueError(e)


def create_test_dataset(
    name: str,
    data: pd.DataFrame,
    project_name: Optional[str] = None,
    lastmile_api_token: Optional[str] = None,
) -> evaluation_lib.CreateInputSetResponse:
    """
    Create a Test Set from the given data.

    name: Name to save the Test Set as.
    data: A DataFrame that should contain up to three columns: 'input', 'output', 'groundTruth'. The input column is *required* for every TestSet.
    project_name: The name of the project to save TestSet in.
    lastmile_api_token: The API token for the LastMile API. If not provided,
        will try to get the token from the LASTMILE_API_TOKEN
        environment variable.
        You can create a token from the "API Tokens" section from this website:
        https://lastmileai.dev/settings?page=tokens
    """
    # TODO: Add ability to read from LASTMILE_PROJECT_NAME env variable
    # TODO: Add tags to categorize the TestSet as. This can be used for filtering.
    # TODO (maybe?): Use project_id instead of project_name?
    base_url = WEBSITE_BASE_URL
    lastmile_api_token = core.token(lastmile_api_token)

    project_id = (
        get_project_id(
            project_name=ProjectName(project_name),
            lastmile_api_token=APIToken(lastmile_api_token),
        )
        if project_name is not None
        else result.Ok(None)
    )

    outcome = result.do(
        evaluation_lib.create_input_set_helper(
            BaseURL(base_url),
            project_id_ok,
            data,
            APIToken(lastmile_api_token),
            name,
        )
        for project_id_ok in project_id
    )

    return outcome.unwrap_or_raise(ValueError)


# TODO (rossdan): Rename all "input" stuff to be test set
def download_input_set(
    input_set_id: Optional[str] = None,
    input_set_name: Optional[str] = None,
    project_name: Optional[str] = None,
    lastmile_api_token: Optional[str] = None,
) -> pd.DataFrame:
    """
    Download Input Set from given id or name.

    input_set_id: The id of the Input Set to download.
        Do not use this if you are providing input_set_name.
    input_set_name: Name to save the Input Set to download.
        Do not use this if you are providing input_set_id.
    project_name: The name of the project that this Input Set
        belongs to. It acts as an additional filter since
        the same input_set_name can exist in multiple projects.
        Do not use this if you are providing input_set_id.
    lastmile_api_token: The API token for the LastMile API. If not provided,
        will try to get the token from the LASTMILE_API_TOKEN
        environment variable.
        You can create a token from the "API Tokens" section from this website:
        https://lastmileai.dev/settings?page=tokens
    """
    base_url = WEBSITE_BASE_URL
    lastmile_api_token = core.token(lastmile_api_token)

    project_id = (
        get_project_id(
            project_name=ProjectName(project_name),
            lastmile_api_token=APIToken(lastmile_api_token),
        )
        if project_name is not None
        else result.Ok(None)
    )

    outcome = result.do(
        evaluation_lib.download_input_set_helper(
            BaseURL(base_url),
            project_id_ok,
            (
                core.InputSetID(input_set_id)
                if input_set_id is not None
                else None
            ),
            input_set_name,
            lastmile_api_token,
        )
        for project_id_ok in project_id
    )

    return outcome.unwrap_or_raise(ValueError)


def create_example_set(
    df: pd.DataFrame,
    example_set_name: Optional[str],
    project_name: Optional[str] = None,
    ground_truths: Optional[list[str]] = None,
    lastmile_api_token: Optional[str] = None,
) -> evaluation_lib.CreateExampleSetResponse:
    base_url = WEBSITE_BASE_URL
    lastmile_api_token = core.token(lastmile_api_token)

    project_id = (
        get_project_id(
            project_name=ProjectName(project_name),
            lastmile_api_token=APIToken(lastmile_api_token),
        )
        if project_name is not None
        else result.Ok(None)
    )

    outcome = result.do(
        evaluation_lib.create_example_set_helper(
            BaseURL(base_url),
            project_id_ok,
            df,
            example_set_name,
            ground_truths,
            APIToken(lastmile_api_token),
        )
        for project_id_ok in project_id
    )
    return outcome.unwrap_or_raise(ValueError)


def download_example_set(
    example_set_id: Optional[str] = None,
    example_set_name: Optional[str] = None,
    project_name: Optional[str] = None,
    lastmile_api_token: Optional[str] = None,
) -> pd.DataFrame:
    base_url = WEBSITE_BASE_URL
    lastmile_api_token = core.token(lastmile_api_token)

    project_id = (
        get_project_id(
            project_name=ProjectName(project_name),
            lastmile_api_token=APIToken(lastmile_api_token),
        )
        if project_name is not None
        else result.Ok(None)
    )

    raw = result.do(
        evaluation_lib.download_example_set_helper(
            BaseURL(base_url),
            APIToken(lastmile_api_token),
            project_id_ok,
            (
                core.ExampleSetID(example_set_id)
                if example_set_id is not None
                else None
            ),
            example_set_name,
        )
        for project_id_ok in project_id
    )

    return raw.map(clean_rag_query_tracelike_df).unwrap_or_raise(ValueError)


def run(
    run_fn: Callable[[str], str],
    inputs: Sequence[str] | pd.DataFrame,
    project_name: Optional[str] = None,
    lastmile_api_token: Optional[str] = None,
) -> pd.DataFrame:
    """
    Runs the input data using the run_fn, and returns the results in an 'output' column in a DataFrame..
    Importantly, this function wraps the run in a trace, so it can be tracked and evaluated easily.

    run_fn: The callable to invoke the execution flow.
    inputs: A DataFrame with an 'input' column, or a list of strings.
    project_name: The name of the project the evaluation result is saved in.
        If not provided, will read from the LASTMILE_PROJECT_NAME environment variable.
        If that is not set, will use the DEFAULT project.
    lastmile_api_token: The API token for the LastMile API. If not provided,
        will try to get the token from the LASTMILE_API_TOKEN
        environment variable.
        You can create a token from the "API Tokens" section from this website:
        https://lastmileai.dev/settings?page=tokens
    """

    run_query_with_tracer_fn = wrap_with_tracer(
        run_fn,
        project_name=project_name,
        lastmile_api_token=lastmile_api_token,
    )

    outputs_with_trace_ids = evaluation_lib.run_rag_query_fn_helper(
        run_query_with_tracer_fn, inputs
    )

    if isinstance(inputs, Sequence):
        inputs = pd.DataFrame(
            {
                "input": inputs,
            }
        )

    output_df: Res[pd.DataFrame] = result.do(
        result.Ok(
            inputs.assign(  # type: ignore[pandas]
                output=outputs_with_trace_ids_ok[0],
                traceId=outputs_with_trace_ids_ok[1],
            )
        )
        for outputs_with_trace_ids_ok in outputs_with_trace_ids
    )
    return output_df.unwrap_or_raise(ValueError)


def evaluate(
    evaluators: (
        Mapping[
            str,  # Name of the evaluation metric
            Evaluator
            | EvaluatorTuple,  # Tuple of Evaluator function and (optionally) Aggregator function
        ]
        | set[str]
    ),
    project_name: Optional[str] = None,
    example_set_id: Optional[str] = None,
    examples_dataframe: Optional[pd.DataFrame] = None,
    save_options: Optional[SaveOptions] = None,
    lastmile_api_token: Optional[str] = None,
) -> evaluation_lib.CreateEvaluationResponse:
    """
    *Description*

        Run evaluations on RAG query Examples using chosen evaluation functions.

        evaluators: A mapping of evaluator names to evaluator functions. Each evaluator takes a DataFrame and produces one value per row.
            Example: {"exact_match": some_exact_match_checking_function}

        project_name: The name of the project the evaluation result is saved in.
            If not provided, will read from the LASTMILE_PROJECT_NAME environment variable.
            If that is not set, will use the DEFAULT project.
        example_set_id, examples_dataframe: give one of these to specify your evaluation inputs.
        save_options: Controls backend storage options for your Evaluation Result.
        lastmile_api_token: You can get one here https://lastmileai.dev/settings?page=tokens.
            If None, this function will try to load it from a local .env file.


    *Input Data (Examples)*

        A RAG query example is essentially a row of data
        containing fields like `query`, `context`, `prompt`, `groundTruth`, etc.

        Examples can contain any data from your RAG Query Traces, for example, as well as a groundTruth column.

        The data is specified as either an example set ID or a DataFrame. If an example set ID is provided,
        it will be downloaded from the LastMile API and evaluations will run locally.

        If a DataFrame is provided, it will be used directly (also locally).

    *Evaluators*

        Each evaluator is a function that maps a DataFrame to a list of metric values, one float per row.
        The idea is to apply an example-level evaluator to each row of the input DataFrame.

        Accepts either:
            1) mapping of evaluator name to callable or EvaluatorTuple
            2) set of predefined default evaluator names.

        EvaluatorTuple allows you to do custom aggregations over all the DataFrame rows (for example, some specific recall@precision).
        If not provided, a few defaults will be used.
    """

    base_url = BaseURL(WEBSITE_BASE_URL)
    lastmile_api_token = core.token(lastmile_api_token)

    project_id = (
        get_project_id(
            project_name=ProjectName(project_name),
            lastmile_api_token=APIToken(lastmile_api_token),
        )
        if project_name is not None
        else result.Ok(None)
    )

    save_options_ = save_options or SaveOptions()

    all_typed_evaluators = (
        evaluation_lib.user_provided_evaluators_to_all_typed_evaluators(
            evaluators, lastmile_api_token
        )
    )

    outcome = result.do(
        evaluation_lib.evaluate_helper(
            base_url,
            project_id_ok,
            (
                core.ExampleSetID(example_set_id)
                if example_set_id is not None
                else None
            ),
            examples_dataframe,
            lastmile_api_token,
            save_options_,
            all_typed_evaluators_ok,
        )
        for project_id_ok in project_id
        for all_typed_evaluators_ok in all_typed_evaluators
    )

    return outcome.unwrap_or_raise(ValueError)


# TODO: Figure out how to specify we want to inputs and outputs from eventData
# for evaluators instead of default "input" and "output" columns
# We can also for now just say we don't support running eval on eventData and
# we must have defined inputs. I think this is reasonable
def run_and_evaluate(
    run_fn: Callable[[str], str],
    evaluators: (
        Mapping[
            str,  # Name of the evaluation metric
            Evaluator
            | EvaluatorTuple,  # Tuple of Evaluator function and (optionally) Aggregator function
        ]
        | set[str]
    ),
    project_name: Optional[str] = None,
    input_set_id: Optional[str] = None,
    inputs: Optional[list[str]] = None,
    ground_truths: Optional[list[str]] = None,
    save_options: Optional[SaveOptions] = None,
    n_trials: int = 1,
    lastmile_api_token: Optional[str] = None,
) -> evaluation_lib.CreateEvaluationResponse:
    """
    *Description*

        Run a RAG query flow function on the given inputs,
        then run evaluations on corresponding RAG query outputs using chosen evaluation functions.

        run_fn: This should run or simulate your RAG query flow. It must either return a string output,
            or a tuple (string, string) representing (output, rag_query_trace_id).
            If you return the tuple, the evaluation results will be connected to the trace in the UI.
        evaluators: A mapping of evaluator names to evaluator functions. Each evaluator takes a DataFrame and produces one value per row.
            Example: {"exact_match": some_exact_match_checking_function}

        project_name: Optionally, this allows you to group your evaluation results with other evaluations within the project.
        input_set_id, inputs: give exactly one of these to specify your RAG system inputs (query time input).
        ground_truths: Optionally, provide ground truths (references) for each of your inputs.
            This is only accepted if you give a list for your inputs.
            If you give input_set_id, the library will fetch your ground truths from that input set and you must not give ground truths as a function argument.
        save_options: Controls backend storage options for your Example Set and Evaluation Result.
        n_trials: This allows you to simulate a larger Example sample set by using your RAG query inputs N times each.
        lastmile_api_token: You can get one here https://lastmileai.dev/settings?page=tokens.
            If None, this function will try to load it from a local .env file.


    *Input Data (Examples)*
        See `evaluate()`.

    *Evaluators*
        See `evaluate()`.

    """

    base_url = BaseURL(WEBSITE_BASE_URL)
    lastmile_api_token = core.token(lastmile_api_token)

    project_id = (
        get_project_id(
            project_name=ProjectName(project_name),
            lastmile_api_token=APIToken(lastmile_api_token),
        )
        if project_name is not None
        else result.Ok(None)
    )

    save_options_ = save_options or SaveOptions()

    if not save_options_.do_save:
        raise ValueError(
            "do_save==False is currently not supported for `run_and_evaluate()`."
        )

    all_typed_evaluators = (
        evaluation_lib.user_provided_evaluators_to_all_typed_evaluators(
            evaluators, lastmile_api_token
        )
    )

    run_query_with_tracer_fn = wrap_with_tracer(
        run_fn,
        project_name=project_name,
        lastmile_api_token=lastmile_api_token,
    )

    outcome = result.do(
        evaluation_lib.run_and_evaluate_helper(
            base_url,
            project_id_ok,
            run_query_with_tracer_fn,
            all_typed_evaluators_ok,
            save_options_,
            n_trials,
            lastmile_api_token,
            (
                core.InputSetID(input_set_id)
                if input_set_id is not None
                else None
            ),
            inputs,
            ground_truths,
        )
        for project_id_ok in project_id
        for all_typed_evaluators_ok in all_typed_evaluators
    )

    return outcome.unwrap_or_raise(ValueError)


def assert_is_close(
    evaluation_result: evaluation_lib.CreateEvaluationResponse,
    metric_name: str,
    value: float,
) -> None:
    df_metrics_agg = evaluation_result.df_metrics_aggregated
    metric = df_metrics_agg.set_index(["testSetId", "metricName"]).value.unstack("metricName")[metric_name].iloc[0]  # type: ignore[pandas]
    assert np.isclose(metric, value), f"Expected: {value}, Got: {metric}"  # type: ignore[fixme]


def get_default_evaluators() -> dict[
    str,
    str,
]:
    """
    Gets predefined evaluator names that come built in with the LastMile Eval SDK.
    You can choose whichever ones you want and define them as a set when
    using the `evaluate()` and `run_and_evaluate()` methods.

    Example:
    ```python
    from lastmile_eval.rag.debugger.api import evaluate

    def evaluate(
        ...
        evaluators={"toxicity", "exact_match", "bleu"},
        ...
    )
    ```
    """

    return evaluation_lib.get_default_evaluators_with_descriptions()
