import time
import google.generativeai as genai

def generate_with_retry(model, prompt, max_retries=5):
    attempt = 0
    wait_time = 2  
    
    while attempt < max_retries:
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            if "429" in str(e):
                print(f"Limit kena! Tunggu {wait_time} detik...")
                time.sleep(wait_time)
                attempt += 1
                wait_time *= 2  
            else:
                
                raise e
    return None