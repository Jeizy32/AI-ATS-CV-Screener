import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key dari .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

print("Mencari model yang tersedia untuk API Key ini...")
print("-" * 30)

# Menampilkan semua model yang support generateContent
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)