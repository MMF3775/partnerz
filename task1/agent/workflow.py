from langgraph.graph import StateGraph, START, END
from .state import State
from .node import Node


class Workflow:
    graph_builder = StateGraph(State)

    graph_builder.add_node("Knowledge", Node.query)
    graph_builder.add_node("Aggregator", Node.aggregator)

    graph_builder.add_edge(START, "Knowledge")
    graph_builder.add_edge("Knowledge", "Aggregator")
    graph_builder.add_edge("Aggregator", END)

    graph = graph_builder.compile()