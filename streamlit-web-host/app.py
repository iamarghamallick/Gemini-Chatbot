import streamlit as st
import google.generativeai as genai

# get the api key from secrets file
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# set model to geminipro
model = genai.GenerativeModel("gemini-pro")

# start chat and store the chat object to a variable
chat = model.start_chat(history=[])


# define function to handle prompts
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


# set the config
st.set_page_config(
    page_title="Gemini Chat-Bot",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

# set the title
st.title("Gemini Chat-Bot")

# initialize history list
if "messages" not in st.session_state:
    st.session_state.messages = []

# populates previous chat
for message in st.session_state.messages:
    # display previous messageds
    with st.chat_message(message["role"]):  # create a chat element
        st.markdown(message["content"])  # add content to element

# initialize prompt variable to get the input text
prompt = st.chat_input("Message Gemini-ChatBot")

if prompt:
    # create chat element for user
    with st.chat_message("user"):
        st.markdown(prompt)  # add content to the element
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )  # add prompt to the history

    # evaluate the prompt
    response = get_gemini_response(prompt)

    # create chat element for the assistant
    with st.chat_message("assistant"):
        # Create a empty placeholder element
        placeholder = st.empty()

        # traverse through the response object
        for a in response:
            # add data element to the placeholder element
            placeholder.markdown(a.text)

    # add the final result to the placeholder element
    placeholder.markdown(response.text)

    # add the result to the history
    st.session_state.messages.append({"role": "assistant", "content": response.text})
