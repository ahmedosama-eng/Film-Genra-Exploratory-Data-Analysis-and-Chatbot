from conversation import q_chat_with_create_embedings,q_chat_with_retrive_embedings
from helper import check_file_exists
from flask import Flask, request

app = Flask(__name__)

q_chat=None

def intilalize_the_caht():
    global q_chat
    data_path ="F:/studying machine/Film Genra ChatBot/data/Film Genre Stats.csv"
    vdb_path ="vectorstore2/db_faiss22"
    cheak_path="F:/studying machine/Film Genra ChatBot/vectorstore2/db_faiss22/index.faiss"
    if check_file_exists(cheak_path)==True:
        q_chat= q_chat_with_retrive_embedings(vdb_path)
    else:
        q_chat=q_chat_with_create_embedings(data_path,vdb_path)



@app.route('/filmgenra', methods=['POST'])
def filmgenra_chat():
   try: 
        request_data = request.get_json()
        user_query = request_data.get("message")
        response = q_chat(user_query)
        return {"response": response['answer']}
   except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    intilalize_the_caht()
    app.run(host='0.0.0.0', port=5000)



