# Intelligent Problem Solver (Python & Machine Learning Edition)

### Department of Artificial Intelligence — Vishwakarma University, Pune
**Subject:** Design and Analysis of Algorithms (DAA)

---

## 🌟 Overview & What Changed from JavaScript to Python

In this version, the previous JavaScript rule-based system has been transformed into a full **Python & Machine Learning application**:

1. **Machine Learning Model Integration**:
   - Replaced static if-else decision rules with trained **Random Forest** and **Decision Tree** classifiers (using `scikit-learn`).
   - Predicts optimal algorithms based on problem features: input size $n$, degree of sortedness, memory constraints ($O(1)$ space), data distribution, negative graph weights, shortest path requirements, and MST constraints.
   - Computes **ML Confidence Scores (%)** for recommendations.
   - Provides **Feature Importance** analytics explaining which problem constraints dictated the algorithm choice.
   - Supports live model switching and retraining directly from the user interface.

2. **100% Python Interactive Web Application (Streamlit)**:
   - Converted all simulator logic and visualizations into Python using **Streamlit**, **Plotly**, and **NetworkX**.
   - No Node.js / JavaScript runtime required.

3. **Interactive Step-by-Step Simulators**:
   - **Sorting Simulator**: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort with customizable array inputs, step sliders, and active element highlighting.
   - **Searching Simulator**: Linear Search and Binary Search with range halving and found/not-found status.
   - **Graph Simulator**: BFS, DFS, Dijkstra, Bellman-Ford, Prim, and Kruskal visualized on an interactive circular network graph with node states, relaxed distances, and MST edge selections.
   - **Recurrence Tree Simulator**: Expand $T(n) = aT(n/b) + f(n)$ into hierarchical tree levels showing recursive subproblem size and work accumulation.

4. **Model Analytics & Explainability**:
   - Evaluation metrics: Accuracy, Classification Report, Confusion Matrix heatmap, and Feature Importance bar charts.

5. **Learn Complexity**:
   - Interactive Big-O growth curves comparing $O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$ alongside complexity reference tables.

---

## 🚀 How to Run

### Option 1: Quick Launch (Windows)
Double-click [`run_app.bat`](file:///c:/Users/Vedant/Downloads/intelligent-problem-solver-v3.2-array-input/run_app.bat).

### Option 2: Command Line (PowerShell / Command Prompt)
Open your terminal in this directory and run:

```bash
python -m streamlit run app.py
```

> **Note for Windows:** Use `python -m streamlit run app.py` (with the `python -m` prefix) to prevent the `'streamlit' is not recognized` PATH error in PowerShell.

The application will open automatically in your browser at:
👉 **`http://localhost:8501`**

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| [`app.py`](file:///c:/Users/Vedant/Downloads/intelligent-problem-solver-v3.2-array-input/app.py) | Main Streamlit web application with tabs for Advisor, Simulator, Analytics, and Complexity guide. |
| [`ml_model.py`](file:///c:/Users/Vedant/Downloads/intelligent-problem-solver-v3.2-array-input/ml_model.py) | Scikit-learn Random Forest & Decision Tree models, synthetic benchmark dataset generator, training, and inference. |
| [`algorithms.py`](file:///c:/Users/Vedant/Downloads/intelligent-problem-solver-v3.2-array-input/algorithms.py) | Algorithmic complexity metadata and step-by-step state generators for Sorting, Searching, and Graph algorithms. |
| [`recurrence_solver.py`](file:///c:/Users/Vedant/Downloads/intelligent-problem-solver-v3.2-array-input/recurrence_solver.py) | Recurrence relation structural parser (Master Theorem, Characteristic Equation, Iteration) and tree generator. |
| [`visualizer.py`](file:///c:/Users/Vedant/Downloads/intelligent-problem-solver-v3.2-array-input/visualizer.py) | Interactive Plotly renderers for array bars, NetworkX graphs, recursion trees, and ML metrics. |
| [`requirements.txt`](file:///c:/Users/Vedant/Downloads/intelligent-problem-solver-v3.2-array-input/requirements.txt) | Python dependencies (`streamlit`, `scikit-learn`, `plotly`, `networkx`, `pandas`, `numpy`). |
| [`run_app.bat`](file:///c:/Users/Vedant/Downloads/intelligent-problem-solver-v3.2-array-input/run_app.bat) | One-click Windows batch launcher. |
