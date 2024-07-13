import llm
from llm.default_plugins.openai_models import Chat

MODELS = (
    "hive"
)

class HyperbeeChat(Chat):
    def __init__(self, model_name):
        super().__init__(
            model_name=model_name,
            model_id=(
                "hyperbee-chat"
            ),
            api_base="https://api.hyperbee.ai/v1/",
        )

    def __str__(self):
        return "Hyperbee: {}".format(self.model_id)

@llm.hookimpl
def register_models(register):
    for model_id in MODELS:
        register(HyperbeeChat(model_id))
