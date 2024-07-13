import llm
from llm.default_plugins.openai_models import Chat

MODELS = (
    "auto",
    "claude-3-haiku-20240307",
    "claude-3-opus-20240229",
    "claude-3-sonnet-20240229",
    "claude-3-5-sonnet-20240620",
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    "small-bee-en",
    "gpt-4o",
    "gpt-3.5-turbo",
    "gpt-4-turbo",
    "gpt-4",
    "llama-3-70b-instruct",
)

class HyperbeeChat(Chat):
    needs_key = "hyperbee"
    def __init__(self, model_name):
        super().__init__(
            model_name=model_name,
            model_id=(
                "hyperbee/" + model_name
            ),
            api_base="https://api.hyperbee.ai/v1/",
        )

    def __str__(self):
        return "Hyperbee: {}".format(self.model_id)

@llm.hookimpl
def register_models(register):
    # Only do this if the key is set
    key = llm.get_key("", "hyperbee", "LLM_HYPERBEE_KEY")
    if not key:
        return
    for model_id in MODELS:
        register(HyperbeeChat(model_id))
