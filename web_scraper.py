#This code is written by Allen Wong [allenwsh@gmail.com]
import logging
import sys

import base64
import gc
import random
import tempfile
import time
import uuid

from llama_index.core import Settings
from IPython.display import Markdown, display
from llama_index.llms.vllm import Vllm

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader
from IPython.display import Markdown, display
import os
from llama_index.llms.ollama import Ollama
from llama_index.llms.ipex_llm import IpexLLM

from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core import PromptTemplate
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, ServiceContext, SimpleDirectoryReader


import streamlit as st
import warnings
import time

# Insert Intel Logo
#st.logo ("/home/smgailab/data1/AI_Allen/image/Intel_logo.png", link=None, icon_image=None)

# Insert Intel AI Everywhere 
#st.image ("/home/smgailab/data1/AI_Allen/image/xeon.png", caption="Intel AI Everywhere!")
   

warnings.filterwarnings(
    "ignore", category=UserWarning, message=".*padding_mask.*"
)

# Reset the Chatbot
def reset_chat():
    st.session_state.messages = []
    st.session_state.context = None
    gc.collect()

    
# Get the URL linke from User

with st.sidebar:
    st.header(f"Please insert your URL here!")
    url = st.text_input("Insert your URL here: ", placeholder="Input your URL here....", key="text")
    def on_click():
        st.session_state["text "] = ""
    st.button("Reset", on_click=on_click)
    if url:
        st.write("The URL entered: ", url)
    
    else:
        st.error('Could not find the URL, please re-enter again.....')
        st.stop()
        
url_link=url

# setup llm & embedding model

Settings.llm=Ollama(model="llama3.1", request_timeout=120.0)
Settings.embed_model = HuggingFaceEmbedding( model_name="BAAI/bge-large-en-v1.5", trust_remote_code=True)
system_prompt="Given the context information above I want you to think step by step to answer the query in a crisp manner, incase case you don't know the answer say 'I don't know!'.\n"

#If you want to use vllm, just uncomment the code below
#Settings.llm=llm
    #llm=Vllm(model="/home/smgailab/data1/AI_Allen/model/Meta-Llama-3-8B-Instruct")
    #llm = IpexLLM.from_model_id(
    #                        model_name="/home/smgailab/data1/AI_Allen/model/Meta-Llama-3-8B-Instruct",
    #                        tokenizer_name="/home/smgailab/data1/AI_Allen/model/Meta-Llama-3-8B-Instruct",
    #                        context_window=2048,
    #                        max_new_tokens=512,
    #                        )


#chat_engine = index.as_chat_engine(chat_mode="condense_question", streaming=True)
    
    
@st.cache_resource(show_spinner=True)
def load_data():
    with st.spinner(text="Loading and indexing the URL... Hang On........for few seconds....."):
        reader = SimpleWebPageReader(html_to_text=True)
        documents = reader.load_data(urls=[url_link])
            #documents = reader.load_data(["https://finance.yahoo.com/news/intel-sells-arm-shares-likely-104454742.html"])
        index = VectorStoreIndex.from_documents(documents, show_progress=True)
            #index = SummaryIndex.from_documents(documents)
            #documents[0]
            #index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index
        
# Setting Up Chat Engine       
index = load_data()
    
# define query_engine function
query_engine = index.as_query_engine(streaming=True)

# inform the user that the AI ChatBot is ready to use
st.success("Your AI ChatBot Is Ready to Chat!")

col1, col2 = st.columns([6, 1])

with col1:
    st.header(f"AI ChatBot with the Web Scraping Capability Powered by Intel 4th Gen 8480+!")

with col2:
    st.button("Clear ↺", on_click=reset_chat)

# Initialize chat history
if "messages" not in st.session_state:
    reset_chat()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])    
    
    
if "message" not in st.session_state.keys():
    reset_chat()
        
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        

if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulate stream of response with milliseconds delay
        streaming_response = query_engine.query(prompt)
        
        for chunk in streaming_response.response_gen:
            full_response += chunk
            message_placeholder.markdown(full_response + "▌")

        # full_response = query_engine.query(prompt)

        message_placeholder.markdown(full_response)
        # st.session_state.context = ctx

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
