import os
from typing import Literal

from dotenv import load_dotenv
from langgraph.prebuilt import ToolNode

from .core import Agent
load_dotenv()  # take environment variables
from .state import State
from .prompt import *
from task1.rag.rag import SimpleRag


class Node:
    bot_tools = []
    BotTools = ToolNode(tools=bot_tools)
    @staticmethod
    def bot(state: State) -> State:
        variables = {
            "question": state.get('query'),
        }
        agg = Agent(tools=Node.bot_tools)
        res = agg.query(
            system_prompt=bot_prompt,
            prompt_variables=variables,
            messages=state.get('messages')
        )
        return {"exception": res.get('exception')} if res.get("exception") else {
            "messages": [res.get("response")]}

    @staticmethod
    def bot_router(state: State) -> Literal[
        "__end__", "BotTool"]:
        if state.get("messages")[-1].tool_calls:
            return "BotTool"
        else:
            return "__end__"