# LCEL composes Runnables with a pipe: prompt -> model -> parser.
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
 
prompt = ChatPromptTemplate.from_template("Summarize in one sentence: {text}")
chain = prompt | model | StrOutputParser()     # a composed Runnable
summary = chain.invoke({"text": some_long_text})   # or .stream(...) / await .ainvoke(...)
