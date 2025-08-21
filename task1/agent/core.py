from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


class Agent:
    def __init__(self,
                 model: str = 'gpt-4o-mini',
                 temperature: float = 1.0,
                 max_tokens: int = 4096,
                 max_retry: int = 1,
                 tools: list = None):
        self.model = ChatOpenAI(
            base_url=os.getenv("BASE_URL"),
            api_key=os.getenv("API_KEY"),
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            max_retries=max_retry,
        )
        if tools:
            self.model = self.model.bind_tools(tools)

    def query(self, messages= None, system_prompt: str='', prompt_variables: dict = None):

        if prompt_variables:
            system_prompt = system_prompt.format_map(prompt_variables)
        if messages:
            prompt = ChatPromptTemplate.from_messages(
                [
                    SystemMessage(content=system_prompt),
                    MessagesPlaceholder(variable_name="messages"),
                ]
            ).invoke(input=messages)
        else:
            prompt = system_prompt

        try:
            return {"response": self.model.invoke(prompt), "exception": None}
        except Exception as e:
            return {"response": None, "exception": e}
