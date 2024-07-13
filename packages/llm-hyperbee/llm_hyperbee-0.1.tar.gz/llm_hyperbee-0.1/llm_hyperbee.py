import llm
from llm.default_plugins.openai_models import Chat

MODELS = (
    "workspace/llm_model"
)


class HyperbeeChat(Chat):
    def __init__(self, model_name):
        super().__init__(
            model_name=model_name,
            model_id=(
                "hyperbee-chat"
            ),
            api_base="http://34.110.195.245/v1/",
        )

    def __str__(self):
        return "Hyperbee: {}".format(self.model_id)


@llm.hookimpl
def register_models(register):
    for model_id in MODELS:
        register(HyperbeeChat(model_id))
