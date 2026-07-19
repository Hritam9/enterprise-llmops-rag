from pathlib import Path


class PromptRegistry:

    PROMPTS = {

        "v1": "configs/prompts.yaml",

        "v2": "configs/prompts_v2.yaml",

    }

    @classmethod
    def load(cls, version="v1"):

        return Path(

            cls.PROMPTS[version]

        ).read_text()
