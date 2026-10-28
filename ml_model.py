"""
Machine Learning Model for Algorithm Selection
Trains Random Forest and Decision Tree Classifiers to recommend optimal
algorithms based on problem characteristics (DAA Project - Vishwakarma University).
"""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

MODEL_FILE = os.path.join(os.path.dirname(__file__), "algorithm_recommender.joblib")

SORTING_ALGOS = [
    "Insertion Sort", "Selection Sort", "Bubble Sort", "Merge Sort",
    "Quick Sort", "Heap Sort", "Shell Sort"
]

SEARCHING_ALGOS = [
    "Linear Search", "Binary Search", "Jump Search",
    "Interpolation Search", "Exponential Search"
]

GRAPH_ALGOS = [
    "BFS", "DFS", "Dijkstra", "Bellman-Ford",
    "Floyd-Warshall", "Prim", "Kruskal", "Topological Sort"
]

CATEGORY_ALGOS = {
    "Sorting": SORTING_ALGOS,
    "Searching": SEARCHING_ALGOS,
    "Graph": GRAPH_ALGOS
}

PROBLEM_TYPES = {"Sorting": 0, "Searching": 1, "Graph": 2}
PROBLEM_TYPES_REV = {0: "Sorting", 1: "Searching", 2: "Graph"}

FEATURE_NAMES = [
    "problem_type",          # 0: Sorting, 1: Searching, 2: Graph
    "input_size_log",        # log10(n)
    "is_sorted",             # 1 if sorted, 0 if not
    "memory_constrained",    # 1 if O(1) extra space is required, 0 otherwise
    "uniform_distribution",  # 1 if data is uniformly distributed
    "negative_weights",      # 1 if graph has negative edges
    "need_mst",              # 1 if MST is needed
    "need_shortest_path",    # 1 if shortest path is needed
    "is_dag",                # 1 if graph is a DAG
]

def generate_synthetic_dataset(num_samples=2500, random_state=42):
    """
    Generates algorithmic benchmark dataset for training ML recommendation models.
    Reflects core theoretical optimality criteria from DAA.
    """
    rng = np.random.RandomState(random_state)
    records = []

    for _ in range(num_samples):
        pt_str = rng.choice(["Sorting", "Searching", "Graph"], p=[0.40, 0.35, 0.25])
        pt = PROBLEM_TYPES[pt_str]

        # Log-uniform input size n between 5 and 1,000,000
        n = int(10 ** rng.uniform(0.7, 6.0))
        input_size_log = np.log10(n)

        is_sorted = int(rng.choice([0, 1], p=[0.6, 0.4]))
        memory_constrained = int(rng.choice([0, 1], p=[0.65, 0.35]))
        uniform_distribution = int(rng.choice([0, 1], p=[0.8, 0.2]))
        negative_weights = int(rng.choice([0, 1], p=[0.85, 0.15]))
        need_mst = int(rng.choice([0, 1], p=[0.85, 0.15]))
        need_shortest_path = int(rng.choice([0, 1], p=[0.7, 0.3]))
        is_dag = int(rng.choice([0, 1], p=[0.85, 0.15]))

        # Target classification
        if pt_str == "Sorting":
            if memory_constrained and n > 20:
                target = "Heap Sort"
            elif n <= 20:
                if is_sorted:
                    target = "Insertion Sort"
                else:
                    target = rng.choice(["Insertion Sort", "Selection Sort", "Bubble Sort"], p=[0.75, 0.20, 0.05])
            elif n > 1000:
                if memory_constrained:
                    target = "Heap Sort"
                elif rng.rand() < 0.65:
                    target = "Merge Sort"
                else:
                    target = "Quick Sort"
            else:
                # Moderate size 20 < n <= 1000
                if memory_constrained:
                    target = "Heap Sort"
                else:
                    target = rng.choice(["Quick Sort", "Merge Sort", "Shell Sort"], p=[0.55, 0.30, 0.15])

        elif pt_str == "Searching":
            if not is_sorted:
                target = "Linear Search"
            else:
                if uniform_distribution:
                    target = "Interpolation Search"
                elif n <= 20:
                    target = rng.choice(["Linear Search", "Binary Search"], p=[0.55, 0.45])
                elif n > 1000:
                    target = rng.choice(["Binary Search", "Exponential Search", "Jump Search"], p=[0.65, 0.20, 0.15])
                else:
                    target = rng.choice(["Binary Search", "Jump Search"], p=[0.75, 0.25])

        else: # Graph
            if negative_weights:
                target = rng.choice(["Bellman-Ford", "Floyd-Warshall"], p=[0.75, 0.25])
            elif need_mst:
                target = rng.choice(["Kruskal", "Prim"], p=[0.55, 0.45])
            elif is_dag:
                target = "Topological Sort"
            elif need_shortest_path:
                target = "Dijkstra"
            elif memory_constrained or n > 1000:
                target = "BFS"
            else:
                target = rng.choice(["BFS", "DFS"], p=[0.6, 0.4])

        records.append({
            "problem_type": pt,
            "input_size_log": input_size_log,
            "is_sorted": is_sorted,
            "memory_constrained": memory_constrained,
            "uniform_distribution": uniform_distribution,
            "negative_weights": negative_weights,
            "need_mst": need_mst,
            "need_shortest_path": need_shortest_path,
            "is_dag": is_dag,
            "target": target
        })

    return pd.DataFrame(records)

class AlgorithmRecommenderModel:
    def __init__(self, model_type="random_forest"):
        self.model_type = model_type
        if model_type == "decision_tree":
            self.model = DecisionTreeClassifier(max_depth=8, random_state=42)
        else:
            self.model = RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42)
        self.classes_ = []
        self.accuracy = 0.0
        self.feature_importances_ = None
        self.classification_rep = ""
        self.cm = None

    def train(self, df=None):
        if df is None:
            df = generate_synthetic_dataset()
        X = df[FEATURE_NAMES]
        y = df["target"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        self.model.fit(X_train, y_train)
        self.classes_ = list(self.model.classes_)
        y_pred = self.model.predict(X_test)
        self.accuracy = accuracy_score(y_test, y_pred)
        self.classification_rep = classification_report(y_test, y_pred, zero_division=0)
        self.cm = confusion_matrix(y_test, y_pred, labels=self.classes_)
        self.feature_importances_ = self.model.feature_importances_
        return self.accuracy

    def predict_top_k(self, features_dict, k=3):
        """
        Returns top k recommended algorithms along with normalized confidence percentages.
        Guarantees returned algorithms strictly match the problem_type category.
        """
        pt_name = features_dict.get("problem_type", "Sorting")
        pt_val = PROBLEM_TYPES.get(pt_name, 0)
        n = max(features_dict.get("input_size", 1000), 1)
        input_size_log = np.log10(n)

        row = [
            pt_val,
            input_size_log,
            int(features_dict.get("is_sorted", False)),
            int(features_dict.get("memory_constrained", False)),
            int(features_dict.get("uniform_distribution", False)),
            int(features_dict.get("negative_weights", False)),
            int(features_dict.get("need_mst", False)),
            int(features_dict.get("need_shortest_path", False)),
            int(features_dict.get("is_dag", False)),
        ]

        X_sample = pd.DataFrame([row], columns=FEATURE_NAMES)
        probs = self.model.predict_proba(X_sample)[0]

        valid_algos = CATEGORY_ALGOS.get(pt_name, SORTING_ALGOS)
        scored = []
        for algo_name, prob in zip(self.classes_, probs):
            if algo_name in valid_algos:
                scored.append((algo_name, float(prob)))

        # If model probabilities inside category are tiny, fall back to valid algorithms
        if not scored or sum(p for _, p in scored) == 0:
            scored = [(a, 1.0 / len(valid_algos)) for a in valid_algos]

        # Normalize probabilities over the valid category so they sum to 100%
        total_p = sum(p for _, p in scored)
        norm_scored = [(a, p / total_p) for a, p in scored]
        norm_scored.sort(key=lambda x: x[1], reverse=True)

        return norm_scored[:k]

    def save(self, filepath=MODEL_FILE):
        joblib.dump({
            "model": self.model,
            "model_type": self.model_type,
            "classes": self.classes_,
            "accuracy": self.accuracy,
            "feature_importances": self.feature_importances_,
            "cm": self.cm,
            "classification_rep": self.classification_rep
        }, filepath)

    @classmethod
    def load(cls, filepath=MODEL_FILE):
        if not os.path.exists(filepath):
            return None
        data = joblib.load(filepath)
        instance = cls(model_type=data.get("model_type", "random_forest"))
        instance.model = data["model"]
        instance.classes_ = data["classes"]
        instance.accuracy = data["accuracy"]
        instance.feature_importances_ = data["feature_importances"]
        instance.cm = data.get("cm")
        instance.classification_rep = data.get("classification_rep", "")
        return instance

def get_or_train_model(model_type="random_forest", force_retrain=False):
    """Loads existing trained model or trains a new one."""
    if not force_retrain and os.path.exists(MODEL_FILE):
        model = AlgorithmRecommenderModel.load(MODEL_FILE)
        if model is not None and model.model_type == model_type:
            return model

    model = AlgorithmRecommenderModel(model_type=model_type)
    model.train()
    model.save(MODEL_FILE)
    return model

if __name__ == "__main__":
    print("Training ML Algorithm Recommender Model...")
    m = AlgorithmRecommenderModel()
    acc = m.train()
    print(f"Model Training Accuracy: {acc * 100:.2f}%")
    m.save()
    print("Model saved successfully!")

    # Test Sorting
    test_sort = {
        "problem_type": "Sorting",
        "input_size": 50000,
        "is_sorted": False,
        "memory_constrained": True
    }
    recs = m.predict_top_k(test_sort)
    print("\nTest Prediction for Large Input with Memory Constraint (Sorting):")
    for algo, conf in recs:
        print(f"  - {algo}: {conf*100:.1f}% confidence")

    # Test Searching
    test_search = {
        "problem_type": "Searching",
        "input_size": 10000,
        "is_sorted": True,
        "uniform_distribution": True
    }
    recs = m.predict_top_k(test_search)
    print("\nTest Prediction for Uniformly Distributed Sorted Search:")
    for algo, conf in recs:
        print(f"  - {algo}: {conf*100:.1f}% confidence")

    # Test Graph
    test_graph = {
        "problem_type": "Graph",
        "negative_weights": True
    }
    recs = m.predict_top_k(test_graph)
    print("\nTest Prediction for Negative Weights Graph:")
    for algo, conf in recs:
        print(f"  - {algo}: {conf*100:.1f}% confidence")
