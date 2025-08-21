"""
This module defines a TypedDict used to represent the state of the agent.  

The State TypedDict includes:  
- messages: list of the user input query  

Usage:  
- This state structure can be utilized in applications that require tracking messages,  
  summaries, and token usage, such as chatbots or language model applications.  
"""
from typing import Annotated

from langgraph.graph import add_messages
from typing_extensions import TypedDict

class State(TypedDict):
    query: str
    messages: Annotated[list, add_messages]