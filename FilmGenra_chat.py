from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
#from langchain.embeddings.openai import OpenAIEmbeddings
#from langchain_community.embeddings import OpenAIEmbeddings
#from langchain.chat_models import s
#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

import sys
import os
import openai

import faiss
import pickle


sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']


def doc_loader(filepath):
    print("\n\n  here in doc_loader \n\n")        
    loader = CSVLoader(file_path=filepath, encoding="utf-8", csv_args={'delimiter': ','})
    data = loader.load()
    return data

def text_spliter(data):
    print("\n\n  here in text_spliter \n\n")            
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(data)
    for i in text_chunks:
        print("\n\n\n")
        print(i)
        print("\n\n\n")
    print(type(text_chunks))
    return text_chunks
 
def create_Embeddings_and_vectordb(text_chunks,DB_FAISS_PATH):
    print("\n\n  here in create_Embeddings_and_vectordb \n\n")     
    embedding = OpenAIEmbeddings()
    docsearch = FAISS.from_documents(text_chunks, embedding)
    docsearch.save_local(DB_FAISS_PATH)
    return docsearch


def retrive_vectordb(vdb_path):
    print("\n\n  here in retrive_vectordb \n\n") 
    docsearch = FAISS.load_local(vdb_path,embeddings=OpenAIEmbeddings(),allow_dangerous_deserialization=True)
    return docsearch
 

  

def chatbot_model(docsearch):
    print("\n\n  here in chatbot_model \n\n") 
    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)
    chat_memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    qa = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=docsearch.as_retriever(),
        memory=chat_memory
    )
    return qa







#problems
# memory 
#cahnking
