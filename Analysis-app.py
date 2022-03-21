import streamlit as st
import pickle

st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    font-family:Arial Black;
    
}
</style>
""", unsafe_allow_html=True)


model = pickle.load(open("analyser.pkl","rb"))


def main():
    st.title("Sentiment Analysis Web App")
    st.subheader("Built with Streamlit and Python")
    Enter = st.text_input("Enter Text")
    if st.button("Predict"):
    
        data = Enter
        score = model.polarity_scores(data)
        if score["neg"] != 0:
            st.markdown('<p class="big-font" color:Red>Negative 😡</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="big-font">Positive 😊</p>', unsafe_allow_html=True)
        

if __name__ == '__main__' :
    main()