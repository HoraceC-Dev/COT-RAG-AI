from typing import TypedDict, Annotated
from langgraph.graph.message import AnyMessage, add_messages

# State definition for the graph
class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    flow: str