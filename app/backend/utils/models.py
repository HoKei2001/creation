from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ModelConfig:
    base_url: str
    model_name: str
    api_key: str

# Available models configuration
AVAILABLE_MODELS: Dict[str, ModelConfig] = {
    "deepseek-v3": ModelConfig(
        base_url="http://10.2.3.50:10002/v1/",
        model_name="deepseek-ai/deepseek-v3",
        api_key="123"
    ),
    "deepseek-r1": ModelConfig(
        base_url="http://10.4.33.15:80/v1/",
        model_name="inarikami/DeepSeek-R1-Distill-Qwen-32B-AWQ",
        api_key="123"
    ),
    "llama-33": ModelConfig(
        base_url="http://10.4.33.13:80/v1",
        model_name="ibnzterrell/Meta-Llama-3.3-70B-Instruct-AWQ-INT4",
        api_key="123"
    ),
    "qwen-qwq": ModelConfig(
        base_url="http://10.2.3.50:11434/v1",
        model_name="qwq:latest",
        api_key="123"
    )
}

# Default model
DEFAULT_MODEL = "deepseek-r1" 