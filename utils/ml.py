import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC, SVR
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB


def preprocess(df, target):

    df = df.copy()

    encoder = LabelEncoder()

    for col in df.select_dtypes(include="object").columns:
        df[col] = encoder.fit_transform(df[col].astype(str))

    X = df.drop(columns=[target])
    y = df[target]

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


def save_model(model, filename):
    joblib.dump(model, filename)