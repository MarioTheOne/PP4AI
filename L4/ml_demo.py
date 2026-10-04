import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree


def main():
    iris = load_iris(as_frame=True)
    flower_data = iris.frame.copy()
    flower_data["species"] = flower_data["target"].map(
        {0: "setosa", 1: "versicolor", 2: "virginica"}
    )
    flower_data = flower_data.drop(columns=["target"])

    print("First five flowers:")
    print(flower_data.head())
    print("\nNumber of flowers:", len(flower_data))
    print("Missing values by column:")
    print(flower_data.isna().sum())
    print("\nFlowers per species:")
    print(flower_data["species"].value_counts())

    X = flower_data.drop(columns=["species"])
    y = flower_data["species"]
    print("\nInput columns:", list(X.columns))
    print("Target column:", y.name)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )
    print("\nTraining flowers:", len(X_train))
    print("Test flowers:", len(X_test))

    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X_train, y_train)
    print("The model has been trained.")
    print("Species order in tree:", list(model.classes_))

    fig, ax = plt.subplots(figsize=(14, 7))
    plot_tree(
        model,
        feature_names=list(X.columns),
        class_names=list(model.classes_),
        filled=True,
        rounded=True,
        impurity=False,
        fontsize=10,
        ax=ax,
    )
    ax.set_title("Decision tree learned from the training flowers")
    fig.tight_layout()
    plt.show()

    predictions = model.predict(X_test)
    results = X_test.copy()
    results["actual_species"] = y_test
    results["predicted_species"] = predictions
    results["correct"] = results["actual_species"] == results["predicted_species"]

    print("\nTest results:")
    print(results.head(10))
    test_accuracy = accuracy_score(y_test, predictions)
    number_correct = int(results["correct"].sum())
    print(f"\nCorrect predictions: {number_correct} out of {len(y_test)}")
    print(f"Test accuracy: {test_accuracy:.1%}")
    print("\nMisclassified flowers:")
    print(results.loc[~results["correct"]])
    print("Number of mistakes:", int((~results["correct"]).sum()))

    baseline = DummyClassifier(strategy="most_frequent")
    baseline.fit(X_train, y_train)
    baseline_predictions = baseline.predict(X_test)
    baseline_accuracy = accuracy_score(y_test, baseline_predictions)
    print(f"\nBaseline test accuracy: {baseline_accuracy:.1%}")
    print(f"Decision tree test accuracy: {test_accuracy:.1%}")

    new_flowers = pd.DataFrame(
        {
            "sepal length (cm)": [5.1, 6.0, 6.7],
            "sepal width (cm)": [3.5, 2.9, 3.0],
            "petal length (cm)": [1.4, 4.5, 5.5],
            "petal width (cm)": [0.2, 1.5, 2.1],
        }
    )
    new_results = new_flowers.copy()
    new_results["predicted_species"] = model.predict(new_flowers)
    print("\nPredictions for new flowers:")
    print(new_results)

    one_flower = pd.DataFrame(
        {
            "sepal length (cm)": [5.8],
            "sepal width (cm)": [2.7],
            "petal length (cm)": [4.1],
            "petal width (cm)": [1.0],
        }
    )
    print("\nPrediction for one additional flower:", model.predict(one_flower)[0])


if __name__ == "__main__":
    main()