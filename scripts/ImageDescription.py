from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders.image import UnstructuredImageLoader

from langchain_openai import ChatOpenAI

from scripts.Templates import SHORT_DESCRIPTION_TEMPLATE
from dotenv import load_dotenv

import base64
from langfuse.openai import openai
from openai import OpenAI

load_dotenv("../.env")

client = OpenAI()


class GetImageDescription:

    def __init__(self, image_path):

        self.image_path = image_path
        self.base64_image = None

    def encode_image(self):
        with open(self.image_path, "rb") as image_file:
            self.base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    def generate_description(self):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """{SHORT_DESCRIPTION_TEMPLATE}""",
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{self.base64_image}"
                            },
                        },
                    ],
                }
            ],
        )
        return response.choices[0].message.content

    @classmethod
    def describe(cls, image_path):
        instance = cls(image_path)
        instance.encode_image()
        description = instance.generate_description()
        return description
