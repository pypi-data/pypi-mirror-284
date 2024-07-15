from gptdb._private.config import Config
from gptdb.component import ComponentType
from gptdb.model.cluster import BaseModelController
from gptdb.serve.agent.db.gpts_app import GptsAppCollectionDao, GptsAppDao

CFG = Config()

collection_dao = GptsAppCollectionDao()
gpts_dao = GptsAppDao()


async def available_llms(worker_type: str = "llm"):
    controller = CFG.SYSTEM_APP.get_component(
        ComponentType.MODEL_CONTROLLER, BaseModelController
    )
    types = set()
    models = await controller.get_all_instances(healthy_only=True)
    for model in models:
        worker_name, wt = model.model_name.split("@")
        if wt == worker_type:
            types.add(worker_name)
    return list(types)
