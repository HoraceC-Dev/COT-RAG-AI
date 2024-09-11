from src.custom_tool_function import CustomToolFunction
from src.chatbot import initialize_resources
from src.graph_setup import set_up_graph 
from src.demonstrations import demonstration_example_1, demonstration_example_2 

# Entry point of the program
if __name__ == "__main__":
    llm, flow_retriever = initialize_resources()
    tool = CustomToolFunction()
    tools = tool.create_tool()
    final_graph = set_up_graph(llm, flow_retriever, tools)

    demonstration_example_1(final_graph)
    demonstration_example_2(final_graph)