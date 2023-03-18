import streamlit as st
from datetime import datetime
from streamlit.components.v1 import html
import pandas as pd

amount = 0
recipient = "None"
proceed = "None"
st.markdown("""# Transaction Generator""")

html_temp = """
                <div style="background-color:{};padding:1px">

                </div>
                """

with st.sidebar:
    st.markdown("""
    # Welcome to Fraud Detection!
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    # How does it work
    Simply enter some details of a transaction you'd like to make and we'll tell you if you're a criminal or not.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    Made by The Laundromat
    """,
    unsafe_allow_html=True,
    )

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2, col3, col4 = st.columns(4)

with col1:
    expander = st.expander("Transaction Type")
    ex_type = ["Transfer", "Cash Out", "Cash In","Payment","Debit"]
    transaction_type = expander.radio("Please select one", ["None","Transfer", "Cash Out", "Cash In","Payment","Debit"],index=0)

with col2:
    if transaction_type in ex_type:
        amount = st.text_input('Amount', 0)
        print(amount)
        amount = int(amount)
    else:
        st.text("")

# amount_entered = ["None","1000", "2000", "5000","10000"]

with col3:
    if amount > 0:
         recipient = st.expander("Recipient")
         recipient = recipient.radio("Please select one", ["None","John Doe", "Al Capone", "Not a criminal","Mum"])
    else:
        st.text("")

recipient_type = ["John Doe", "Al Capone", "Not a criminal","Mum"]

with col4:
    if recipient in recipient_type:
        proceed = st.expander("How would you like to proceed?")
        proceed = proceed.radio("Please select one", ["None", "Check transaction", "Submit transaction"])
    else:
        st.text("")

proceed_options = ["Check transaction", "Submit transaction"]

if proceed == "Check transaction":
    st.markdown("""# Models""")

    html_temp = """
                    <div style="background-color:{};padding:1px">

                    </div>
                    """


    expander = st.expander("ML Model")
    model = expander.radio("Please select a model", ["Logistic Regression", "Decision Tree", "Random Forest","XGBoost"])


