"""
Intelligent Problem Solver - Python & Machine Learning Edition
DAA & AI Project - Vishwakarma University, Pune
Combines Machine Learning for Algorithm Recommendation with an Interactive Step-by-Step Simulator.
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from ml_model import (
    AlgorithmRecommenderModel, get_or_train_model,
    FEATURE_NAMES, PROBLEM_TYPES
)
from algorithms import (
    SORTING_METADATA, SEARCHING_METADATA, GRAPH_METADATA, RECURRENCE_METADATA,
    get_algo_info, generate_sorting_steps, generate_searching_steps,
    generate_graph_steps
)
from recurrence_solver import analyze_recurrence_equation, generate_rec_tree
from visualizer import (
    render_array_chart, render_graph_chart, render_rec_tree_chart,
    render_complexity_plot, render_feature_importance_plot,
    render_confusion_matrix_plot
)

# Set page configuration
st.set_page_config(
    page_title="Intelligent Problem Solver | ML Edition",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS matching the clean, academic, modern theme
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #f5f7fb;
    }
    .top-header {
        background: linear-gradient(135deg, #1f3a5f 0%, #2d5485 100%);
        color: white;
        padding: 24px 32px;
        border-radius: 14px;
        margin-bottom: 24px;
        box-shadow: 0 4px 15px rgba(31, 58, 95, 0.15);
    }
    .top-header h1 {
        margin: 0;
        font-size: 28px;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    .top-header p {
        margin: 6px 0 0 0;
        opacity: 0.9;
        font-size: 14px;
    }
    .badge {
        background: rgba(255, 255, 255, 0.2);
        color: #ffffff;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    .algo-card {
        background: white;
        border: 1px solid #e2e8ee;
        border-radius: 12px;
        padding: 18px 20px;
        margin-bottom: 14px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .algo-card:hover {
        box-shadow: 0 6px 16px rgba(31, 58, 95, 0.08);
    }
    .algo-card-top {
        border-left: 5px solid #1f3a5f;
        background: #fafcfe;
    }
    .pill {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 4px;
    }
    .pill-time { background: #eef4fb; color: #1f3a5f; }
    .pill-space { background: #f3edf8; color: #5c2d91; }
    .pill-conf { background: #e6f4ea; color: #137333; font-weight: 700; }
    .step-box {
        background: #f6f9fb;
        border-left: 4px solid #47719e;
        border-radius: 8px;
        padding: 14px 18px;
        margin-top: 14px;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# Cache model training/loading for optimal responsiveness
@st.cache_resource
def load_ml_model(model_type="random_forest"):
    return get_or_train_model(model_type=model_type)

# App Header
st.markdown("""
<div class="top-header">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1>💡 Intelligent Problem Solver</h1>
            <p>Machine Learning Algorithm Recommender & Interactive Step-by-Step Simulator</p>
        </div>
        <div>
            <span class="badge">DAA & AI Project</span>
            <span class="badge" style="margin-left: 6px;">Vishwakarma University</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ ML Model Settings")
    model_choice = st.selectbox(
        "Select Recommendation Model",
        ["Random Forest Classifier", "Decision Tree Classifier"],
        index=0
    )
    model_key = "decision_tree" if "Decision" in model_choice else "random_forest"
    model = load_ml_model(model_key)

    st.markdown(f"**Model Accuracy:** `{model.accuracy * 100:.1f}%`")
    st.markdown(f"**Model Type:** `{model.model_type.replace('_', ' ').title()}`")

    if st.button("🔄 Retrain ML Model"):
        with st.spinner("Retraining model on algorithmic benchmark dataset..."):
            model = get_or_train_model(model_type=model_key, force_retrain=True)
            st.success("Model retrained successfully!")

    st.markdown("---")
    st.markdown("### 🎓 Academic Context")
    st.info(
        "**Department of Artificial Intelligence**\n"
        "Design & Analysis of Algorithms (DAA)\n"
        "Integrates Supervised Machine Learning to replace static rule engines with probabilistic, data-driven algorithm selection."
    )

# Main Application Tabs
tab_advisor, tab_simulator, tab_analytics, tab_learn = st.tabs([
    "🎯 ML Algorithm Advisor",
    "🔬 Interactive Simulator",
    "📊 Model Analytics & Explainability",
    "📚 Learn Complexity"
])

# =========================================================================
# TAB 1: ML ADVISOR
# =========================================================================
with tab_advisor:
    col_input, col_output = st.columns([1, 1.2], gap="large")

    with col_input:
        st.subheader("1. Describe Your Problem")
        problem_type = st.selectbox(
            "Problem Category",
            ["Sorting", "Searching", "Graph", "Recurrence Relation"]
        )

        features = {"problem_type": problem_type}

        if problem_type == "Recurrence Relation":
            rec_equation = st.text_input(
                "Recurrence Equation",
                value="T(n) = 2T(n/2) + n",
                help="Enter standard recurrence like T(n) = 2T(n/2) + n or T(n) = T(n-1) + C"
            )
            st.caption("Presets: `T(n) = 2T(n/2) + n` (Merge Sort) | `T(n) = T(n/2) + C` (Binary Search) | `T(n) = T(n-1) + 1` (Linear)")

        elif problem_type == "Sorting":
            n = st.number_input("Input Size (n)", min_value=1, max_value=1000000, value=1000, step=100)
            features["input_size"] = n

            memory_constrained = st.checkbox("Strict Memory Constraint (Requires O(1) auxiliary space)", value=False)
            features["memory_constrained"] = memory_constrained

            is_sorted = st.checkbox("Array is already nearly sorted", value=False)
            features["is_sorted"] = is_sorted

            condition = st.selectbox(
                "Optimization Priority",
                ["Balanced / General", "Small input (n ≤ 20)", "Large input (n > 1000)", "In-place execution (O(1) memory)"]
            )
            if "Small" in condition:
                features["input_size"] = min(n, 20)
            elif "Large" in condition:
                features["input_size"] = max(n, 2000)
            elif "In-place" in condition:
                features["memory_constrained"] = True

        elif problem_type == "Searching":
            n = st.number_input("Input Size (n)", min_value=1, max_value=1000000, value=1000, step=100)
            features["input_size"] = n

            is_sorted = st.checkbox("Data is sorted", value=True)
            features["is_sorted"] = is_sorted

            uniform_dist = st.checkbox("Values are uniformly distributed (e.g. arithmetic progression)", value=False)
            features["uniform_distribution"] = uniform_dist

        elif problem_type == "Graph":
            n_vertices = st.number_input("Number of Vertices (V)", min_value=2, max_value=50000, value=100)
            features["input_size"] = n_vertices

            graph_objective = st.selectbox(
                "Primary Graph Objective",
                ["Shortest Path", "Minimum Spanning Tree (MST)", "Topological Ordering (DAG)", "Traversal / Exploration"]
            )
            if graph_objective == "Shortest Path":
                features["need_shortest_path"] = True
            elif graph_objective == "Minimum Spanning Tree (MST)":
                features["need_mst"] = True
            elif graph_objective == "Topological Ordering (DAG)":
                features["is_dag"] = True

            negative_weights = st.checkbox("Graph has negative edge weights", value=False)
            features["negative_weights"] = negative_weights

            mem_priority = st.checkbox("Memory is critical / Very dense graph", value=False)
            features["memory_constrained"] = mem_priority

    with col_output:
        st.subheader("2. Recommended Algorithms (ML Model Output)")

        if problem_type == "Recurrence Relation":
            analysis = analyze_recurrence_equation(rec_equation)
            st.success(f"**Identified Category:** {analysis['category']}")
            st.write(analysis['summary'])

            st.markdown("#### Ranked Solving Methods:")
            for i, m in enumerate(analysis["methods"]):
                is_top = (i == 0)
                card_class = "algo-card algo-card-top" if is_top else "algo-card"
                top_badge = '<span class="pill pill-conf">TOP RECOMMENDATION</span>' if is_top else ''

                st.markdown(f"""
                <div class="{card_class}">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0; color: #1f3a5f;">#{i+1} {m['name']}</h4>
                        {top_badge}
                    </div>
                    <div style="margin: 6px 0;">
                        <span class="pill pill-time">{m['match']}</span>
                    </div>
                    <p style="margin: 6px 0 0 0; color: #4a5568; font-size: 13px;"><b>Why:</b> {m['why']}</p>
                </div>
                """, unsafe_allow_html=True)

        else:
            # Run ML Model Prediction
            predictions = model.predict_top_k(features, k=3)

            st.caption(f"Predictions generated by **{model_choice}** using input problem features.")

            for rank, (algo_name, confidence) in enumerate(predictions):
                meta = get_algo_info(problem_type, algo_name)
                is_top = (rank == 0)
                card_class = "algo-card algo-card-top" if is_top else "algo-card"

                time_info = meta.get('worst', meta.get('time', 'O(n)'))
                space_info = meta.get('space', 'O(1)')
                desc = meta.get('desc', '')
                why_text = meta.get('why', '')

                st.markdown(f"""
                <div class="{card_class}">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0; color: #1f3a5f;">#{rank+1} {algo_name}</h4>
                        <span class="pill pill-conf">ML Confidence: {confidence*100:.1f}%</span>
                    </div>
                    <div style="margin: 8px 0 6px 0;">
                        <span class="pill pill-time">Time: {time_info}</span>
                        <span class="pill pill-space">Space: {space_info}</span>
                    </div>
                    <p style="margin: 4px 0; color: #4a5568; font-size: 13px;">{desc}</p>
                    <p style="margin: 6px 0 0 0; color: #2d3748; font-size: 12px; background: #f7fafc; padding: 6px 10px; border-radius: 6px;">
                        <b>Why Recommended:</b> {why_text}
                    </p>
                </div>
                """, unsafe_allow_html=True)

# =========================================================================
# TAB 2: INTERACTIVE SIMULATOR
# =========================================================================
with tab_simulator:
    sim_category = st.radio(
        "Select Simulation Category",
        ["Sorting", "Searching", "Graph", "Recurrence Tree"],
        horizontal=True
    )

    # 1. SORTING SIMULATOR
    if sim_category == "Sorting":
        col_ctrl, col_viz = st.columns([1, 2], gap="medium")

        with col_ctrl:
            st.markdown("#### Controls")
            algo_sort = st.selectbox("Algorithm", list(SORTING_METADATA.keys()))
            meta = SORTING_METADATA[algo_sort]
            st.caption(f"**Time:** `{meta['worst']}` | **Space:** `{meta['space']}`")

            arr_text = st.text_input("Enter Array Elements (comma-separated)", "64, 25, 12, 22, 11, 90, 34, 7")
            try:
                arr = [int(x.strip()) for x in arr_text.split(",") if x.strip()][:14]
            except ValueError:
                arr = [64, 25, 12, 22, 11, 90, 34, 7]
                st.warning("Invalid numbers entered. Using default array.")

            # Generate steps
            sort_steps = generate_sorting_steps(algo_sort, arr)
            total_steps = len(sort_steps)

            if "sort_idx" not in st.session_state:
                st.session_state.sort_idx = 0
            if st.session_state.sort_idx >= total_steps:
                st.session_state.sort_idx = total_steps - 1

            c_prev, c_next, c_reset = st.columns(3)
            with c_prev:
                if st.button("⬅️ Prev", key="sort_prev", disabled=(st.session_state.sort_idx == 0)):
                    st.session_state.sort_idx -= 1
            with c_next:
                if st.button("Next ➡️", key="sort_next", disabled=(st.session_state.sort_idx >= total_steps - 1)):
                    st.session_state.sort_idx += 1
            with c_reset:
                if st.button("Reset", key="sort_reset"):
                    st.session_state.sort_idx = 0

            step_idx = st.slider(
                "Step Slider",
                0, total_steps - 1,
                value=st.session_state.sort_idx,
                key="sort_slider"
            )
            st.session_state.sort_idx = step_idx

        with col_viz:
            st.markdown(f"#### Step {st.session_state.sort_idx + 1} of {total_steps}: {sort_steps[st.session_state.sort_idx]['text']}")
            cur_step = sort_steps[st.session_state.sort_idx]
            fig = render_array_chart(cur_step)
            if fig:
                st.plotly_chart(fig, use_container_width=True)

            st.markdown(f"""
            <div class="step-box">
                <b>What is happening?</b><br>
                {cur_step['description']}
            </div>
            """, unsafe_allow_html=True)

    # 2. SEARCHING SIMULATOR
    elif sim_category == "Searching":
        col_ctrl, col_viz = st.columns([1, 2], gap="medium")

        with col_ctrl:
            st.markdown("#### Controls")
            algo_search = st.selectbox("Algorithm", ["Linear Search", "Binary Search"])
            meta = SEARCHING_METADATA[algo_search]
            st.caption(f"**Worst Time:** `{meta['worst']}` | **Space:** `{meta['space']}`")

            arr_text = st.text_input("Enter Array (comma-separated)", "11, 12, 22, 25, 34, 64, 90")
            try:
                arr = [int(x.strip()) for x in arr_text.split(",") if x.strip()][:20]
            except ValueError:
                arr = [11, 12, 22, 25, 34, 64, 90]

            target_val = st.number_input("Search Target", value=25)

            search_steps = generate_searching_steps(algo_search, arr, target_val)
            total_steps = len(search_steps)

            if "search_idx" not in st.session_state:
                st.session_state.search_idx = 0
            if st.session_state.search_idx >= total_steps:
                st.session_state.search_idx = total_steps - 1

            c_prev, c_next, c_reset = st.columns(3)
            with c_prev:
                if st.button("⬅️ Prev", key="search_prev", disabled=(st.session_state.search_idx == 0)):
                    st.session_state.search_idx -= 1
            with c_next:
                if st.button("Next ➡️", key="search_next", disabled=(st.session_state.search_idx >= total_steps - 1)):
                    st.session_state.search_idx += 1
            with c_reset:
                if st.button("Reset", key="search_reset"):
                    st.session_state.search_idx = 0

            step_idx = st.slider(
                "Step Slider",
                0, total_steps - 1,
                value=st.session_state.search_idx,
                key="search_slider"
            )
            st.session_state.search_idx = step_idx

        with col_viz:
            st.markdown(f"#### Step {st.session_state.search_idx + 1} of {total_steps}: {search_steps[st.session_state.search_idx]['text']}")
            cur_step = search_steps[st.session_state.search_idx]
            fig = render_array_chart(cur_step)
            if fig:
                st.plotly_chart(fig, use_container_width=True)

            st.markdown(f"""
            <div class="step-box">
                <b>What is happening?</b><br>
                {cur_step['description']}
            </div>
            """, unsafe_allow_html=True)

    # 3. GRAPH SIMULATOR
    elif sim_category == "Graph":
        col_ctrl, col_viz = st.columns([1, 2], gap="medium")

        with col_ctrl:
            st.markdown("#### Controls")
            algo_graph = st.selectbox("Algorithm", ["BFS", "DFS", "Dijkstra", "Bellman-Ford", "Prim", "Kruskal"])
            meta = GRAPH_METADATA[algo_graph]
            st.caption(f"**Time:** `{meta['worst']}` | **Space:** `{meta['space']}`")

            default_edges = "A B 4\nA C 2\nB C 1\nB D 5\nC D 8\nC E 10\nD E 2"
            graph_text = st.text_area("Graph Edges (u v weight)", default_edges, height=130)

            graph_res = generate_graph_steps(algo_graph, graph_text)
            graph_steps = graph_res["steps"]
            total_steps = len(graph_steps)

            if "graph_idx" not in st.session_state:
                st.session_state.graph_idx = 0
            if st.session_state.graph_idx >= total_steps:
                st.session_state.graph_idx = total_steps - 1

            c_prev, c_next, c_reset = st.columns(3)
            with c_prev:
                if st.button("⬅️ Prev", key="graph_prev", disabled=(st.session_state.graph_idx == 0)):
                    st.session_state.graph_idx -= 1
            with c_next:
                if st.button("Next ➡️", key="graph_next", disabled=(st.session_state.graph_idx >= total_steps - 1)):
                    st.session_state.graph_idx += 1
            with c_reset:
                if st.button("Reset", key="graph_reset"):
                    st.session_state.graph_idx = 0

            step_idx = st.slider(
                "Step Slider",
                0, total_steps - 1,
                value=st.session_state.graph_idx,
                key="graph_slider"
            )
            st.session_state.graph_idx = step_idx

        with col_viz:
            st.markdown(f"#### Step {st.session_state.graph_idx + 1} of {total_steps}: {graph_steps[st.session_state.graph_idx]['text']}")
            cur_step = graph_steps[st.session_state.graph_idx]
            fig = render_graph_chart(graph_res["nodes"], graph_res["edges"], cur_step)
            if fig:
                st.plotly_chart(fig, use_container_width=True)

            st.markdown(f"""
            <div class="step-box">
                <b>What is happening?</b><br>
                {cur_step['description']}
            </div>
            """, unsafe_allow_html=True)

    # 4. RECURRENCE TREE SIMULATOR
    elif sim_category == "Recurrence Tree":
        col_ctrl, col_viz = st.columns([1, 2], gap="medium")

        with col_ctrl:
            st.markdown("#### Tree Parameters")
            n_param = st.slider("Recurrence Input Size (n)", min_value=4, max_value=64, value=16, step=4)
            branching = st.slider("Branching Factor (subproblems a)", min_value=1, max_value=3, value=2)
            depth = st.slider("Max Tree Depth", min_value=1, max_value=4, value=3)

            tree_data = generate_rec_tree(n=n_param, depth=depth, branching=branching)

            st.info(f"Tree shows recursive divide-and-conquer expansion down to depth {depth}.")

        with col_viz:
            st.markdown(f"#### Recursion Tree Visualization (n={n_param}, a={branching})")
            fig = render_rec_tree_chart(tree_data)
            if fig:
                st.plotly_chart(fig, use_container_width=True)

            st.markdown("""
            <div class="step-box">
                <b>Recursion Tree Analysis Method:</b><br>
                Each level i contains a<sup>i</sup> subproblems of size n/b<sup>i</sup>.
                Calculate the work performed per level, then sum across all log<sub>b</sub>(n) levels.
            </div>
            """, unsafe_allow_html=True)

# =========================================================================
# TAB 3: MODEL ANALYTICS & EXPLAINABILITY
# =========================================================================
with tab_analytics:
    st.subheader("Machine Learning Model Performance & Explainability")
    st.write(
        "To fulfill the Artificial Intelligence requirement of the DAA curriculum, "
        "the rule engine is augmented by a trained Machine Learning classifier. "
        "Below are the model metrics and feature importance distributions."
    )

    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Model Architecture", model_choice)
    col_m2.metric("Testing Accuracy", f"{model.accuracy * 100:.1f}%")
    col_m3.metric("Number of Features", len(FEATURE_NAMES))

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        if model.feature_importances_ is not None:
            fig_fi = render_feature_importance_plot(FEATURE_NAMES, model.feature_importances_)
            st.plotly_chart(fig_fi, use_container_width=True)

    with col_chart2:
        if model.cm is not None:
            fig_cm = render_confusion_matrix_plot(model.cm, model.classes_)
            st.plotly_chart(fig_cm, use_container_width=True)

    with st.expander("📄 View Detailed Scikit-Learn Classification Report"):
        st.code(model.classification_rep if model.classification_rep else "Report available upon evaluation.", language="text")

# =========================================================================
# TAB 4: LEARN COMPLEXITY
# =========================================================================
with tab_learn:
    st.subheader("Time and Space Complexity Reference Guide")
    st.write("Big-O notation describes asymptotic resource growth as input size n approaches infinity.")

    col_plot, col_table = st.columns([1.1, 0.9], gap="medium")

    with col_plot:
        fig_comp = render_complexity_plot()
        st.plotly_chart(fig_comp, use_container_width=True)

    with col_table:
        st.markdown("#### Complexity Classes")
        df_comp = pd.DataFrame([
            {"Complexity": "O(1)", "Growth": "Constant", "Example": "Hash table lookup, array indexing"},
            {"Complexity": "O(log n)", "Growth": "Logarithmic", "Example": "Binary Search, Balanced BST search"},
            {"Complexity": "O(n)", "Growth": "Linear", "Example": "Linear Search, Counting Sort (small k)"},
            {"Complexity": "O(n log n)", "Growth": "Linearithmic", "Example": "Merge Sort, Heap Sort, Quick Sort"},
            {"Complexity": "O(n²)", "Growth": "Quadratic", "Example": "Bubble Sort, Insertion Sort (worst-case)"},
            {"Complexity": "O(V + E)", "Growth": "Graph Linear", "Example": "BFS, DFS, Topological Sort"},
            {"Complexity": "O(V³)", "Growth": "Cubic", "Example": "Floyd-Warshall all-pairs shortest paths"}
        ])
        st.dataframe(df_comp, use_container_width=True, hide_index=True)

        st.caption("ℹ️ Notice how O(n²) grows dramatically compared to O(n log n) as n scales above 20.")
