from __future__ import annotations

import logging
from typing import Optional

from gptdb._private.config import Config
from gptdb.app.base import WebServerParameters
from gptdb.component import SystemApp
from gptdb.configs.model_config import MODEL_DISK_CACHE_DIR
from gptdb.util.executor_utils import DefaultExecutorFactory

logger = logging.getLogger(__name__)

CFG = Config()


def initialize_components(
    param: WebServerParameters,
    system_app: SystemApp,
    embedding_model_name: str,
    embedding_model_path: str,
    rerank_model_name: Optional[str] = None,
    rerank_model_path: Optional[str] = None,
):
    # Lazy import to avoid high time cost
    from gptdb.app.initialization.embedding_component import (
        _initialize_embedding_model,
        _initialize_rerank_model,
    )
    from gptdb.app.initialization.scheduler import DefaultScheduler
    from gptdb.app.initialization.serve_initialization import register_serve_apps
    from gptdb.datasource.manages.connector_manager import ConnectorManager
    from gptdb.model.cluster.controller.controller import controller

    # Register global default executor factory first
    system_app.register(
        DefaultExecutorFactory, max_workers=param.default_thread_pool_size
    )
    system_app.register(DefaultScheduler)
    system_app.register_instance(controller)
    system_app.register(ConnectorManager)

    from gptdb.serve.agent.hub.controller import module_plugin

    system_app.register_instance(module_plugin)

    from gptdb.serve.agent.agents.controller import multi_agents

    system_app.register_instance(multi_agents)

    _initialize_embedding_model(
        param, system_app, embedding_model_name, embedding_model_path
    )
    _initialize_rerank_model(param, system_app, rerank_model_name, rerank_model_path)
    _initialize_model_cache(system_app)
    _initialize_awel(system_app, param)
    # Initialize resource manager of agent
    _initialize_resource_manager(system_app)
    _initialize_agent(system_app)
    _initialize_openapi(system_app)
    # Register serve apps
    register_serve_apps(system_app, CFG)


def _initialize_model_cache(system_app: SystemApp):
    from gptdb.storage.cache import initialize_cache

    if not CFG.MODEL_CACHE_ENABLE:
        logger.info("Model cache is not enable")
        return

    storage_type = CFG.MODEL_CACHE_STORAGE_TYPE or "disk"
    max_memory_mb = CFG.MODEL_CACHE_MAX_MEMORY_MB or 256
    persist_dir = CFG.MODEL_CACHE_STORAGE_DISK_DIR or MODEL_DISK_CACHE_DIR
    initialize_cache(system_app, storage_type, max_memory_mb, persist_dir)


def _initialize_awel(system_app: SystemApp, param: WebServerParameters):
    from gptdb.configs.model_config import _DAG_DEFINITION_DIR
    from gptdb.core.awel import initialize_awel

    # Add default dag definition dir
    dag_dirs = [_DAG_DEFINITION_DIR]
    if param.awel_dirs:
        dag_dirs += param.awel_dirs.strip().split(",")
    dag_dirs = [x.strip() for x in dag_dirs]

    initialize_awel(system_app, dag_dirs)


def _initialize_agent(system_app: SystemApp):
    from gptdb.agent import initialize_agent

    initialize_agent(system_app)


def _initialize_resource_manager(system_app: SystemApp):
    from gptdb.agent.expand.resources.gptdb_tool import list_gptdb_support_models
    from gptdb.agent.expand.resources.host_tool import (
        get_current_host_cpu_status,
        get_current_host_memory_status,
        get_current_host_system_load,
    )
    from gptdb.agent.expand.resources.search_tool import baidu_search
    from gptdb.agent.resource.base import ResourceType
    from gptdb.agent.resource.manage import get_resource_manager, initialize_resource
    from gptdb.serve.agent.resource.datasource import DatasourceResource
    from gptdb.serve.agent.resource.knowledge import KnowledgeSpaceRetrieverResource
    from gptdb.serve.agent.resource.plugin import PluginToolPack

    initialize_resource(system_app)
    rm = get_resource_manager(system_app)
    rm.register_resource(DatasourceResource)
    rm.register_resource(KnowledgeSpaceRetrieverResource)
    rm.register_resource(PluginToolPack, resource_type=ResourceType.Tool)
    # Register a search tool
    rm.register_resource(resource_instance=baidu_search)
    rm.register_resource(resource_instance=list_gptdb_support_models)
    # Register host tools
    rm.register_resource(resource_instance=get_current_host_cpu_status)
    rm.register_resource(resource_instance=get_current_host_memory_status)
    rm.register_resource(resource_instance=get_current_host_system_load)


def _initialize_openapi(system_app: SystemApp):
    from gptdb.app.openapi.api_v1.editor.service import EditorService

    system_app.register(EditorService)
