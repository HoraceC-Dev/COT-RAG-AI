# FlowRetriever class to retrieve relevant documents from the vector store
class FlowRetriever():
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    # Convert and set up the retriever using vector store
    def _retriever(self):
        return self.vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 1})
    # Retrieves the most similar document based on the query
    def get_relevant_documents(self, query):
        retriever = self._retriever()
        return retriever.invoke(query)