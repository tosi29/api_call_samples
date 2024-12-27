import google.generativeai as genai
import os

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)

def generate_text(prompt):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    prompt = "日本の山を高い順に5つ挙げてください。"
    generated_text = generate_text(prompt)
    print("生成されたテキスト:")
    print(generated_text)
