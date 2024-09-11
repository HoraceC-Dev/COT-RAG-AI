from src.graph_state import State
from src.utils import create_prompt, handle_tool_error

from langgraph.graph import StateGraph, END
from typing import Literal
from langchain_core.runnables import RunnableLambda
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode

# Function to set up and compile the state graph
def set_up_graph(llm, flow_retriever, tools):

    # Function for generating responses
    def generate(state):
        prompt = create_prompt()
        chain = prompt | llm.bind_tools(tools)
        result = chain.invoke({"flow": state["flow"], "messages": state["messages"]})
        msg = state["messages"] + [result]
        return {"messages": msg}
    # Routing function to check if tool execution is required
    def route_check(state) -> Literal["__end__", "tool_executor"]:
        return "tool_executor" if state["messages"][-1].tool_calls else END

    # Function to retrieve the flow for the user's request
    def get_flow(state):
        if len(state["messages"]) == 1:
            flow = flow_retriever.get_relevant_documents(state["messages"][-1].content)
            return {"flow": flow[0].metadata["Flow"]}

    graph = StateGraph(State)
    graph.add_node("generate", generate)
    graph.add_node("set_flow", get_flow)
    graph.add_node("tool_executor", create_tool_node_with_fallback(tools))
    graph.add_edge("set_flow", "generate")
    graph.set_entry_point("set_flow")
    graph.add_conditional_edges("generate", route_check)
    graph.add_edge("tool_executor", "generate")

    return graph.compile(checkpointer=MemorySaver())

# Function to create a tool node with a fallback for error handling
def create_tool_node_with_fallback(tools: list) -> dict:
    return ToolNode(tools).with_fallbacks(
        [RunnableLambda(handle_tool_error)], exception_key="error"
    )