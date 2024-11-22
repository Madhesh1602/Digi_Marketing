from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

from scripts.Templates import LONG_DESCRIPTION_TEMPLATE
from dotenv import load_dotenv

import os
from langfuse.callback import CallbackHandler

load_dotenv("../.env")

langfuse_handler = CallbackHandler(
    public_key=os.environ["LANGFUSE_PUBLIC_KEY"],
    secret_key=os.environ["LANGFUSE_SECRET_KEY"],
    host=os.environ["LANGFUSE_HOST"],
)


class GenerateProductContent:

    def __init__(self, product_data):

        self.data = product_data
        self.chain = None
        self.revision_chain = None
        self.content = None

    def initialize_chain(self):

        temperature = self.data["temperature"]
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=temperature)

        content_prompt = PromptTemplate(
            template=LONG_DESCRIPTION_TEMPLATE,
            input_variables=[
                "business_name",
                "target_customer",
                "min_age",
                "max_age",
                "region",
                "content_duration",
                "content_type",
                "product_name",
                "image_description",
                "social_media",
                "content_goal",
                "occasion_type",
                "hooks",
                "language",
                "word_count",
            ],
        )

        content_generation_chain = content_prompt | llm
        self.chain = content_generation_chain

    def generate_content(self):
        if self.chain is None:
            self.initialize_chain()
        input_dict = self.data
        del input_dict["temperature"]
        result = self.chain.invoke(input_dict, config={"callbacks": [langfuse_handler]})
        self.content = result.content
        return self.content

    def initialize_revise_chain(self):
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content="You are an experienced Digital Marketing content creator. Provide content as asked and revise the content if any feedback is provided."
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )
        self.revision_chain = prompt | llm

    def revise_content(self, query):
        if self.revision_chain is None:
            self.initialize_revise_chain()
        result = self.revision_chain.invoke(
            {
                "messages": [
                    AIMessage(content=f"{self.content}"),
                    HumanMessage(content=f"{query}"),
                ],
            },
            config={"callbacks": [langfuse_handler]},
        )
        self.content = result.content
        return self.content
