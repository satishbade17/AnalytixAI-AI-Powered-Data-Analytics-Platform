import streamlit as st
import joblib
import numpy as np
import pandas as pd

from utils.ml import *

from sklearn.metrics import *

st.title("🤖 Machine Learning Studio")

if "df" not in st.session_state:
    st.warning("Upload dataset first.")
    st.stop()

df = st.session_state["df"]

problem = st.radio(
    "Problem Type",
    [
        "Classification",
        "Regression"
    ]
)

target = st.selectbox(
    "Target Column",
    df.columns
)

X_train, X_test, y_train, y_test = preprocess(df, target)

# ---------------- Models ---------------- #

if problem == "Classification":

    models = {

        "Logistic Regression": LogisticRegression(),

        "Decision Tree": DecisionTreeClassifier(),

        "Random Forest": RandomForestClassifier(),

        "KNN": KNeighborsClassifier(),

        "SVM": SVC(),

        "Naive Bayes": GaussianNB()

    }

else:

    models = {

        "Linear Regression": LinearRegression(),

        "Decision Tree": DecisionTreeRegressor(),

        "Random Forest": RandomForestRegressor(),

        "KNN": KNeighborsRegressor(),

        "SVR": SVR()

    }

model_name = st.selectbox(
    "Choose Model",
    list(models.keys())
)

if st.button("Train Model"):

    model = models[model_name]

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    st.success("Model Trained Successfully!")

    if problem == "Classification":

        st.metric(
            "Accuracy",
            round(
                accuracy_score(y_test, pred),
                3
            )
        )

        st.metric(
            "Precision",
            round(
                precision_score(
                    y_test,
                    pred,
                    average="weighted"
                ),
                3
            )
        )

        st.metric(
            "Recall",
            round(
                recall_score(
                    y_test,
                    pred,
                    average="weighted"
                ),
                3
            )
        )

        st.metric(
            "F1 Score",
            round(
                f1_score(
                    y_test,
                    pred,
                    average="weighted"
                ),
                3
            )
        )

        st.write("Confusion Matrix")

        st.write(confusion_matrix(
            y_test,
            pred
        ))

    else:

        st.metric(
            "R² Score",
            round(
                r2_score(
                    y_test,
                    pred
                ),
                3
            )
        )

        st.metric(
            "MAE",
            round(
                mean_absolute_error(
                    y_test,
                    pred
                ),
                3
            )
        )

        mse = mean_squared_error(
            y_test,
            pred
        )

        st.metric("MSE", round(mse,3))

        st.metric(
            "RMSE",
            round(np.sqrt(mse),3)
        )

    save_model(
        model,
        "models/model.pkl"
    )

    with open(
        "models/model.pkl",
        "rb"
    ) as f:

        st.download_button(
            "⬇ Download Model",
            f,
            "model.pkl"
        )