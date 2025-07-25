from chatbot.config.system_config import SETTINGS
from chatbot.utils.database_clients.milvus.utils import (
    DataType,
    IndexConfig,
    IndexParam,
    IndexType,
    IndexValueType,
    MetricType,
    SchemaField
)
from chatbot.core.model_clients.embedder.openai import OpenAIEmbedder, OpenAIClientConfig

import logging
logging.getLogger("openai").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)


embedder = OpenAIEmbedder(
    config=OpenAIClientConfig(
        api_key=SETTINGS.OPENAI_API_KEY,
        model_id="text-embedding-3-small",
        model_dimensions=1536,
    )
)
dense_embedding_dimension = len(embedder.get_text_embedding("test"))

DOCUMENT_DATABASE_SCHEMA = [
    SchemaField(
        field_name="chunk_id",
        field_type=DataType.STRING,
        index_config=IndexConfig(index=True),
        field_description="ID of the chunk",
        is_primary=True
    ),
    SchemaField(
        field_name="chunk",
        field_type=DataType.STRING,
        index_config=IndexConfig(index=True),
        field_description="Content of the chunk",
    ),
    SchemaField(
        field_name="chunk_dense_embedding",
        field_type=DataType.DENSE_VECTOR,
        dimension=dense_embedding_dimension,
        index_config=IndexConfig(
            index=True,
            index_type=IndexType.HNSW,
            hnsw_m=16,
            hnsw_ef_construction=500,
            metric_type=MetricType.IP
        ),
        field_description="Dense embedding of the chunk",
    ),
    SchemaField(
        field_name="chunk_sparse_embedding",
        field_type=DataType.SPARSE_VECTOR,
        index_config=IndexConfig(index=True),
        field_description="Sparse embedding of the chunk",
    ),
]

FAQ_DATABASE_SCHEMA = [
    SchemaField(
        field_name="faq_id",
        field_type=DataType.STRING,
        index_config=IndexConfig(index=True),
        field_description="ID of the FAQ",
        is_primary=True
    ),
    SchemaField(
        field_name="faq",
        field_type=DataType.JSON,
        index_config=IndexConfig(index=True),
        field_description="Content of the FAQ",
    ),
    SchemaField(
        field_name="question_dense_embedding",
        field_type=DataType.DENSE_VECTOR,
        dimension=dense_embedding_dimension,
        index_config=IndexConfig(
            index=True,
            index_type=IndexType.HNSW,
            hnsw_m=16,
            hnsw_ef_construction=500,
            metric_type=MetricType.IP
        ),
        field_description="Dense embedding of the question",
    ),
    SchemaField(
        field_name="question_sparse_embedding",
        field_type=DataType.SPARSE_VECTOR,
        index_config=IndexConfig(index=True),
        field_description="Sparse embedding of the question",
    ),
]

JSON_INDEX_PARAMS = {
    "faq": [
        IndexParam(
            indexed_key="faq['question']",
            index_name="question",
            value_type=IndexValueType.STRING
        ),
        IndexParam(
            indexed_key="faq['answer']",
            index_name="answer",
            value_type=IndexValueType.STRING
        ),
    ]
}
