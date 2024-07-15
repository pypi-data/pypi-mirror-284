"""Proxy models."""


def __lazy_import(name):
    module_path = {
        "OpenAILLMClient": "gptdb.model.proxy.llms.chatgpt",
        "GeminiLLMClient": "gptdb.model.proxy.llms.gemini",
        "SparkLLMClient": "gptdb.model.proxy.llms.spark",
        "TongyiLLMClient": "gptdb.model.proxy.llms.tongyi",
        "WenxinLLMClient": "gptdb.model.proxy.llms.wenxin",
        "ZhipuLLMClient": "gptdb.model.proxy.llms.zhipu",
        "YiLLMClient": "gptdb.model.proxy.llms.yi",
        "MoonshotLLMClient": "gptdb.model.proxy.llms.moonshot",
        "OllamaLLMClient": "gptdb.model.proxy.llms.ollama",
        "DeepseekLLMClient": "gptdb.model.proxy.llms.deepseek",
    }

    if name in module_path:
        module = __import__(module_path[name], fromlist=[name])
        return getattr(module, name)
    else:
        raise AttributeError(f"module {__name__} has no attribute {name}")


def __getattr__(name):
    return __lazy_import(name)


__all__ = [
    "OpenAILLMClient",
    "GeminiLLMClient",
    "TongyiLLMClient",
    "ZhipuLLMClient",
    "WenxinLLMClient",
    "SparkLLMClient",
    "YiLLMClient",
    "MoonshotLLMClient",
    "OllamaLLMClient",
    "DeepseekLLMClient",
]
