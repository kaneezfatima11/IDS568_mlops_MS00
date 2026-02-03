from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train_and_save_model():
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    joblib.dump(model, "model.pkl")
    print("Saved model.pkl in the project root")

if __name__ == "__main__":
    train_and_save_model()
