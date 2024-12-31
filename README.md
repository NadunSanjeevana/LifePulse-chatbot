# Work-Life Balancer Chatbot (Life Pulse App)

## Overview
The **Work-Life Balancer Chatbot** is a Python-based conversational assistant designed to enhance the functionality of the Work-Life Balancer app. The chatbot interacts with users to assist in task management, and answering queries about work-life balance. It integrates seamlessly with the backend services to deliver real-time responses and personalized recommendations. It used Qwen LLM model.

## Features
- **Natural Language Processing (NLP)**: Understands user inputs using Dialogflow or Rasa.
- **Task Management**: Assists users in creating, updating, and deleting tasks through chat commands.
- **Mindfulness Tips**: Provides curated tips to improve work-life balance upon user request.
- **Progress Insights**: Offers analytics and progress updates conversationally.

## Tech Stack
- **Programming Language**: Node.js
- **Framework**: Express.js

## Installation

### Prerequisites
- Python
- Flask
- Ollama
- Qwen Model

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd work-life-balancer-chatbot
   ```

2. Start Ollama

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:
   ```bash
   python chatbot_api.py
   ```

1. Deploy the chatbot to a cloud service (e.g., Google Cloud Function):
   ```bash
   gcloud functions deploy chatbot --runtime nodejs14 --trigger-http
   ```
2. Link the chatbot with your Dialogflow or Rasa endpoint for seamless integration.

