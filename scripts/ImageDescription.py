from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders.image import UnstructuredImageLoader

from langchain_openai import ChatOpenAI

from scripts.Templates import SHORT_DESCRIPTION_TEMPLATE
from dotenv import load_dotenv

load_dotenv("../.env")

# LLM Components
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002", temperature=0)
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


short_description_prompt = PromptTemplate(
    template=SHORT_DESCRIPTION_TEMPLATE, input_variables=["image"]
)
short_description_chain = short_description_prompt | llm


class GetImageDescription:

    def __init__(self, image_path):

        global short_description_chain

        self.image_path = image_path
        self.chain = short_description_chain
        self.image_data = None

    def initialize_image_data(self):
        loader = UnstructuredImageLoader(self.image_path)  # , mode="elements")
        data = loader.load()
        self.image_data = data

    def generate_description(self):
        self.initialize_image_data()
        result = self.chain.invoke({"image": self.image_data})
        return result.content

    @classmethod
    def describe(cls, image_path):
        instance = cls(image_path)
        description = instance.generate_description()
        return description
