import chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
# Document class to store question and metadata(workflow)
class Document():
    def __init__(self, page_content, metadata):
        self.page_content = page_content
        self.metadata = metadata

    def __repr__(self):
        return f"Document(page_content='{self.page_content}', metadata={self.metadata})"

# Dataset class to handle document conversion and vectorization
class Dataset():
    def __init__(self, documents):
        self.documents = documents

    def __repr__(self):
        return f"Dataset(documents={self.documents})"

    # Transforms the dataset into a list of Document objects
    def _docs_transformation(self):
        return [
            Document(page_content=row['question'], metadata={'Flow': row['flow']})
            for index, row in self.documents.iterrows()
        ]

    # Converts documents into a vector store using OpenAI embeddings and Chroma
    def _vectorization(self, documents):
        chromadb_client = chromadb.Client()
        try:
            chromadb_client.create_collection(name="demo")
        except:
            print("The vectorstore has already been created.")

        embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        return Chroma.from_documents(documents, embeddings, collection_name="demo")
        # Main function of the class to create a dataset and vectorize documents
    def dataset_creation(self):
        list_of_docs = self._docs_transformation()
        return self._vectorization(list_of_docs)