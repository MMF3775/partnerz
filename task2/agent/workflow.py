from langgraph.graph import StateGraph, START, END
from .state import State
from .node import Node
from langgraph.checkpoint.memory import MemorySaver

class Workflow:
    graph_builder = StateGraph(State)
    memory = MemorySaver()

    graph_builder.add_node("Bot", Node.bot)
    graph_builder.add_node("BotTool", Node.BotTools)

    graph_builder.add_edge(START, "Bot")
    graph_builder.add_conditional_edges('Bot',Node.bot_router)
    graph_builder.add_edge('BotTool', "Bot")
    graph_builder.add_edge("Bot", END)

    graph = graph_builder.compile(checkpointer=memory)