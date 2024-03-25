# conversational_QA_chatbot

A conversational question-answering chatbot utilizing Google's Generative AI LLM GeminiPro capabilities to provide responses to user inquiries.

https://github.com/umairsiddique3171/conversational_QA_chatbot/assets/148565997/9de823a7-f93d-4ac3-b1ad-fc37e09e507d

## Overview

This project implements a chatbot capable of engaging in a question-and-answer dialogue with users. It employs Google's Generative AI, specifically the GeminiPro model, to generate responses to user queries.

## Dependencies

- [python-dotenv](https://pypi.org/project/python-dotenv/): For loading environment variables from a .env file.
- [Streamlit](https://streamlit.io/): A popular Python library for building interactive web applications.
- [google-generativeai](https://pypi.org/project/google-generativeai/): Google's Generative AI library for AI-generated content.

## Setup

1. Clone the repository:

    ```
    git clone https://github.com/umairsiddique3171/conversational_QA_chatbot.git
    cd conversational_QA_chatbot
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Set up a `.env` file with the required environment variable `GOOGLE_API_KEY`.

4. Run the application:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Upon running the application, users are presented with an input field where they can ask questions.
2. After submitting a question, the chatbot responds with relevant information.
3. The conversation history is displayed to users, showing both user queries and bot responses.

## Code Overview

The primary functionality of the application is implemented in the `app.py` file. Here's a brief overview of the code:

- **Dependencies**: Importing necessary libraries and setting up environment variables.
- **Configuration**: Configuring the Generative AI model with the Google API key.
- **Streamlit App**: Initializing the Streamlit application and setting the page configuration.
- **Chat Interaction**: Handling user input, obtaining responses from the Generative AI model, and displaying them to the user.
- **Chat History**: Displaying the conversation history, including both user queries and bot responses.

## Notes

We use .env files primarily for configuring environment variables in software applications. Here's why they are commonly used:
- Configuration Management: .env files allow developers to manage configurations such as API keys, database URIs, and other sensitive information without hardcoding them directly into the source code. This separation of configuration from code promotes better security practices and makes it easier to maintain different configurations for development, testing, and production environments.
- Portability: Environment variables specified in a .env file can be easily transferred between different environments or shared with collaborators. This simplifies deployment processes and ensures consistent configurations across different setups.
- Security: Storing sensitive information like passwords or API keys directly in source code can pose security risks, especially if the code is publicly accessible or shared among multiple developers. .env files provide a way to keep such sensitive data separate and secure.
- Ease of Use: Reading environment variables from a .env file is a common practice in many programming languages and frameworks. It's straightforward and allows developers to access configuration values easily within their code.
- Flexibility: With .env files, developers can quickly adjust configurations without modifying the source code. This flexibility is valuable during development and deployment, as it allows for rapid iteration and experimentation.

## License

This project is licensed under the [MIT License](https://github.com/umairsiddique3171/conversational_QA_chatbot/blob/main/LICENSE).

## Author 

[@umairsiddique3171](https://github.com/umairsiddique3171)
