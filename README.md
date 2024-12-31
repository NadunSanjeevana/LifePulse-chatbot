# Work-Life Balancer Chatbot (Life Pulse App)

## Overview
The **Work-Life Balancer Chatbot** is a Node.js-based conversational assistant designed to enhance the functionality of the Work-Life Balancer app. The chatbot interacts with users to provide assistance in task management, schedule planning, and answering queries about work-life balance. It integrates seamlessly with the backend services to deliver real-time responses and personalized recommendations.

## Features
- **Natural Language Processing (NLP)**: Understands user inputs using Dialogflow or Rasa.
- **Task Management**: Assists users in creating, updating, and deleting tasks through chat commands.
- **Mindfulness Tips**: Provides curated tips to improve work-life balance upon user request.
- **Progress Insights**: Offers analytics and progress updates in a conversational manner.

## Tech Stack
- **Programming Language**: Node.js
- **Framework**: Express.js
- **NLP Platform**: Dialogflow or Rasa
- **Database**: Firebase Firestore
- **Deployment**: Google Cloud Platform (GCP)

## Installation

### Prerequisites
- Node.js (v14 or above)
- npm or Yarn
- Firebase account with a configured project
- Dialogflow or Rasa account

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd work-life-balancer-chatbot
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Set up Firebase:
   - Create a Firebase project in the [Firebase Console](https://firebase.google.com/).
   - Download the `serviceAccountKey.json` file and place it in the root directory.
   - Enable Firestore and Firebase Authentication.

4. Set up Dialogflow or Rasa:
   - For Dialogflow:
     - Create an agent in the Dialogflow console.
     - Export the agent JSON file and integrate it into the project.
   - For Rasa:
     - Train your model and link the endpoint with the chatbot.

5. Configure environment variables:
   - Create a `.env` file in the root directory and add the following:
     ```env
     PORT=5000
     FIREBASE_PROJECT_ID=<your_firebase_project_id>
     FIREBASE_CLIENT_EMAIL=<your_firebase_client_email>
     FIREBASE_PRIVATE_KEY=<your_firebase_private_key>
     NLP_PLATFORM=<dialogflow_or_rasa>
     ```

6. Start the server:
   ```bash
   npm start
   # or for development
   npm run dev
   ```


## Deployment
1. Deploy the chatbot to a cloud service (e.g., Google Cloud Function):
   ```bash
   gcloud functions deploy chatbot --runtime nodejs14 --trigger-http
   ```
2. Link the chatbot with your Dialogflow or Rasa endpoint for seamless integration.

