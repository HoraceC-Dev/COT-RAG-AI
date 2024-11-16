<div align="center">
    <h1>COT RAG-AI Integration: Maximize the Potential of RAG</h1>
</div>
<div align="center">
    <p>:star: Empowering AI Agents with human-like reasoning and chain-of-thought capabilities. :star:</p>
</div>

## Table of Contents
- [Introduction](#Introduction)
- [Features](#Features)
- [Usage](#Usage)
- [Example](#Example)
- [Installation](#Installation)
- [License](#license)
- [Disclaimer](#Disclaimer)

# Introduction
COT RAG-AI Integration enhances Retrieval-Augmented Generation (RAG) systems by incorporating chain-of-thought (COT) reasoning. This project combines advanced language models with custom workflows to handle complex queries requiring multi-step reasoning, improving the relevance and accuracy of generated responses.

# Features
**Advanced Reasoning with GPT-4**: Utilizes GPT-4 for human-like reasoning in handling complex queries.
**Custom RAG System**: Built using LangChain and LangGraph for sophisticated, reasoning-based workflows.
Semantic Search and Workflows: Encodes queries into semantic embeddings to retrieve relevant Standard Operating Procedures (SOPs).
**Dynamic Responses**: Adapts to user inputs, providing personalized guidance through dynamic processes.
Scalable and Flexible: Reduces the need for multiple specialized models by retrieving appropriate workflows for various queries.
# Usage
Ideal for applications requiring coherent, multi-step reasoning:

**Customer Support**: Provides precise answers from a knowledge base to improve response quality.
**Technical Problem Solving**: Offers step-by-step guidance for complex issues.
**Educational Tutoring**: Explains concepts progressively while maintaining logical flow.
**Professional Assistance**: Assists in legal, medical, and financial queries with precise, sourced answers.

# Example
Here's an example of how the COT RAG-AI Integration works:

Let say a customer asks, "Why is my laptop battery draining so quickly after the latest update?"

![RAG Flow](assets/COT-RAG%20System.jpeg)

Next, the chatbot guides the user through the troubleshooting steps:

- Step 1: "Let's check your battery usage statistics. Go to Settings > Battery > Battery Usage. Do you see any apps consuming excessive power?"

- User Response: "Yes, there's an app that's using a lot of power."

- Step 2: "Try updating or uninstalling that app to see if it improves battery life."

- Step 3: "Also, adjust your screen brightness and disable unnecessary background services."

- Step 4: "After making these changes, monitor your battery performance and let me know if the issue persists."

Adaptive Responses: Based on the user's feedback at each step, the chatbot adjusts its guidance accordingly.

# Installation
### Clone the Repository:
```bash
git clone https://github.com/HoraceC-Dev/COT-RAG-AI.git
```
### Navigate to the Project Directory:
```bash
cd COT-RAG-AI
```
### Install Dependencies:
```bash
pip install -r requirements.txt
```
### Set Up API Keys:
Obtain an OpenAI API key for GPT-4 and store the API Key in a .env File

Create a .env file in the project root directory and add the following line:
```env
OPENAI_API_KEY=your_openai_api_key
```

### Run Examples/Test Cases:
After setting up everything, run the **main.py** script to test the setup and explore the pre-built examples:
```bash
python main.py
```
This will execute two example test cases to demonstrate the functionality of the project.

#### Customization:
Feel free to add your own workflows or scenarios by modifying the **src/strings.py** file.
This file provides a customizable interface for updating existing scenarios.

# License
This project is licensed under the MIT License - see the [LICENSE](License) file for details.

# Disclaimer
The COT RAG System is intended for educational purposes only. The creator assumes no responsibility for any consequences arising from it use. Users are advised to comply with appropriate terms of service of relevant usage and adhere to all applicable laws, regulartions, and ethical guidlines.
