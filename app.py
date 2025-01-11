from dotenv import load_dotenv
load_dotenv() # load all enviornment variables
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")

def get_gemini_reponse(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q/A Model")
st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Enter")

if submit:
    response=get_gemini_reponse(input)
    st.subheader("AI:\n")
    st.write(response)