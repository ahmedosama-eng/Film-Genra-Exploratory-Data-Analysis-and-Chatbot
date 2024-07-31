from FilmGenra_chat import chatbot_model,doc_loader,create_Embeddings_and_vectordb,text_spliter,retrive_vectordb


def q_chat_with_create_embedings(data_path,vdb_path):
    print("\n\n  here in q_chat_with_create_embedings \n\n") 
    q_chat=chatbot_model(create_Embeddings_and_vectordb(text_spliter(doc_loader(data_path)),vdb_path))
    return q_chat


def q_chat_with_retrive_embedings(vdb_path):
    print("\n\n  here in q_chat_with_retrive_embedings \n\n") 
    q_chat=chatbot_model(retrive_vectordb(vdb_path))
    return q_chat


