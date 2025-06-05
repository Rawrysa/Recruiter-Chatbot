# Recruiter-Chatbot

A conversational AI assistant built with Streamlit, leveraging LLMs and semantic search to answer questions about Galaletsang Modimola using information from a resume and profile data.

## Features
- Chat interface powered by Streamlit
- Uses Mistral LLM API for natural language responses
- Semantic search with FAISS and Sentence Transformers
- Contextual answers based on Galaletsang's resume and profile
- Downloadable CV when requested in chat
- Automatic chat timeout for inactivity

## Project Structure
```
docs/
    your_resume_or_cv.pdf   # Resume used for context
    professional_background_summary.txt                       # Profile data for semantic search
scripts/
    interface.py                      # Streamlit app interface
    chatbot.py                        # Chatbot logic and LLM integration
    s_search.py                       # Semantic search utilities
    logger.py                         # Logging utilities
logs/
    chatbot.log                       # Log file
```

## Setup
1. **Clone the repository**

2. **Install dependencies** (preferably in a virtual environment):
   ```sh
   pip install -r requirements.txt
   ```
   (Ensure you have `streamlit`, `faiss-cpu`, `sentence-transformers`, `python-dotenv`, and `mistralai`.)
   
3. **Set up environment variables**:
   - Create a `.env` file in the root directory with your Mistral API key:
     ```env
     MISTRAL_API_KEY=your_api_key_here
     ```
     
4. **Run the app**:
   ```sh
   streamlit run scripts/interface.py
   ```

## Usage
- Open the Streamlit app in your browser.
- Ask questions about Galaletsang Modimola.
- If you mention "CV" or "resume" in your query, a download button for the PDF will appear.
- The chat will end automatically after 60 seconds of inactivity.

## Notebooks
- Use `notebooks/testing_grounds.ipynb` for experimenting with embeddings, semantic search, and LLM queries.

## License
This project is for educational and demonstration purposes.
