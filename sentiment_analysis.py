import streamlit as st
from textblob import TextBlob

# Streamlit application
def main():
    st.title("Sentiment Analysis App")

    st.write("Enter text below and get the sentiment analysis:")

    # User input
    user_input = st.text_area("Input Text", "Type here...")

    # Analyze sentiment when the button is clicked
    if st.button("Analyze Sentiment"):
        if user_input:
            analysis = TextBlob(user_input)
            sentiment = analysis.sentiment.polarity

            if sentiment > 0:
                st.success("The sentiment is **Positive**.")
            elif sentiment < 0:
                st.error("The sentiment is **Negative**.")
            else:
                st.warning("The sentiment is **Neutral**.")
        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    main()
