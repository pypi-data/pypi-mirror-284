"""Import all models to make sure they are registered with SQLAlchemy.
"""

from gptdb.app.knowledge.chunk_db import DocumentChunkEntity
from gptdb.app.knowledge.document_db import KnowledgeDocumentEntity
from gptdb.app.openapi.api_v1.feedback.feed_back_db import ChatFeedBackEntity
from gptdb.datasource.manages.connect_config_db import ConnectConfigEntity
from gptdb.model.cluster.registry_impl.db_storage import ModelInstanceEntity
from gptdb.serve.agent.db.my_plugin_db import MyPluginEntity
from gptdb.serve.agent.db.plugin_hub_db import PluginHubEntity
from gptdb.serve.flow.models.models import ServeEntity as FlowServeEntity
from gptdb.serve.prompt.models.models import ServeEntity as PromptManageEntity
from gptdb.serve.rag.models.models import KnowledgeSpaceEntity
from gptdb.storage.chat_history.chat_history_db import (
    ChatHistoryEntity,
    ChatHistoryMessageEntity,
)

_MODELS = [
    PluginHubEntity,
    MyPluginEntity,
    PromptManageEntity,
    KnowledgeSpaceEntity,
    KnowledgeDocumentEntity,
    DocumentChunkEntity,
    ChatFeedBackEntity,
    ConnectConfigEntity,
    ChatHistoryEntity,
    ChatHistoryMessageEntity,
    ModelInstanceEntity,
    FlowServeEntity,
]
