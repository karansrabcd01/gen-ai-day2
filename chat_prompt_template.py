from langchain_core.prompts import ChatPromptTemplate

chat_template= ChatPromptTemplate([
     ("system", "You are a helpful {domain} Expert."),
     ("human", "Explain in the simple terms, What is {topic}?")

])

prompt=chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)
