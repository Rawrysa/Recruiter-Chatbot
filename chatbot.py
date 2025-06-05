import os
from dotenv import load_dotenv
from mistralai import Mistral
from s_search import SearchEngine
from logger import setup_logger

class Chatbot:
    def __init__(self):
        load_dotenv()

        self.api_key = os.getenv("MISTRAL_API_KEY")
        self.model = "mistral-large-latest"

        self.logger = setup_logger("Chatbot", "logs/chatbot.log")

        try:
            self.client = Mistral(api_key=self.api_key)

            with open("docs/professional_background_summary.txt", "r") as f:
                profile_data = f.read()

            self.search_engine = SearchEngine()

            self.chunks = self.search_engine.chunk_text(profile_data)
            self.search_engine.build_index(self.chunks)

            self.logger.info("Chatbot initialized successfully.")

        except Exception as e:
            self.logger.error(f"Error initializing chatbot: {e}")
            raise RuntimeError("Failed to initialize chatbot. Check logs for details.")

    def get_context(self, user_input):
        try:
            i = self.search_engine.search(user_input)

            top_chunks = [self.chunks[idx] for idx in i[0]]

            profile_data = "\n\n".join(top_chunks)

            self.logger.info("Profile data retrieved successfully.")

        except Exception as e:
            self.logger.error(f"Error retrieving profile data: {e}")
            raise RuntimeError(e)

        return profile_data

    def get_response(self, user_input):
        
        try:

            context = self.get_context(user_input)

            messages = [
                {"role": "system", "content":
                f"""
                You are a helpful assistant trained to answer recruiter and hiring-related questions about Galaletsang Modimola.

                Context:
                {context}

                Use this information to answer recruiter queries clearly and professionally.

                """}
            ]

            messages.extend(user_input)

            response = self.client.chat.complete(
                model=self.model,
                messages=messages
            )

            self.logger.info("Response generated successfully.")
            return response.choices[0].message.content
        
        except Exception as e:
            self.logger.error(f"Error generating response: {e}")
            raise RuntimeError("Failed to generate response. Check logs for details.")
