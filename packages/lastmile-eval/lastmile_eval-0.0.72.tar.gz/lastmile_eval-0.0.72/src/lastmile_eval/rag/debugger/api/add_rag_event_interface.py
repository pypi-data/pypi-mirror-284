"""Interface for defining the methods for adding rag-specific events"""

import abc
import json
from dataclasses import asdict
from typing import Any, Optional, TYPE_CHECKING, Union
from enum import Enum

from opentelemetry.trace.span import Span

from ..common.types import Node, RetrievedNode, TextEmbedding
from ..common import core

if TYPE_CHECKING:
    from _typeshed import DataclassInstance


class RAGEventType(str, Enum):
    """
    Enum to define the type of RAG event that is being added.

    Subclassing as str is required for Enum to be JSON serialiazation compliant
    see: https://stackoverflow.com/questions/65339635/how-to-deserialise-enumeration-with-string-representation
    """

    CHUNKING = "chunking"
    EMBEDDING = "embedding"
    MULTI_EMBEDDING = "multi_embedding"
    PROMPT_COMPOSITION = "prompt_composition"
    QUERY = "query"
    RERANKING = "reranking"
    RETRIEVAL = "retrieval"
    SUB_QUESTION = "sub_question"
    SYNTHESIZE = "synthesize"
    TEMPLATING = "templating"
    TOOL_CALL = "tool_call"
    CUSTOM = "custom"


# TODO: Add exception handling events
class AddRagEventInterface(abc.ABC):
    """
    Interface for defining the rag-specific events. Each rag-specific event calls
    into add_rag_event_for_span() to add the event for a span.

    The method `add_rag_event_for_span` needs to be implemented by whichever
    class implements this interface (Python does not have interfaces so this
    is done through a child class inheriting AddRagEventInterface).
    """

    def add_query_event(
        self,
        query: str,
        llm_output: str | list[str],
        span: Optional[Span] = None,
        system_prompt: Optional[str] = None,
        event_name: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ):
        """
        Use this to keep track of the start and end of a query.

        This calls into the `add_rag_event_for_span` method so please see the
        docstrings there on how to use any of the shared arguments.
        """
        if system_prompt is not None:
            if metadata is None:
                metadata = {}
            metadata["system_prompt"] = system_prompt
        self.log_span_event(
            name=event_name or RAGEventType.QUERY,
            input=query,
            output=llm_output,  # TODO(rossdan): Make it str only to make everything else easier
            span=span,
            event_data=metadata,
            event_kind=RAGEventType.QUERY,
        )

    def add_chunking_event(
        self,
        output_nodes: list[Node],
        span: Optional[Span] = None,
        filepath: Optional[str] = None,
        retrieved_node: Optional[RetrievedNode] = None,
        event_name: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ):
        """
        Use this to keep track of nodes generated either from:
            1. a file (ingestion)
            2. RetrievedNode (retrieval)
                if you desire to sub-chunk your retrieved nodes

        @param filepath: The path to the file that was chunked
            If this is not provided, retrieved_node must be provided
        @param retrieved_node: The retrieved node that was chunked
            If this is not provided, filepath must be provided
        @param output_nodes: The nodes generated from the chunking process

        You can use metadata to store other information such chunk size,
        mime type, file metadata, etc.

        This calls into the `add_rag_event_for_span` method so please see the
        docstrings there on how to use any of the shared arguments.
        """
        if filepath is None and retrieved_node is None:
            print(
                "Warning: You must either provide a filepath or a retrieved node in order to chunk text"
            )
            return
        if filepath is not None and retrieved_node is not None:
            print(
                "Warning: You must provide either a filepath or a retrieved node, not both"
            )
            return
        input_text: str = ""
        if filepath:
            input_text = filepath
        if retrieved_node:
            input_text = retrieved_node.text

        output_nodes_serialized = json.dumps(list(map(asdict, output_nodes)))

        self.log_span_event(
            name=event_name or RAGEventType.CHUNKING,
            input=input_text,
            output=output_nodes_serialized,
            span=span,
            event_data=metadata,
            event_kind=RAGEventType.CHUNKING,
        )

    def add_embedding_event(
        self,
        embedding: TextEmbedding,
        span: Optional[Span] = None,
        event_name: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ):
        """
        Use this to keep track of the embeddings generated from text in either:
            1. the query during retrieval
            2. the documents during ingestion

        You can use metadata to store other information such as the embedding
        model name.

        This calls into the `add_rag_event_for_span` method so please see the
        docstrings there on how to use any of the shared arguments.
        """
        self.log_span_event(
            name=event_name or RAGEventType.EMBEDDING,
            input=embedding.text,
            output=embedding.vector,
            span=span,
            event_data=metadata,
            event_kind=RAGEventType.EMBEDDING,
        )

    def add_multi_embedding_event(
        self,
        embeddings: list[TextEmbedding],
        rounding_decimal_places: int = 4,
        span: Optional[Span] = None,
        event_name: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ):
        """
        Similar to add_embedding_event() but for multiple TextEmbedding objects.

        @param rounding_decimal_places: The number of decimal places to round
            each float value in the embedding vectors to. We need to do this
            because OpenTelemetry doesn't support nested lists in span
            attributes, so we need to convert the nested list of embeddings
            to a json string. However, for floats with long decimal places,
            this can cause the string to be too large for OpenTelemetry to
            handle (floats are 64-bit, strings are 8-bit per char) and fail
            with a "413 Request Entity Too Large" error.

            If this happens, you can also try reducing the size of your
            payload calls by splitting up `add_multi_embedding_event`
            within separate sub-spans and using `add_embedding_event()`
            instead.

            Example:
            ```
            # Before
            tracer.add_multi_embedding_event(
                embeddings=embeddings,
                span=span,
            )

            # After
            for embedding in embeddings:
                with tracer.start_as_current_span(
                    "sub-embedding",
                    context=span.get_span_context() #Connect to parent span
                ) as sub_span:
                    tracer.add_embedding_event(
                        embedding=embedding,
                        span=sub_span,
                    )
            tracer.add_synthesize_event(
                input="Synthesized embedings",
                output="Success!",
                span=span,
            )
            ```

        You can use metadata to store other information such as the embedding
        model name, text count, etc.

        This calls into the `add_rag_event_for_span` method so please see the
        docstrings there on how to use any of the shared arguments.
        """
        clipped_vectors: list[list[float]] = [
            [round(j, rounding_decimal_places) for j in i.vector]
            for i in embeddings
        ]

        self.log_span_event(
            name=event_name or RAGEventType.MULTI_EMBEDDING,
            input=[embedding.text for embedding in embeddings],
            # Span attributes can only be primitives or lists of primitives
            # clipped_vectors are in list[list[float]] format so we need to
            # dump to str
            output=json.dumps(clipped_vectors),
            span=span,
            event_data=metadata,
            event_kind=RAGEventType.MULTI_EMBEDDING,
        )

    def add_prompt_composition_event(
        self,
        resolved_prompt: str,
        span: Optional[Span] = None,
        event_name: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ):
        """
        Use this to keep track of how a prompt is composed from multiple
        sources such as the system prompt, user prompt, and retrieved context.
        This event represents the synthesis of all these sources (from child span events)
        into a single resolved prompt.


        This calls into the `add_rag_event_for_span` method so please see the
        docstrings there on how to use any of the shared arguments.
        """
        self.log_span_event(
            name=event_name or RAGEventType.PROMPT_COMPOSITION,
            input="",
            output=resolved_prompt,
            span=span,
            event_data=metadata,
            event_kind=RAGEventType.PROMPT_COMPOSITION,
        )

    def add_sub_question_event(
        self,
        original_query: str,
        subqueries: list[str],
        span: Optional[Span] = None,
        event_name: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ):
        """
        Use this to keep track of whenever a query is split into smaller
        sub-questions to be handled separately later.

        This calls into the `add_rag_event_for_span` method so please see the
        docstrings there on how to use any of the shared arguments.
        """
        self.log_span_event(
            name=event_name or RAGEventType.SUB_QUESTION,
            input=original_query,
            output=subqueries,
            span=span,
            event_data=metadata,
            event_kind=RAGEventType.SUB_QUESTION,
        )

    def add_retrieval_event(
        self,
        query: str,
        retrieved_nodes: list[RetrievedNode],  # Can also make this str
        span: Optional[Span] = None,
        event_name: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ):
        """
        Use this to keep track of the nodes retrieved for a query.

        This calls into the `add_rag_event_for_span` method so please see the
        docstrings there on how to use any of the shared arguments.
        """
        retrieved_nodes_serialized = json.dumps(
            list(map(asdict, retrieved_nodes))
        )
        self.log_span_event(
            name=event_name or RAGEventType.RETRIEVAL,
            input=query,
            output=retrieved_nodes_serialized,
            span=span,
            event_data=metadata,
            event_kind=RAGEventType.RETRIEVAL,
        )

    def add_reranking_event(
        self,
        input_nodes: list[Node],
        output_nodes: list[Node],
        span: Optional[Span] = None,
        event_name: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ):
        """
        Use this to keep track on how nodes that were retrieved are re-ordered

        You can use metadata to store other information such as the re-ranking
        model name.

        This calls into the `add_rag_event_for_span` method so please see the
        docstrings there on how to use any of the shared arguments.
        """
        input_nodes_as_dict = list(map(lambda node: asdict(node), input_nodes))
        output_nodes_as_dict = list(
            map(lambda node: asdict(node), output_nodes)
        )
        self.log_span_event(
            name=event_name or RAGEventType.RERANKING,
            # TODO: Fix dict issue with span events
            input=input_nodes_as_dict,
            output=output_nodes_as_dict,
            span=span,
            event_data=metadata,
            event_kind=RAGEventType.RERANKING,
        )

    def add_template_event(
        self,
        prompt_template: str,
        resolved_prompt: str,
        system_prompt: Optional[str] = None,
        span: Optional[Span] = None,
        event_name: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ):
        """
        Use this to keep track on how a query is re-written using a prompt
        template

        You can use metadata to store other information such as the original
        user question, retrieved context, prompt template id, etc.

        This calls into the `add_rag_event_for_span` method so please see the
        docstrings there on how to use any of the shared arguments.
        """
        if system_prompt is not None:
            if metadata is None:
                metadata = {}
            metadata["system_prompt"] = system_prompt
        self.log_span_event(
            name=event_name or RAGEventType.TEMPLATING,
            input=prompt_template,
            output=resolved_prompt,
            span=span,
            event_data=metadata,
            event_kind=RAGEventType.TEMPLATING,
        )

    def add_tool_call_event(
        self,
        query: str,
        tool_name: str,
        # TODO: Result and value of tool_arguments can't actually be Any,
        # it must be JSON-serializable
        tool_arguments: Optional[dict[str, Any]] = None,
        span: Optional[Span] = None,
        event_name: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ):
        """
        Use this to keep track of how the LLM chooses what tool to use based on user query.
        This does NOT include invoking the tool itself to get an answer
        to the query.

        You can use metadata to store other information such as the tool
        parameter schema, tool parameter values, pre-processed result, etc.

        This calls into the `add_rag_event_for_span` method so please see the
        docstrings there on how to use any of the shared arguments.
        """
        tool_data = {"tool_name": tool_name}
        if tool_arguments:
            tool_data["tool_arguments"] = tool_arguments
        self.log_span_event(
            name=event_name or RAGEventType.TOOL_CALL,
            input=query,
            output=json.dumps(tool_data),
            span=span,
            event_data=metadata,
            event_kind=RAGEventType.TOOL_CALL,
        )

    def add_synthesize_event(
        self,
        input: Any,
        output: Any,
        span: Optional[Span] = None,
        event_name: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ):
        """
        Use this as a catch-all to summarize the input and output of several
        nested events.

        This calls into the `add_rag_event_for_span` method so please see the
        docstrings there on how to use any of the shared arguments.
        """
        self.log_span_event(
            name=event_name or RAGEventType.SYNTHESIZE,
            # TODO: Fix dict issue for span data
            input=input,
            output=output,
            span=span,
            event_data=metadata,
            event_kind=RAGEventType.SYNTHESIZE,
        )

    @abc.abstractmethod
    def log_span_event(
        self,
        # TODO: Have better typing for JSON for input, output, event_data
        input: core.JSON = None,
        output: core.JSON = None,
        span: Optional[Span] = None,
        event_data: Optional[Union[core.JSON, "DataclassInstance"]] = None,
        event_kind: RAGEventType = RAGEventType.CUSTOM,
        name: Optional[str] = None,
    ) -> None:
        """
        Log an event tracking the input, output and JSON-serializable event data for an individual span.
        There can only be one RAG Event for the span, meant to capture the input and output of the span.

        You can use the data recorded in the event to generate test cases and run evaluations.

        input: The input to record.
        output: The output to record.
        span: The span to record the event for
            Defaults to opentelemetry.trace.get_current_span()
        event_data: JSON-serializable event data capturing any other metadata to save as part of the event.
        event_kind: The kind of event (e.g. "reranking", "tool_call", etc.).
            If this is a well-defined event kind, it will be rendered in an event-specific way in the UI.
        name: A name to give the event, if needed.
            Useful to disambiguate multiple of the same kind of event.
        """

    @abc.abstractmethod
    def log_trace_event(
        self,
        input: core.JSON = None,
        output: core.JSON = None,
        event_data: Optional[
            Union[core.JSONObject, "DataclassInstance"]
        ] = None,
    ) -> None:
        """
        Log an event tracking the input, output and JSON-serializable event data for the trace.
        There can only be one RAG Event at the trace level, meant to capture the input and output of the entire flow.

        You can use the data recorded in the event to generate test cases and run evaluations.

        Args:
            input (Optional[Dict[str, Any]]): The input to the RAG application. It should be a JSON-serializable dictionary.
                Defaults to None.
            output (Optional[Dict[str, Any]]): The output produced by the RAG application. It should be a JSON-serializable dictionary.
                Defaults to None.
            event_data (Optional[Dict[str, Any]]): Additional JSON-serializable event data capturing any other metadata to save as part of the event.
                Defaults to None.

        Returns:
            None
        """
