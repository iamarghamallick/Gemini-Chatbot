import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# get the api key from secrets file
genai.configure(api_key=GOOGLE_API_KEY)

# set model to geminipro
model = genai.GenerativeModel("gemini-pro")

# start chat and store the chat object to a variable
chat = model.start_chat(history=[])


# define function to handle prompts
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


if __name__ == "__main__":
    res = get_gemini_response("Hello")
    print(res)
