Credit_Risk_Project

Класификатор за одобрение на кредити (Credit Risk Classifier)

Курсов проект по Системи, основани на знания.
Студент: Димитър Георчев.
Университет: Софийски университет „Св. Климент Охридски“, ФМИ.

📌 Формулировка на задачата

Целта на проекта е разработването на интелигентна система за класификация на кредитополучатели в две категории: „нисък риск“ (Good) и „висок риск“ (Bad). Задачата е решена чрез машинно обучение върху набора от данни German Credit Dataset.

📊 Данни и алгоритми

Използван е наборът от данни "German Credit Data" от Kaggle, включващ 1000 записа със следните атрибути:

Числови: Age, Credit amount, Duration.

Категориални: Sex, Job, Housing, Saving accounts, Checking account, Purpose.

Целева променлива: Risk (Good/Bad).

Сравнителен анализ на моделите

Проведено е изследване на четири метода чрез 10-слойна крос-валидация:

Logistic Regression: Най-висока сигурност при рискови клиенти.

Decision Tree: Висока интерпретируемост, но по-ниски резултати.

Random Forest: Стабилен баланс.

XGBoost: Избран за финална реализация поради най-висока цялостна прецизност и общ баланс.

🛠 Програмна реализация

Системата е изградена на Python (3.9+) на модулен принцип:

analysis_model.ipynb / main.py: Подготовка на данни, сравнителен анализ и генериране на модела.

app.py: Уеб интерфейс чрез Streamlit за класификация в реално време.

credit_model.pkl: Сериализиран XGBoost модел.

label_encoder.pkl: Правила за преобразуване на текстови данни.

🚀 Инсталация и стартиране

1. Инсталиране на библиотеки:

pip install streamlit pandas joblib xgboost scikit-learn


2. Стартиране на приложението:

streamlit run app.py


📖 Литература

Kabure (2019). German Credit Data with Risk (Kaggle).

Streamlit Documentation (2026).

Brownlee, J. (2021). Develop a Model for the Imbalanced Classification.

Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System.
