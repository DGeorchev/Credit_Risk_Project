import streamlit as st
import pandas as pd
import joblib


model = joblib.load("credit_model.pkl")
le = joblib.load("label_encoder.pkl")

st.title("Класификатор за одобрение на кредити")
st.write("Въведете информация за кандидата, за да предвидите кредитния риск.")


age = st.number_input("Age", min_value=18, max_value=80, value=30)
sex = st.selectbox("Sex", ["male", "female"])
job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing", ["own", "free", "rent"])
saving_accounts = st.selectbox("Saving Accounts", ["little", "moderate", "quite rich", "rich", "Unknown"])
checking_account = st.selectbox("Checking Account", ["little", "moderate", "rich", "Unknown"])
credit_amount = st.number_input("Credit Amount", min_value=0, value=100)
duration = st.number_input("Duration (months)", min_value=1, value=12)
purpose = st.selectbox("Purpose",
                       ["car", "furniture/equipment", "radio/TV", "domestic appliances", "repairs", "education",
                        "business", "vacation/others"])


input_df = pd.DataFrame({
    "Age": [age],

    "Sex": [0 if sex == "male" else 1],

    "Job": [job],

    "Housing": [0 if housing == "own" else 1 if housing == "free" else 2],

    "Saving accounts": [saving_accounts],
    "Checking account": [checking_account],
    "Credit amount": [credit_amount],
    "Duration": [duration],
    "Purpose": [purpose]
})
for col in ['Saving accounts', 'Checking account', 'Purpose']:

    encoder = le[col]
    input_df[col] = encoder.transform(input_df[col].astype(str))

if st.button("Извод"):
    prediction = model.predict(input_df)

    if prediction[0] == 0:
        st.success(f"✅ Добър!")
    else:
        st.error(f"🛑 Лош!")