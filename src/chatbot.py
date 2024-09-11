import os
import uuid
import pandas as pd

from dotenv import load_dotenv

from langchain_core.messages import HumanMessage

from src.llm import openai_llm
from src.dataset import Dataset
from src.flow_retriever import FlowRetriever

# Initialize resources such as LLMs, vectorstore, and flow retriever
def initialize_resources():
    # Load environment variables from .env file
    load_dotenv()
    # Access the API key
    openai_api_key = os.getenv("OPENAI_API_KEY")
    os.environ["OPENAI_API_KEY"] = openai_api_key

    # Example questions and flows
    example_question_1 = """
    I have forgotten my password and lost my email address. Is there any way I can reset my password for my saving account? I still have my user ID for my XYZ bank account.
    """
    example_question_1_flow = """
    1. User must provide their mobile number, user ID if applicable, and legal name that is associated with the account.
    2. Check whether there is an account linked to the information provided.
    3. Verify the identity of the user once.
    4. Ask user for the new password.
    5. Update the user's password.
    6. Inform the user that their password has been updated.

    If the user is not able to provide sufficient information, please inform the user that you are not able to proceed.
    """
    example_question_2 = """
    I would like to order physical checks and receive them as soon as possible. Could you assist with that?
    """
    example_question_2_flow = """
    1. Users must provide their User ID and password for the account that they want to order physical checks from.
    2. Verify user's identity once.
    3. Ask whether they prefer pick-up or home delivery service.
    4. Inform that the fees will be subtracted from their account balance.
    5. Help the users to order checks and inform them afterward.

    If the user is not able to provide sufficient information, please inform the user that you are not able to proceed.
    """

    # Create a dataset using pandas DataFrame
    documents = pd.DataFrame({
        'question': [example_question_1, example_question_2],
        'flow': [example_question_1_flow, example_question_2_flow],
    })

    llm = openai_llm()
    dataset = Dataset(documents)
    vectorstore = dataset.dataset_creation()
    flow_retriever = FlowRetriever(vectorstore)

    return llm, flow_retriever

# Helper function to run conversation examples
def run_conversation(messages, final_graph):
    thread_id = str(uuid.uuid4())
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