#vector embedding of Gemini

from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found in .env file. Please set it.")
    exit()

client = genai.Client(api_key=api_key)




text = " i am a coder "
result = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents=text)

print(result.embeddings)
