import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import plotly.express as px

# Loading the datas

X_train_0 = pd.read_csv("C:/Users/danie/Documents/Open Classrooms/P7/X_train.csv")
X_test_0 = pd.read_csv("C:/Users/danie/Documents/Open Classrooms/P7/X_test.csv")
y_train_0 = pd.read_csv("C:/Users/danie/Documents/Open Classrooms/P7/y_train.csv")
y_test_0 = pd.read_csv("C:/Users/danie/Documents/Open Classrooms/P7/y_test.csv")

X_train = X_train_0.to_numpy()
X_test = X_test_0.to_numpy()
y_train = np.array(y_train_0["TARGET"].to_list())
y_test = np.array(y_test_0["TARGET"].to_list())

# End of loading

st.title('Welcome to the credit answer dashboard !')

st.write('## This application predict if the client will refund or not his loan')

cus = int(len(X_test))
st.write(cus)

st.sidebar.write('The number of available client is ', cus)
customer_number = st.sidebar.number_input('Please select the customer number', min_value=0, max_value=cus, value=int(cus/2), step=1)

threshold = st.sidebar.slider("Choose a threshold", min_value=0.0, max_value = 1.0, value=0.5, step = 0.01)

if customer_number != "" :
    st.markdown(
    f"""
    * Client number : {customer_number}
    """
)

RFinal = DecisionTreeClassifier(
    random_state=1, min_samples_split=2, max_features="sqrt"
)

RFinal.fit(X_train, y_train)

yhat = RFinal.predict_proba([list(X_test_0.iloc[customer_number])])
result = yhat[0][1]
# summarize

categories = list(X_train_0)

st.subheader("Feature importance")

select_element = st.selectbox('Pick a category', categories)

st.subheader("Description of the category")
fig = px.scatter(X_test_0, x=select_element)
st.write(fig)