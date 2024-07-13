from betterproto import Casing

from maitai_gen.config import Config, InferenceLocations, ModelConfig

from maitai_back.services import model_service

SERVER_PROVIDERS = ["groq", "openai", "anthropic"]
CLIENT_PROVIDERS = ["openai"]


# Initialize MODELS and last_fetch_time as global variables
import time

MODELS = None
LAST_FETCH_TIME = None
TTL = 60 * 60 

def initialize_models():
    global MODELS, LAST_FETCH_TIME
    current_time = time.time()
    if MODELS is None or (current_time - LAST_FETCH_TIME) > TTL:
        MODELS = model_service.get_models(-1)
        LAST_FETCH_TIME = current_time

initialize_models()

DEFAULT_CLIENT_MODEL = "gpt-4o"
DEFAULT_SERVER_MODEL = "llama3-70b-8192"


def get_default_config() -> Config:
    return Config(
        inference_location=InferenceLocations.SERVER,
        evaluation_enabled=True,
        apply_corrections=True,
        model='gpt-4o',
        temperature=1,
        streaming=False,
        response_format="text",
        stop=None,
        logprobs=False,
        max_tokens=None,
        n=1,
        frequency_penalty=0,
        presence_penalty=0,
        timeout=-1,
        context_retrieval_enabled=False,
    )


def reconcile_config_with_default(config_dict: dict) -> Config:
    default_config_json = get_default_config().to_pydict(casing=Casing.SNAKE)
    for key, value in default_config_json.items():
        if key not in config_dict:
            config_dict[key] = value
    return Config().from_pydict(config_dict)


def get_model_provider(model_name: str):
    for model in MODELS:
        if model.model == model_name:
            return model.provider
    return None


def get_models(providers):
    models = []
    for model in MODELS:
        if model.provider in providers:
            models.append(model.model)
    return models


def get_available_models():
    model_config = ModelConfig(
        all_models=[m.model for m in MODELS],
        client_models=get_models(CLIENT_PROVIDERS),
        server_models=get_models(SERVER_PROVIDERS),
        default_client_model=DEFAULT_CLIENT_MODEL,
        default_server_model=DEFAULT_SERVER_MODEL,
    )
    return model_config.to_pydict(casing=Casing.SNAKE)
