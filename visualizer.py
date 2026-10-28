"""
Interactive Visualizers using Plotly
Renders responsive, high-performance visual representations of:
- Sorting and Searching array bars
- Graph networks (nodes, edges, weights, visited states)
- Recursion Trees
- Big-O Complexity Growth curves
- ML Model Feature Importances and Confusion Matrix
"""

import math
import numpy as np
import plotly.graph_objects as go
import networkx as nx

def render_array_chart(step):
    """Renders interactive array bar chart with highlighted elements."""
    arr = step.get("a", [])
    if not arr:
        return None

    hi = step.get("hi", [])
    focus = step.get("focus", [])

    colors = []
    text_colors = []
    for i, v in enumerate(arr):
        if i in focus:
            colors.append("#2e7d32") # Dark green for pivot/target
            text_colors.append("#ffffff")
        elif i in hi:
            colors.append("#d8a13b") # Amber/Gold for current compare/swap
            text_colors.append("#ffffff")
        else:
            colors.append("#7590a9") # Slate blue for normal
            text_colors.append("#ffffff")

    fig = go.Figure(data=[
        go.Bar(
            x=[f"Idx {i}" for i in range(len(arr))],
            y=arr,
            marker_color=colors,
            marker_line_color="#1f3a5f",
            marker_line_width=1.5,
            text=[f"<b>{v}</b>" for v in arr],
            textposition="auto",
            textfont=dict(color=text_colors, size=13),
            hoverinfo="x+y"
        )
    ])

    max_val = max([abs(x) for x in arr] + [10])
    fig.update_layout(
        height=320,
        margin=dict(l=20, r=20, t=25, b=20),
        yaxis=dict(
            range=[0, max_val * 1.25],
            showgrid=True,
            gridcolor="#e9edf3",
            title="Value"
        ),
        xaxis=dict(showgrid=False, title="Array Index"),
        plot_bgcolor="#f8fafc",
        paper_bgcolor="#ffffff",
    )
    return fig

def render_graph_chart(nodes, edges, step):
    """Renders interactive NetworkX graph with node/edge states."""
    if not nodes:
        return None

    visited = set(step.get("visited", []))
    chosen_pairs = set(step.get("chosen", []))
    cur = step.get("cur", None)
    dist = step.get("dist", {})

    # Create NetworkX graph and circular coordinates
    G = nx.Graph()
    for n in nodes:
        G.add_node(n)
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = nx.circular_layout(G)

    # Edge traces
    edge_x = []
    edge_y = []
    edge_active_x = []
    edge_active_y = []
    edge_label_x = []
    edge_label_y = []
    edge_label_text = []

    for u, v, w in edges:
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        is_active = (f"{u}-{v}" in chosen_pairs or f"{v}-{u}" in chosen_pairs)

        if is_active:
            edge_active_x.extend([x0, x1, None])
            edge_active_y.extend([y0, y1, None])
        else:
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        edge_label_x.append((x0 + x1) / 2)
        edge_label_y.append((y0 + y1) / 2)
        edge_label_text.append(f"w={int(w) if w == int(w) else w}")

    fig = go.Figure()

    # Normal edges
    if edge_x:
        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=2, color="#b8c3cf"),
            hoverinfo="none",
            mode="lines",
            showlegend=False
        ))

    # Active / chosen edges
    if edge_active_x:
        fig.add_trace(go.Scatter(
            x=edge_active_x, y=edge_active_y,
            line=dict(width=5, color="#1f3a5f"),
            hoverinfo="none",
            mode="lines",
            showlegend=False
        ))

    # Edge weight markers
    fig.add_trace(go.Scatter(
        x=edge_label_x, y=edge_label_y,
        mode="text",
        text=edge_label_text,
        textfont=dict(size=11, color="#657386"),
        hoverinfo="none",
        showlegend=False
    ))

    # Node traces
    node_x = []
    node_y = []
    node_colors = []
    node_text = []
    line_colors = []
    text_colors = []

    for n in nodes:
        x, y = pos[n]
        node_x.append(x)
        node_y.append(y)

        # Dist annotation if available
        d_val = dist.get(n)
        d_str = f"\nd:{d_val if d_val != float('inf') else '∞'}" if (dist and d_val is not None) else ""
        node_text.append(f"<b>{n}</b>{d_str}")

        if n == cur:
            node_colors.append("#d8a13b") # Amber for current
            line_colors.append("#946300")
            text_colors.append("#ffffff")
        elif n in visited:
            node_colors.append("#527695") # Blue for visited
            line_colors.append("#1f3a5f")
            text_colors.append("#ffffff")
        else:
            node_colors.append("#ffffff")
            line_colors.append("#8395a8")
            text_colors.append("#1f3a5f")

    fig.add_trace(go.Scatter(
        x=node_x, y=node_y,
        mode="markers+text",
        text=node_text,
        textposition="middle center",
        textfont=dict(color=text_colors, size=12),
        marker=dict(
            size=44,
            color=node_colors,
            line=dict(width=2.5, color=line_colors)
        ),
        hoverinfo="text",
        showlegend=False
    ))

    fig.update_layout(
        height=380,
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor="#f8fafc",
        paper_bgcolor="#ffffff",
    )
    return fig

def render_rec_tree_chart(tree_data):
    """Renders hierarchical recursion tree diagram."""
    nodes = tree_data["nodes"]
    edges = tree_data["edges"]

    # Calculate coordinates level by level
    levels = {}
    for n in nodes:
        lvl = n["level"]
        levels.setdefault(lvl, []).append(n)

    pos = {}
    max_w = max(len(nodes_at_lvl) for nodes_at_lvl in levels.values())

    for lvl, n_list in levels.items():
        k = len(n_list)
        for i, node in enumerate(n_list):
            x = (i + 1) / (k + 1) * 100
            y = -lvl * 50
            pos[node["id"]] = (x, y)

    edge_x = []
    edge_y = []
    for u, v in edges:
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    fig = go.Figure()
    if edge_x:
        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=2, color="#b5c0cb"),
            mode="lines",
            hoverinfo="none",
            showlegend=False
        ))

    node_x = [pos[n["id"]][0] for n in nodes]
    node_y = [pos[n["id"]][1] for n in nodes]
    node_text = [n["label"] for n in nodes]

    fig.add_trace(go.Scatter(
        x=node_x, y=node_y,
        mode="markers+text",
        text=node_text,
        textposition="middle center",
        textfont=dict(color="#1f3a5f", size=11, family="monospace"),
        marker=dict(
            size=36,
            color="#edf3f8",
            line=dict(width=2, color="#6d879f")
        ),
        hoverinfo="text",
        showlegend=False
    ))

    fig.update_layout(
        height=380,
        margin=dict(l=20, r=20, t=25, b=25),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor="#f8fafc",
        paper_bgcolor="#ffffff",
    )
    return fig

def render_complexity_plot():
    """Generates comparative Big-O growth curves."""
    n_vals = np.linspace(1, 40, 100)

    o_1 = np.ones_like(n_vals)
    o_log_n = np.log2(n_vals)
    o_n = n_vals
    o_n_log_n = n_vals * np.log2(n_vals)
    o_n2 = n_vals ** 2

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=n_vals, y=o_1, mode="lines", name="O(1) - Constant", line=dict(color="#2e7d32", width=2.5)))
    fig.add_trace(go.Scatter(x=n_vals, y=o_log_n, mode="lines", name="O(log n) - Logarithmic", line=dict(color="#0288d1", width=2.5)))
    fig.add_trace(go.Scatter(x=n_vals, y=o_n, mode="lines", name="O(n) - Linear", line=dict(color="#ed6c02", width=2.5)))
    fig.add_trace(go.Scatter(x=n_vals, y=o_n_log_n, mode="lines", name="O(n log n) - Linearithmic", line=dict(color="#9c27b0", width=2.5)))
    fig.add_trace(go.Scatter(x=n_vals, y=o_n2, mode="lines", name="O(n²) - Quadratic", line=dict(color="#d32f2f", width=2.5)))

    fig.update_layout(
        title="Theoretical Big-O Growth Rates vs Input Size (n)",
        xaxis_title="Input Size (n)",
        yaxis_title="Operations / Growth Units",
        yaxis=dict(range=[0, 250], showgrid=True, gridcolor="#e9edf3"),
        xaxis=dict(showgrid=True, gridcolor="#e9edf3"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=390,
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor="#f8fafc",
        paper_bgcolor="#ffffff",
    )
    return fig

def render_feature_importance_plot(feature_names, importances):
    """Renders horizontal bar chart of ML feature importances."""
    sorted_idx = np.argsort(importances)
    names = [feature_names[i].replace("_", " ").title() for i in sorted_idx]
    vals = [importances[i] * 100 for i in sorted_idx]

    fig = go.Figure(data=[
        go.Bar(
            y=names,
            x=vals,
            orientation="h",
            marker=dict(color="#1f3a5f"),
            text=[f"{v:.1f}%" for v in vals],
            textposition="outside"
        )
    ])
    fig.update_layout(
        title="ML Feature Importance (% contribution to algorithm choice)",
        xaxis_title="Importance (%)",
        height=340,
        margin=dict(l=140, r=40, t=40, b=30),
        xaxis=dict(range=[0, max(vals) * 1.25], showgrid=True, gridcolor="#e9edf3"),
        plot_bgcolor="#f8fafc",
        paper_bgcolor="#ffffff",
    )
    return fig

def render_confusion_matrix_plot(cm, classes):
    """Renders confusion matrix heatmap."""
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=classes,
        y=classes,
        colorscale="Blues",
        hoverongaps=False
    ))
    fig.update_layout(
        title="Confusion Matrix (Actual vs Predicted)",
        xaxis_title="Predicted Algorithm",
        yaxis_title="Actual Optimal Algorithm",
        height=450,
        margin=dict(l=80, r=20, t=40, b=80),
        xaxis=dict(tickangle=45),
        plot_bgcolor="#f8fafc",
        paper_bgcolor="#ffffff",
    )
    return fig
