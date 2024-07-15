"""Some internal tools for the GPT-DB project."""

from typing_extensions import Annotated, Doc

from ...resource.tool.base import tool


@tool(description="List the supported models in GPT-DB project.")
def list_gptdb_support_models(
    model_type: Annotated[
        str, Doc("The model type, LLM(Large Language Model) and EMBEDDING).")
    ] = "LLM",
) -> str:
    """List the supported models in gptdb."""
    from gptdb.configs.model_config import EMBEDDING_MODEL_CONFIG, LLM_MODEL_CONFIG

    if model_type.lower() == "llm":
        supports = list(LLM_MODEL_CONFIG.keys())
    elif model_type.lower() == "embedding":
        supports = list(EMBEDDING_MODEL_CONFIG.keys())
    else:
        raise ValueError(f"Unsupported model type: {model_type}")
    return "\n\n".join(supports)
