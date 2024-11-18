from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key= os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
Prompt = '''You are a legal-aid assistant bot who knows everything about the Indian Constitution. Help with the following question.

'''
def get_response(prompt):
  GemPrompt = Prompt + prompt
  response = model.generate_content(GemPrompt)
  return response.text
