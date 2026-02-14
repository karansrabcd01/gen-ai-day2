from google import genai
from dotenv import load_dotenv
import streamlit as st
import os

from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize the LangChain Google Genai model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv('GOOGLE_API_KEY')
)

# Streamlit UI
st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Select...",
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

template = load_prompt("template.json")

if st.button("Summarize"):
    if paper_input != "Select...":
        try:
            with st.spinner('Generating summary...'):
                # Fill the placeholders
                prompt = template.invoke({
                    "paper_input": paper_input,
                    "style_input": style_input,
                    "length_input": length_input
                })
                
                # Invoke the model
                response = llm.invoke(prompt)
                
                # Display the result
                st.success("Summary Generated!")
                st.write(response.content)
                
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please select a research paper first!")