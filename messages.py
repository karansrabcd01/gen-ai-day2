from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# Use the full model name with version
model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.9)

# chat_history=[

#     SystemMessage(content="You are a helpful assistant that provides concise and accurate answers to user queries.")
# ]

messages =[
    SystemMessage(content="you are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain?")

]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print("Chat history:", messages)

# while True:
#     user_input=input("You: ")
#     chat_history.append(HumanMessage(content=user_input))
#     if user_input=='exit':
#         print("Exiting the chatbot. Goodbye!")
#         break
#     response = model.invoke(chat_history)
#     chat_history.append(AIMessage(content=response.content))
#     print("Chatbot:", response.content)

# print("Chat history:", chat_history)
# result = model.invoke("What is the capital of India?")
# print(result.content)