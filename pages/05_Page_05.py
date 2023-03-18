import streamlit as st
import pickle

# Set page config
st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:", layout="wide", initial_sidebar_state="collapsed", background_color="#e6f7ff")

# Add content to your Streamlit app
st.write("Hello, World!")

# # Export Pipeline as pickle file
# with open("pipeline.pkl", "wb") as file:
#     pickle.dump(pipeline_tuned, file)

# # Load Pipeline from pickle file
# my_pipeline = pickle.load(open("pipeline.pkl","rb"))

# my_pipeline.score(X_test, y_test)
