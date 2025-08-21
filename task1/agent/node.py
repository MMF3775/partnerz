import os
from dotenv import load_dotenv
from .core import Agent
load_dotenv()  # take environment variables
from .state import State
from .prompt import *
from task1.rag.rag import SimpleRag


class Node:

    @staticmethod
    def query(state: State) -> State:
        rag = SimpleRag(state.get('knowledge'))
        res = rag.query(state.get('query'))
        return {'answer': res}

    @staticmethod
    def aggregator(state: State) -> State:
        variables = {
            "query": state.get('query'),
            "content": state.get('answer'),
        }
        agg = Agent()
        res = agg.query(
            system_prompt=aggregator_prompt,
            prompt_variables=variables,
        )

        return {"exception": res.get('exception')} if res.get("exception") else {
            "response": res.get("response").content}
