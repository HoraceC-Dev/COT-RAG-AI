from langchain_openai import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Function to initialize the OpenAI LLM (GPT-4o)
def openai_llm():
    # There are a lot of options(e.g. 3.5, 4o mini), in this example we will be using 4o AUG
    return ChatOpenAI(model="gpt-4o-2024-08-06", temperature=0, streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
