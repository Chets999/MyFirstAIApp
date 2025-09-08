#install langchain required libraries 

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate 
from langchain import LLMChain
#API Key 

import os 

os.environ['GOOGLE_API_KEY'] ="AIzaSyD91RmsgcvRu56slhMB3aOwxrsAfj7jJIc"

# Using Google Models (Gemini Pro)



# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")


#Create PromptTemplate to generalize 



tweet_template = "Give me {number} tweets on {topic} in Kannada"

tweet_prompt = PromptTemplate(template=tweet_template, input_variables=['number','topic']) 


#CReate LLM CHain 


tweet_chain = tweet_prompt | gemini_model 


import streamlit as st

st.header("Tweet Generator by Chetan ") 

st.subheader("Generate Tweets using Generative AI") 

topic=st.text_input("Topic")

number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1) 


if st.button("Generate"):
    tweets = tweet_chain.invoke({"number" : number, "topic" : topic})
    st.write(tweets.content)




