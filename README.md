# Credit Risk Project: Класификатор за одобрение на кредити

**Курсов проект по Системи, основани на знания**
* **Студент:** Димитър Георчев
* **Университет:** Софийски университет „Св. Климент Охридски“, ФМИ

---

## Формулировка на задачата
Целта на проекта е разработването на интелигентна система за класификация на кредитополучатели в две категории: „нисък риск“ (Good) и „висок риск“ (Bad). Задачата е решена чрез машинно обучение върху набора от данни German Credit Dataset.

## Данни
Използван е наборът от данни "German Credit Data" от Kaggle, включващ 1000 записа със следните атрибути:
* **Числови:** Age, Credit amount, Duration.
* **Категориални:** Sex, Job, Housing, Saving accounts, Checking account, Purpose.
* **Целева променлива:** Risk (Good/Bad).

## Сравнителен анализ на моделите
Проведено е изследване на четири метода чрез 10-слойна крос-валидация:
* **Logistic Regression:** Най-висока сигурност при рискови клиенти.
* **Decision Tree:** Висока интерпретируемост, но по-ниски резултати.
* **Random Forest:** Стабилен баланс.
* **XGBoost:** Избран за финална реализация поради най-висока цялостна прецизност и общ баланс.

## Програмна реализация и структура
Системата е изградена на Python (3.9+) на модулен принцип:

* **`training/analysis_model.ipynb`**: Подготовка на данни, сравнителен анализ и трениране на модела.
* **`models/credit_model.pkl`**: Сериализиран XGBoost модел.
* **`models/label_encoder.pkl`**: Правила за преобразуване на текстови данни.
* **`data/german_credit_data.csv`**: Използваният набор от данни.
* **`app.py`**: Уеб интерфейс чрез Streamlit за класификация в реално време.

## Инсталация и стартиране

1. **Инсталиране на необходимите библиотеки:**

```bash
pip install streamlit pandas joblib xgboost scikit-learn
```

2. **Стартиране на приложението:**

```bash
streamlit run app.py
```

## Литература
* Kabure (2019). German Credit Data with Risk (Kaggle).
* Streamlit Documentation (2026).
* Brownlee, J. (2021). Develop a Model for the Imbalanced Classification.
* Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System.
