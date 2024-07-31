import streamlit as st
import requests

# Custom CSS for additional styling with background image
page_bg_image="""
<style>
[data-testid="stApp"]{
  background-image: url(' https://www.thepcdoctor.com.au/wp-content/uploads/2020/12/Sci-Fi-Movies.jpg');
  background-size: cover;
   
}

.main {
        background-color: rgba(0, 0, 0, 0.7); /* White background with some transparency */
    }
 .chatbot-response {
        background-color: #508C9B;
        border-radius: 10px;
        padding: 10px;
        margin-top: 10px;
        font-size: 16px;
    }

    .error-message {
        background-color: #B43F3F;
        border-radius: 10px;
        padding: 10px;
        margin-top: 10px;
        font-size: 16px;
    }

     .title {
        color: #FFFFFF;
        font-family: '28 Days Later' ;
        text-align: center;
    }




</style>
"""

st.markdown(
   page_bg_image,
    unsafe_allow_html=True
)
 
def main():
    st.markdown("<h1 class='title'>Film Genre Chatbot</h1>", unsafe_allow_html=True)
    user_input = st.text_input("Enter your message:")
    if st.button("Send"):
        if user_input:
            # Send the user input to the Flask server
            response = requests.post('http://localhost:5000/filmgenra', json={"message": user_input})
            
            if response.status_code == 200:
                result = response.json()
                st.markdown(f"<div class='chatbot-response'><strong>chatbot:</strong> {result['response']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='error-message'><strong>Error:</strong> {response.json().get('error', 'Unknown error')}</div>", unsafe_allow_html=True)
        else:
            st.write("Please enter a message.")

if __name__ == "__main__":
    main()