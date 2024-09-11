from langchain_core.messages import ToolMessage
from langgraph.graph import StateGraph
from langchain.prompts import ChatPromptTemplate

# Fallback function to handle tool errors
def handle_tool_error(state: StateGraph) -> dict:
    error = state.get("error")
    tool_calls = state["messages"][-1].tool_calls
    return {
        "messages": [
            ToolMessage(
                content=f"Error: {repr(error)}\nPlease fix your mistakes.",
                tool_call_id=tc["id"],
            )
            for tc in tool_calls
        ]
    }


# Helper function to create the prompt template
def create_prompt():
    return ChatPromptTemplate.from_messages(
        [
            ("system", """You are an expert agent capable of fulfilling the user query with the following flow:\n{flow}\nNote: You have the responsibility to follow up with the user if you require any further clarification for the purpose of answering the user query."""),
            ("placeholder", "{messages}")
        ]
    )