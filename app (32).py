import streamlit as st
from textblob import TextBlob
import random
import webbrowser

# Define response map
mental_health_responses = {
    "greeting": ["Hello, I'm here to support you. How are you feeling today?",
                 "Hi there! I'm always ready to talk. How's your day going?"],
    "sad": ["I'm sorry you're feeling this way. Remember, it's okay to feel sad sometimes.",
            "You’re not alone. Want to talk about what’s bothering you?"],
    "anxious": ["Take a deep breath. You're safe here.",
                "It’s okay to feel anxious. I'm here for you."],
    "happy": ["That’s great to hear! Want to share what made you happy?",
              "Awesome! I'm glad you're feeling good!"],
    "default": ["Can you tell me more about how you're feeling?",
                "I'm here to listen. Would you like to talk about it?"]
}

def classify_intent(message):
    blob = TextBlob(message.lower())
    sentiment = blob.sentiment.polarity

    if "hi" in message or "hello" in message:
        return "greeting"
    elif sentiment < -0.2:
        return "sad"
    elif sentiment < 0.1:
        return "anxious"
    elif sentiment > 0.3:
        return "happy"
    else:
        return "default"

def get_response(user_input):
    intent = classify_intent(user_input)
    return random.choice(mental_health_responses[intent])

def get_sentiment_score(text):
    return TextBlob(text).sentiment.polarity

# Streamlit App
st.set_page_config(page_title="Mental Health Chatbot", layout="centered")
st.title("🧠 Mental Health Chatbot")
st.markdown("Welcome! I'm here to support your emotional well-being. ❤️")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("How are you feeling today?", key="user_input")

if st.button("Send"):
    if user_input:
        response = get_response(user_input)
        score = get_sentiment_score(user_input)

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))
        st.session_state.chat_history.append(("Sentiment", f"{score:.2f}"))

# Display chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")

# Mental health resources
st.markdown("---")
st.markdown("### 💡 Helpful Resources:")
st.markdown("- [7 Cups](https://www.7cups.com/)")
st.markdown("- [iCall India](https://icallhelpline.org/)")
st.markdown("- [Therapy Route](https://www.therapyroute.com/)")

# Emergency contact
if st.button("🚨 Panic / Help"):
    webbrowser.open("https://www.icallhelpline.org/contact/")
