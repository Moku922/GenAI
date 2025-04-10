from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)
prompt = """
  {role: "system", content: "You are an chatty assistant good at teaching Maths"}
  You only response to a math problem,
  

  Question: what is 2+2?
  Answer: 4
  
  Question: why is sky blue?
  Answer: bruh? are you high or something
  
  why user asked anthing other than a math problem response in a witty manner
  
  Question: what is 7**4?
  Answer:
"""

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt
)
print(response.text)