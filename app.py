import streamlit as st
from datetime import datetime
from streamlit.components.v1 import html
import pandas as pd
import pickle


amount = 0
recipient = "None"
proceed = "None"

# st.markdown(" :violet[# Transaction Generator], and this is **:blue[colored]** and bold.")

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

col1, col2, col3 = st.columns(3)

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
         recipient = recipient.radio("Please select one", ["None","That bank that just acquired SVB UK for £1", "Al Capone", "Pablo Escobar","Mum"])
    else:
        st.text("")

recipient_type = ["That bank that just acquired SVB UK for £1", "Al Capone", "Pablo Escobar","Mum"]

if recipient in recipient_type:
    proceed = st.expander("How would you like to proceed?")
    proceed = proceed.radio("Please select one", ["None", "Check transaction", "Submit transaction"])
else:
    st.text("")

proceed_options = ["Check transaction", "Submit transaction"]


if transaction_type == "Transfer":
    type_transfer = 1
else:
    type_transfer = 0
if transaction_type == "Cash In":
    type_cashin = 1
else:
    type_cashin = 0
if transaction_type == "Cash Out":
    type_cashout = 1
else:
    type_cashout = 0
if transaction_type == "Payment":
    type_payment = 1
else:
    type_payment = 0
if transaction_type == "Debit":
    type_debit = 1
else:
    type_debit = 0



if recipient == 'Mum':
    recipient_encoded = 1733924
else:
    recipient_encoded = 0
if recipient == 'That bank that just acquired SVB UK for £1':
    recipient_encoded = 439685
else:
    recipient_encoded = 0
if recipient == 'Al Capone':
    recipient_encoded = 1662094
else:
    recipient_encoded = 0
if recipient == 'Pablo Escobar':
    recipient_encoded = 828919
else:
    recipient_encoded = 0


X = pd.DataFrame({'step': 159,
                  'amount': amount,
                  'nameOrig':2188998,
                  'oldBalanceOrig': 170136.0,
                  'newBalanceOrig': 160296.36,
                  'nameDest': recipient_encoded,
                  'oldBalanceDest':0.0,
                  'newBalanceDest': 0.0,
                  'errorBalanceOrig': 0,
                  'errorBalanceDest': 9839.64,
                  'type_CASH_IN': type_cashin,
                  'type_CASH_OUT': type_cashout,
                  'type_DEBIT': type_debit,
                  'type_PAYMENT': type_payment,
                  'type_TRANSFER': type_transfer}, index=[0])
if proceed == "Check transaction":
    st.markdown("""# Models""")

    html_temp = """
                    <div style="background-color:{};padding:1px">

                    </div>
                    """


    expander = st.expander("ML Model")
    modelname = expander.radio("Please select a model", ["Basic model (Logistic Regression)", "Decision Tree", "Random Forest","XGBoost"])

    if modelname == "Basic model (Logistic Regression)":
        model = pickle.load(open("/Users/leahredon/code/AlcaRmsp/User_Interface/Models/LogisticRegression.pickle","rb"))
    if modelname == "Decision Tree":
        model = pickle.load(open("/Users/leahredon/code/AlcaRmsp/User_Interface/Models/DecisionTreeClassifier.pickle","rb"))
    if modelname == "Random Forest":
        model = pickle.load(open("/Users/leahredon/code/AlcaRmsp/User_Interface/Models/RandomForestClassifier.pickle","rb"))
    if modelname == "XGBoost":
        model = pickle.load(open("/Users/leahredon/code/AlcaRmsp/User_Interface/Models/XGBClassifier.pickle","rb"))

    if st.button('Calculate'):
        if model.predict(X) == 1:
            st.image("/Users/leahredon/code/AlcaRmsp/User_Interface/thats-fraud-and-youre-a-criminal-david.gif")
        else:
            st.image("/Users/leahredon/code/AlcaRmsp/User_Interface/mother_teresa.jpeg")
