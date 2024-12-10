Conversational Chatbot 🤖
=========================

This repository contains a conversational chatbot application built using **Streamlit**, designed to enable natural, voice-based interactions with users. The chatbot leverages Google's Generative AI API for intelligent responses and incorporates text-to-speech (TTS) and speech-to-text (STT) functionalities.

* * * * *

Features
--------

-   **Audio Input**: Users can record their voice queries directly in the application.
-   **Speech-to-Text Conversion**: Converts recorded audio into text for processing.
-   **Natural Language Understanding**: Interprets user inputs using Google's Generative AI model.
-   **Text-to-Speech**: Generates audio responses to maintain natural conversation flow.
-   **User Interface**: Provides a sleek and interactive chat interface built with Streamlit.
-   **Footer Microphone Integration**: A floating footer UI for recording and interacting.

* * * * *

Setup and Installation
----------------------

### Prerequisites

-   Python 3.7+
-   Required dependencies (see `requirements.txt`)

### Installation Steps

1.  **Clone the Repository**

    ```
    git clone https://github.com/yourusername/conversational-chatbot.git
    cd conversational-chatbot

    ```

2.  **Install Dependencies**

    ```
    pip install -r requirements.txt

    ```

3.  **Set API Key** Replace the `api_key` variable in `base_model_chatbot.py` with your **Google Generative AI API Key**.

4.  **Run the Application**

    ```
    streamlit run main.py

    ```

* * * * *

File Structure
--------------

```
.
├── main.py                     # Main application file
├── helpers.py                  # Contains utility functions for TTS and STT
├── generate_answer.py          # Chatbot logic with Google Generative AI API integration
├── requirements.txt            # Required Python libraries
├── README.md                   # Project documentation
└── assets                      # Placeholder for storing static assets (if any)

```

* * * * *

Usage
-----

1.  Launch the app using `streamlit run main.py`.
2.  Click the microphone in the floating footer to record your query.
3.  The chatbot transcribes the query, processes it, and responds via text and audio.

* * * * *

Technologies Used
-----------------

-   **Streamlit**: For building the UI.
-   **Google Generative AI**: For intelligent chatbot responses.
-   **SpeechRecognition**: For converting audio input into text.
-   **pyttsx3**: For generating audio responses.
-   **Audio Recorder Streamlit**: For capturing user audio in the app.

* * * * *

Future Enhancements
-------------------

-   **PDF Integration**: Allow users to upload PDFs and query the content.
-   **Multimodal Inputs**: Support for image and video-based queries.
-   **Advanced Models**: Integrate other AI models for domain-specific tasks.

* * * * *

Contributing
------------

Contributions are welcome! Please fork the repository and submit a pull request for review.

* * * * *

License
-------

This project is licensed under the MIT License.

* * * * *

Author
------

Developed by **Your Name**. For queries, feel free to contact: **<deepanrajsakthivel@gmail.com>**.

* * * * *

Acknowledgments
---------------

-   Google Generative AI for providing cutting-edge NLP capabilities.
-   Streamlit for an intuitive app-building platform.
