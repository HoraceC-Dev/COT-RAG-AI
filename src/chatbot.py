import os
import uuid
import pandas as pd

from dotenv import load_dotenv

from langchain_core.messages import HumanMessage

from src.llm import openai_llm
from src.dataset import Dataset
from src.flow_retriever import FlowRetriever
from src.strings import example_question_1, example_question_2, question_1_workflow, question_2_workflow
# Initialize resources such as LLMs, vectorstore, and flow retriever

def initialize_resources():
    # Load environment variables from .env file
    load_dotenv()
    # Access the API key
    openai_api_key = os.getenv("OPENAI_API_KEY")
    os.environ["OPENAI_API_KEY"] = openai_api_key

    documents = pd.DataFrame({
        'question': [example_question_1, example_question_2],
        'flow': [question_1_workflow, question_2_workflow],
    })

    llm = openai_llm()

    dataset = Dataset(documents)

    vectorstore = Dataset(documents).dataset_creation()

    flow_retriever = FlowRetriever(vectorstore)

    return llm, flow_retriever

# Helper function to run conversation examples
def run_conversation(messages, final_graph):
    thread_id = str(uuid.uuid4())
    print("Simulation begins")
    for message in messages:
        print(f"User: {message}")
        print("---------------------------------")
        events = final_graph.stream({"messages": [HumanMessage(content=message)]}, config={"configurable": {"thread_id": thread_id}})
        for event in events:
            if 'generate' in event and 'messages' in event['generate']:
                if event['generate']['messages'][-1].content != "":
                    print("\n---------------------------------")
    print("Conversation completed.")
    print("---------------------------------")
    print("---------------------------------")
    print("---------------------------------")
    