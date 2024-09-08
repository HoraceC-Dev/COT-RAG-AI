# AI Integration in Customer Service: Addressing the Limitations with RAG

Nowadays, companies have been introducing AI and various algorithms in the form of chatbots to enhance customer experience. a noticeable and significant gap remains between chatbots and actual human agents. Specifically, chatbots often struggle with:
- Understanding complex or nuanced customer queries where they involve multiple decision trees.
- Handling unexpected or edge-case scenarios.
- Adapting to the context or history of customer interactions, a common limitation in traditional algorithm-driven chatbots.

This project addresses these challenges and aims to develop a more comprehensive chatbot model. The solution integrates the capabilities of pre-trained models like ChatGPT with a custom-built Retrieval-Augmented Generation (RAG) system. 

## RAG
RAG is a commonly used technique for GPT models to improve the accuracy of information by providing access to an external knowledge base.
Secondly, it offers a means to expand the scope of the model's responses without fine-tuning or training on every single piece of information. 

Here is an ex

---

## 🌟 Features
- **Flexibility**: Given a set of executable workflows, the chatbot is capable of fulfilling queries in various fields.
- **Backend Integration**: Connects the chatbot to a backend system (e.g., a database or a third-party API) to fetch dynamic data.
- **Generative AI**: Leverages OpenAI's models to provide human-like responses to user queries.
- **Scalability**: Leverages the RAG system to retrieve decision flows for corresponding queries using a single Generative AI model.
- **Context-Aware Responses**: The chatbot can maintain conversational context for more natural interactions.
---
### Prerequisites:
- Python 3.8
- OpenAI API Key
- Docker (optional)
