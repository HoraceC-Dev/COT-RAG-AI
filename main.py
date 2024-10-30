from uuid import uuid4
from src.custom_tools import CustomToolFunction
from src.chatbot import initialize_resources
from src.graph_setup import set_up_graph 
from src.strings import sample_conversation_1, sample_conversation_2
from src.chatbot import run_conversation

def main():
    llm, flow_retriever = initialize_resources()
    tool = CustomToolFunction()
    tools = tool.create_tool()
    final_graph = set_up_graph(llm, flow_retriever, tools)
    # demonstration 1
    run_conversation(sample_conversation_1, final_graph)
    # demonstration 2
    run_conversation(sample_conversation_2, final_graph)


if __name__ == "__main__":
    main()
