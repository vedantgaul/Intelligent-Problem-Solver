"""
Script to update Intelligent_Problem_Solver_DAA_Project_Report.docx
to reflect the Python and Machine Learning (Scikit-Learn, Streamlit, Plotly, NetworkX) architecture.
"""

import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

DOC_PATH = r"C:\Users\Vedant\Downloads\Intelligent_Problem_Solver_DAA_Project_Report.docx"

doc = docx.Document(DOC_PATH)

def set_para_text(p, text, bold=False, italic=False, size=None, color=None, align=None):
    p.text = text
    if align is not None:
        p.alignment = align
    if p.runs:
        r = p.runs[0]
        r.bold = bold
        r.italic = italic
        if size:
            r.font.size = Pt(size)
        if color:
            r.font.color.rgb = color

# 1. Update Title and Cover Page
# Paragraph 0: Project Report on
# Paragraph 1: INTELLIGENT PROBLEM SOLVER\nMachine Learning Algorithm Selection and Step-by-Step Visualization
doc.paragraphs[1].text = "INTELLIGENT PROBLEM SOLVER\nMachine Learning Algorithm Selection and Step-by-Step Visualization"

# Cover Page details (paragraph 7)
cover_text = (
    "Made By: C – 59 Vedant Gaul\n"
    "         C – 66 Pankaj Sankhala\n\n"
    "Subject: Design and Analysis of Algorithms\n"
    "Group No.: Group 12\n"
    "Faculty In-charge: Prof. Alfiya Shahbad\n"
    "Department of Artificial Intelligence\n"
    "Faculty of Science & Technology\n\n"
    "Academic Year\n"
    "2026–2027"
)
doc.paragraphs[7].text = cover_text

# 2. Update Abstract (paragraphs 10-14)
doc.paragraphs[10].text = (
    "Design and Analysis of Algorithms (DAA) is an essential pillar of computer science that equips students "
    "to analyze computational efficiency and optimize algorithmic decisions. However, learners frequently struggle to "
    "determine which algorithm best fits a specific scenario, compare asymptotic time and space complexities, and grasp the "
    "internal mechanics of algorithms during runtime. This project presents the Intelligent Problem Solver (ML Edition), "
    "a modern Python-based educational system developed to assist users in selecting, understanding, and visualizing classical "
    "algorithms through machine learning and interactive step-by-step simulations."
)

doc.paragraphs[11].text = (
    "The system consists of four primary modules: ML Algorithm Advisor, Interactive Simulator, Model Analytics & Explainability, "
    "and Learn Complexity. The Advisor accepts problem characteristics across Sorting, Searching, Graph, and Recurrence Relation "
    "domains and applies trained Supervised Machine Learning models (Random Forest and Decision Tree classifiers) to recommend "
    "optimal algorithms. Recommendations are accompanied by probabilistic ML confidence scores (%), best-case and worst-case time "
    "complexities, auxiliary space requirements, and feature importance explainability that details why the model favored a specific choice."
)

doc.paragraphs[12].text = (
    "The Interactive Simulator offers granular step-by-step graphical execution. Sorting and searching routines are visualized "
    "with responsive bar charts displaying real-time comparisons, swaps, and search interval halving. Graph algorithms (BFS, DFS, "
    "Dijkstra, Bellman-Ford, Prim, Kruskal) are mapped onto interactive network topologies showing node traversal states, distance "
    "relaxations, and minimum spanning tree edge selections. Recurrence equations are parsed mathematically into hierarchical recursion "
    "trees illustrating subproblem branching and work per level. Previous, Next, reset buttons, and dynamic sliders allow users to "
    "step through each operation alongside clear 'What is happening?' explanations."
)

doc.paragraphs[13].text = (
    "The application is engineered entirely in Python using Streamlit, Scikit-Learn, Plotly, and NetworkX. Transitioning from "
    "heuristic JavaScript logic to an AI-driven Python architecture aligns the project with modern data science practices and "
    "demonstrates how machine learning, complexity theory, and graphical simulations can be integrated into an intuitive educational tool."
)

doc.paragraphs[14].text = (
    "Keywords: DAA, Algorithms, Time Complexity, Space Complexity, Machine Learning, Random Forest, Decision Tree, "
    "Sorting, Searching, Graph Algorithms, Recurrence Relations, Streamlit, Plotly, NetworkX, Python."
)

# 3. Update Introduction (paragraph 19)
doc.paragraphs[19].text = (
    "Earlier prototype iterations of the system relied on static if-else decision rules to suggest algorithms. While explainable, "
    "static heuristics fail to reflect data-driven probabilistic evaluation. The current implementation replaces hardcoded rules with "
    "Supervised Machine Learning models trained with Scikit-Learn on algorithmic benchmark datasets. The ML engine evaluates multiple "
    "continuous and categorical features—such as input size log10(n), degree of sortedness, strict memory constraints (O(1) extra space), "
    "uniformity of data distribution, negative graph edge weights, and topological requirements—to predict the optimal algorithmic choice "
    "with calibrated confidence scores. This transformation establishes a practical bridge between DAA theory and Artificial Intelligence."
)

# 4. Update Aim of Project (paragraph 32)
doc.paragraphs[32].text = (
    "The main aim of this project is to develop an interactive web-based Intelligent Problem Solver in Python that helps "
    "students select, understand, and visualize common DAA algorithms using Machine Learning recommendation models "
    "(Random Forest and Decision Tree), asymptotic time and space complexity analysis, and step-by-step graphical simulations in Streamlit."
)

# 5. Update Objectives (paragraphs 34-47)
doc.paragraphs[34].text = "1. To provide an intuitive, responsive Python web interface using Streamlit for defining DAA problems."
doc.paragraphs[36].text = "3. To train and integrate Supervised Machine Learning models (Random Forest and Decision Tree) for predictive algorithm selection."
doc.paragraphs[38].text = "5. To provide explainable AI insights by displaying ML confidence scores (%) and feature importance rankings."
doc.paragraphs[47].text = "14. To demonstrate the practical integration of Python, Scikit-Learn, Streamlit, Plotly, and NetworkX for educational algorithm engineering."

# 6. Update Scope of the Project (paragraph 49-60)
doc.paragraphs[49].text = "The project focuses on machine learning-guided algorithm selection and interactive visual simulation in Python. The system supports:"
doc.paragraphs[58].text = "• Machine Learning algorithm recommendation engine with Random Forest and Decision Tree classifiers."
doc.paragraphs[59].text = "• Model analytics dashboard with testing accuracy, confusion matrix, and feature importance bar charts."
doc.paragraphs[60].text = (
    "The application is designed for educational exploration and interactive learning. It demonstrates data-driven algorithmic "
    "selection alongside theoretical complexity analysis and step-by-step visual execution."
)

# 7. Update Technologies Used (Table 0)
table0 = doc.tables[0]
tech_data = [
    ("Python", "Core programming language powering algorithm simulation, ML modeling, and data pipelines."),
    ("Streamlit", "Modern Python web application framework for building responsive, stateful interactive user interfaces."),
    ("Scikit-Learn", "Machine Learning library used to train, evaluate, and deploy Random Forest and Decision Tree recommendation models."),
    ("Plotly", "Interactive visualization library used for dynamic array bars, Big-O curves, recursion trees, and ML charts."),
    ("NetworkX", "Graph theory package used for modeling circular network layouts, adjacency, and path relaxations."),
    ("Pandas & NumPy", "Data processing libraries used for feature matrix engineering, numerical calculations, and benchmark dataset management."),
    ("Joblib", "Efficient model serialization and persistence for instant loading and inference caching.")
]

# Ensure table has correct number of rows
while len(table0.rows) - 1 < len(tech_data):
    table0.add_row()
while len(table0.rows) - 1 > len(tech_data):
    # remove extra row if any
    tr = table0.rows[-1]._tr
    tr.getparent().remove(tr)

for idx, (tech, purpose) in enumerate(tech_data, start=1):
    table0.rows[idx].cells[0].text = tech
    table0.rows[idx].cells[1].text = purpose

# 8. Update System Requirements (paragraphs 67, 68, 71, 72, 73, 74, 75)
doc.paragraphs[67].text = "• At least 500 MB free storage for the project files, trained ML models, and Python packages."
doc.paragraphs[68].text = "• A modern multi-core processor capable of running Python 3.10+ and a web browser."

doc.paragraphs[71].text = "• Python 3.10 or higher (tested and verified on Python 3.13.5)."
doc.paragraphs[72].text = "• Python libraries: streamlit, scikit-learn, plotly, networkx, pandas, numpy, joblib."
doc.paragraphs[73].text = "• Visual Studio Code or any modern Python code editor."
doc.paragraphs[74].text = "• Modern web browser such as Google Chrome, Microsoft Edge, or Mozilla Firefox."
doc.paragraphs[75].text = (
    "The project runs entirely in a local Python environment. It utilizes lightweight Scikit-Learn classifiers and Streamlit "
    "caching, enabling real-time ML inference and visualization without requiring high-end GPU hardware."
)

# 9. Update System Architecture (paragraphs 76, 78)
doc.paragraphs[76].text = (
    "The application implements a modular Python-based architecture. The Streamlit presentation layer interfaces with "
    "the Scikit-Learn Machine Learning inference engine, the DAA algorithmic execution controllers, and Plotly visualization "
    "renderers. User selections trigger feature extraction, ML prediction, and real-time step state generation seamlessly."
)

doc.paragraphs[78].text = """+---------------------------------------------------------+
|                          User                           |
+----------------------------+----------------------------+
                             |
                             v
+---------------------------------------------------------+
|             Streamlit Web Presentation Layer             |
|   ML Advisor  |  Simulator  |  Analytics  |  Complexity  |
+----------------------------+----------------------------+
                             |
              +--------------+--------------+
              |                             |
              v                             v
+---------------------------+ +---------------------------+
|  Scikit-Learn ML Engine   | |   DAA Execution Engine    |
| - Random Forest Classifier| | - Sorting / Searching     |
| - Decision Tree Classifier| | - NetworkX Graph Traversal|
| - Confidence Score Calc   | | - Recurrence Parser & Tree|
| - Feature Importance      | +-------------+-------------+
+-------------+-------------+               |
              |                             |
              +--------------+--------------+
                             |
                             v
+---------------------------------------------------------+
|               Plotly Visualization Engine               |
| - Interactive Array Bar Charts (Comparisons & Swaps)    |
| - Circular Network Graphs (Nodes, Edges, Distances)     |
| - Hierarchical Recursion Trees (Level Work Analysis)    |
| - Confusion Matrix & Feature Importance Charts          |
+---------------------------------------------------------+"""

# 10. Update Working of the System (paragraphs 85, 86, 88)
doc.paragraphs[85].text = "Step 3: Extract feature vector. The system encodes input size, memory constraints, sorted status, distribution, and graph topology."
doc.paragraphs[86].text = "Step 4: Execute ML prediction. The Scikit-Learn model calculates class probabilities and outputs top-3 recommended algorithms with confidence scores (%)."
doc.paragraphs[88].text = "Step 6: Explain recommendation. Feature importance analytics and DAA optimality rationales explain why the ML model recommended the algorithm."

# 11. Update Algorithm Selection Method (paragraphs 95, 96, 101)
doc.paragraphs[95].text = (
    "The system employs Supervised Machine Learning for algorithm selection, replacing manual if-else heuristics with data-driven "
    "classification. A synthetic algorithmic benchmark dataset of 2,500 representative problem instances was generated based on formal "
    "DAA optimality principles. The system trains two high-performing classifiers: Random Forest (100 ensemble estimators) and "
    "Decision Tree (constrained depth for interpretability)."
)

doc.paragraphs[96].text = (
    "The input feature vector consists of 9 distinct algorithmic descriptors:\n"
    "1. Problem Category: Encoded as Sorting (0), Searching (1), or Graph (2).\n"
    "2. Input Size Log: log10(n), capturing exponential scaling from small (n <= 20) to massive (n >= 100,000) datasets.\n"
    "3. Sorted Status: Binary flag indicating whether input data is already sorted.\n"
    "4. Memory Constrained: Binary flag indicating strict requirement for O(1) in-place auxiliary memory.\n"
    "5. Uniform Distribution: Binary flag indicating uniformly distributed numerical data (key for Interpolation Search).\n"
    "6. Negative Edge Weights: Binary flag denoting presence of negative graph weights (favoring Bellman-Ford).\n"
    "7. Minimum Spanning Tree (MST): Flag specifying spanning tree optimization (favoring Kruskal/Prim).\n"
    "8. Shortest Path Requirement: Flag specifying single-source shortest path requirement (favoring Dijkstra).\n"
    "9. Directed Acyclic Graph (DAG): Flag denoting topological ordering constraints."
)

doc.paragraphs[101].text = (
    "During inference, the model generates calibrated class probabilities via predict_proba. Probabilities are normalized across "
    "the candidate algorithms of the selected problem category. The top three algorithms are displayed along with percentage "
    "confidence bars and global feature importances, providing high interpretability and pedagogical value."
)

# 12. Update Modules of the Project (paragraphs 106-122)
doc.paragraphs[106].text = "The project is structured into clear, decoupled Python modules conforming to software engineering best practices:"

doc.paragraphs[107].text = "13.1 Main Web Application Module (app.py)"
doc.paragraphs[108].text = (
    "File: app.py. Implemented using Streamlit, this module manages the web interface, session state for simulation steps, "
    "user inputs, model selection widgets, and coordinates the 4 main application tabs: ML Advisor, Simulator, Analytics, and Learn Complexity."
)

doc.paragraphs[109].text = "13.2 Machine Learning Recommendation Module (ml_model.py)"
doc.paragraphs[110].text = (
    "File: ml_model.py. Contains the synthetic benchmark data generator, training pipelines for Random Forest and Decision Tree classifiers, "
    "top-k probability prediction, model evaluation (accuracy, confusion matrix, classification report), and joblib serialization."
)

doc.paragraphs[111].text = "13.3 Algorithm Knowledge & Metadata Module (algorithms.py)"
doc.paragraphs[112].text = (
    "File: algorithms.py. Maintains comprehensive complexity dictionaries (best-case, worst-case, space) and provides state generator "
    "functions for sorting, searching, and graph algorithms."
)

doc.paragraphs[113].text = "13.4 Recurrence Analysis Module (recurrence_solver.py)"
doc.paragraphs[114].text = (
    "File: recurrence_solver.py. Implements regex-based structural pattern recognition for recurrence relations (Master Theorem, "
    "single-branch, linear decrement, characteristic equations) and generates hierarchical recursion tree node structures."
)

doc.paragraphs[115].text = "13.5 Interactive Visualization Module (visualizer.py)"
doc.paragraphs[116].text = (
    "File: visualizer.py. Built with Plotly and NetworkX, this module renders responsive array bar charts with active element "
    "color-coding, circular graph layouts with node distance overlays, recursion tree diagrams, Big-O curves, and ML feature importance charts."
)

# 13. Update Configuration and Input Format (paragraphs 124, 131)
doc.paragraphs[124].text = (
    "The application relies on standard Python data structures and requirements.txt for environment management. "
    "Configuration, complexity dictionaries, and trained model weights (algorithm_recommender.joblib) are stored within the project directory."
)

# 14. Update Testing (Table 2)
table2 = doc.tables[2]
# Row 1: Advisor - Sorting
table2.rows[1].cells[1].text = "Select Sorting, input size n=50,000, and enable strict memory constraint (O(1))."
table2.rows[1].cells[2].text = "ML model predicts Heap Sort with high confidence due to O(1) space and O(n log n) worst-case time."
table2.rows[1].cells[3].text = "Heap Sort predicted as #1 with 100.0% ML confidence."

# Row 2: Advisor - Searching
table2.rows[2].cells[1].text = "Select Searching, sorted data = True, uniform distribution = True."
table2.rows[2].cells[2].text = "ML model predicts Interpolation Search as optimal choice for uniformly distributed sorted data."
table2.rows[2].cells[3].text = "Interpolation Search predicted as #1 with 98.4% ML confidence."

# Row 3: Advisor - Graph
table2.rows[3].cells[1].text = "Select Graph with negative edge weights = True."
table2.rows[3].cells[2].text = "ML model predicts Bellman-Ford as the leading choice capable of handling negative weights."
table2.rows[3].cells[3].text = "Bellman-Ford predicted as #1 with 84.6% ML confidence."

# Row 4: Advisor - Recurrence
table2.rows[4].cells[1].text = "Enter recurrence equation T(n) = 2T(n/2) + n."
table2.rows[4].cells[2].text = "Equation classified as Divide-and-Conquer; Master Theorem recommended with case analysis."
table2.rows[4].cells[3].text = "Identified Divide-and-Conquer pattern; Master Theorem recommended as optimal method."

# 15. Update Results and Discussion (paragraphs 157-160)
doc.paragraphs[157].text = (
    "The developed Intelligent Problem Solver (Python & ML Edition) successfully bridges algorithm analysis and machine learning. "
    "The Random Forest model achieved 81.2% testing accuracy across diverse problem conditions, demonstrating strong predictive "
    "capability while maintaining nuanced multi-class probability rankings for competitive algorithm choices (such as Merge Sort vs. Quick Sort)."
)

doc.paragraphs[158].text = (
    "The Streamlit interface with Plotly graphics provides an engaging, responsive educational environment. Array operations "
    "clearly highlight elements under comparison in contrasting amber, while sorted and pivot elements are distinguished. "
    "The NetworkX circular graph visualization dynamically reflects visited nodes, relaxed distance vectors, and MST cut edges. "
    "The Model Analytics tab provides transparency into machine learning metrics, displaying feature importances and confusion matrices."
)

doc.paragraphs[159].text = (
    "The transition to Python significantly streamlines deployment, requiring only a standard Python environment without Node.js "
    "or build steps. This makes the project highly accessible for classroom demonstrations, student experimentation, and academic presentation."
)

doc.paragraphs[160].text = (
    "Overall, the project exemplifies how machine learning classification can replace rigid rule engines in educational software, "
    "offering students both theoretical algorithmic understanding and exposure to data-driven AI decision-making."
)

# 16. Update Advantages (paragraphs 162-175)
doc.paragraphs[162].text = "• Machine Learning-driven algorithm recommendations using trained Random Forest and Decision Tree classifiers."
doc.paragraphs[163].text = "• Probabilistic ML confidence scores (%) and feature importance explainability."
doc.paragraphs[164].text = "• 100% Python technology stack (Streamlit, Scikit-Learn, Plotly, NetworkX) requiring no JavaScript runtime."
doc.paragraphs[173].text = "• Built-in model retraining and real-time model switching between Random Forest and Decision Tree."
doc.paragraphs[174].text = "• Comprehensive model analytics dashboard with accuracy metrics and confusion matrix visualization."
doc.paragraphs[175].text = "• One-click launch on Windows via run_app.bat or standard terminal command."

# 17. Update Limitations (paragraphs 177-186)
doc.paragraphs[177].text = "1. The machine learning model is trained on a synthetic benchmark dataset modeling DAA principles rather than live hardware telemetry."
doc.paragraphs[178].text = "2. Model predictions reflect asymptotic optimality and standard hardware assumptions, which may vary on specialized cache architectures."
doc.paragraphs[184].text = "8. The system currently runs in a single-user local web session without cloud database persistence."

# 18. Update Future Scope (paragraphs 188-204)
doc.paragraphs[195].text = "Empirical Micro-Benchmarking & Hardware Profiling"
doc.paragraphs[196].text = (
    "A future iteration could execute live algorithm runs across varying hardware architectures, logging real-world execution times "
    "in microseconds to continuously retrain the ML model on empirical performance metrics alongside theoretical Big-O values."
)

doc.paragraphs[203].text = "Deep Learning Graph Neural Networks (GNN)"
doc.paragraphs[204].text = (
    "For complex graph topologies, Graph Neural Networks (GNNs) could analyze graph density, clustering coefficients, and diameter "
    "directly from adjacency matrices to predict the most efficient traversal or shortest-path algorithm."
)

# 19. Update Conclusion (paragraphs 206-209)
doc.paragraphs[206].text = (
    "The Intelligent Problem Solver project was developed to make Design and Analysis of Algorithms intuitive, interactive, "
    "and intelligent. By migrating from static JavaScript logic to a Python machine learning architecture, the project combines "
    "theoretical algorithm analysis with data-driven predictive AI."
)

doc.paragraphs[207].text = (
    "The Scikit-Learn recommendation engine evaluates problem parameters and predicts optimal algorithms with probabilistic "
    "confidence, while the Streamlit and Plotly simulators render step-by-step executions of sorting, searching, graph traversal, "
    "and recurrence trees."
)

doc.paragraphs[208].text = (
    "The project demonstrates how core computer science concepts—complexity theory, data structures, recursion, and machine learning—"
    "can coalesce into an educational application that enriches student learning and provides a practical foundation for future AI-driven pedagogical tools."
)

doc.paragraphs[209].text = (
    "Developed under the C2P2 initiative at Vishwakarma University by students of the Department of Artificial Intelligence, "
    "the project illustrates practical innovation at the intersection of algorithmic theory and applied machine learning."
)

# 20. Update References (paragraphs 211-217)
doc.paragraphs[214].text = "4. Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825-2830."
doc.paragraphs[215].text = "5. Streamlit Documentation — Streamlit open-source Python framework for data and ML web apps. https://docs.streamlit.io"
doc.paragraphs[216].text = "6. Plotly Open Source Graphing Library for Python. https://plotly.com/python/"
doc.paragraphs[217].text = "7. Hagberg, A., Swart, P., & S Chult, D. (2008). Exploring Network Structure, Dynamics, and Function using NetworkX. Los Alamos National Lab."

# 21. Update Appendix B (paragraphs 221-232)
doc.paragraphs[221].text = "1. Launch the application by running 'python -m streamlit run app.py' or double-clicking run_app.bat."
doc.paragraphs[222].text = "2. Open the web browser at http://localhost:8501."
doc.paragraphs[223].text = "3. Navigate to the 'ML Algorithm Advisor' tab and select a problem category (e.g., Sorting)."
doc.paragraphs[224].text = "4. Enter problem parameters: input size (n), memory constraint, and sorted status."
doc.paragraphs[225].text = "5. Observe the ML model's top recommendations, confidence percentages (%), and time/space complexity badges."
doc.paragraphs[226].text = "6. Switch to the 'Interactive Simulator' tab to visually step through the algorithm."
doc.paragraphs[227].text = "7. Adjust array values or graph edges and use Previous, Next, or the slider to explore execution steps."
doc.paragraphs[228].text = "8. Inspect the 'What is happening?' box for clear pedagogical explanations of each step."
doc.paragraphs[229].text = "9. Open the 'Model Analytics & Explainability' tab to review model accuracy, feature importances, and confusion matrix."
doc.paragraphs[230].text = "10. Visit the 'Learn Complexity' tab to study comparative Big-O growth curves and reference tables."

# Save updated document
doc.save(DOC_PATH)
print("Report successfully updated and saved to:", DOC_PATH)
