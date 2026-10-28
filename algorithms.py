"""
Algorithms Knowledge Base and Execution Simulator
Provides complexity information and step-by-step state generators
for Sorting, Searching, Graph algorithms, and Recurrence Relations.
"""

# Complexity and description metadata
SORTING_METADATA = {
    "Bubble Sort": {
        "best": "O(n)", "worst": "O(n²)", "space": "O(1)",
        "desc": "Repeatedly compares adjacent values and swaps them if they are in the wrong order.",
        "why": "Simple educational algorithm, but inefficient on large datasets."
    },
    "Selection Sort": {
        "best": "O(n²)", "worst": "O(n²)", "space": "O(1)",
        "desc": "Finds the smallest remaining value and places it at the next position.",
        "why": "Minimizes total number of memory write operations (at most O(n) swaps)."
    },
    "Insertion Sort": {
        "best": "O(n)", "worst": "O(n²)", "space": "O(1)",
        "desc": "Builds a sorted part by inserting each new value into its correct position.",
        "why": "Extremely fast for small datasets (n <= 20) and nearly sorted data with O(1) space."
    },
    "Merge Sort": {
        "best": "O(n log n)", "worst": "O(n log n)", "space": "O(n)",
        "desc": "Divides the array into smaller halves, then merges sorted halves.",
        "why": "Guaranteed O(n log n) worst-case time, highly stable, ideal for linked lists and large data."
    },
    "Quick Sort": {
        "best": "O(n log n)", "worst": "O(n²)", "space": "O(log n)",
        "desc": "Partitions values around a pivot and recursively sorts the two sides.",
        "why": "Typically the fastest in-place general-purpose sorting algorithm in practice."
    },
    "Heap Sort": {
        "best": "O(n log n)", "worst": "O(n log n)", "space": "O(1)",
        "desc": "Builds a heap and repeatedly moves the maximum value to the end.",
        "why": "Guarantees O(n log n) time while maintaining strict O(1) auxiliary space (in-place)."
    },
    "Shell Sort": {
        "best": "O(n log n)", "worst": "O(n²)", "space": "O(1)",
        "desc": "Uses gap-based insertion sorting to move values closer to their positions.",
        "why": "Performs well on medium-sized arrays without recursion overhead."
    },
    "Counting Sort": {
        "best": "O(n+k)", "worst": "O(n+k)", "space": "O(n+k)",
        "desc": "Counts how many times each integer occurs and rebuilds the sorted array.",
        "why": "Linear time O(n+k) when the range of key values k is small."
    },
    "Radix Sort": {
        "best": "O(nk)", "worst": "O(nk)", "space": "O(n+k)",
        "desc": "Sorts values digit by digit, starting with the least significant digit.",
        "why": "Linear time sorting for integers with fixed number of digits k."
    },
    "Bucket Sort": {
        "best": "O(n+k)", "worst": "O(n²)", "space": "O(n+k)",
        "desc": "Distributes values into buckets and sorts values inside each bucket.",
        "why": "Linear time average performance when data is uniformly distributed over a range."
    }
}

SEARCHING_METADATA = {
    "Linear Search": {
        "best": "O(1)", "worst": "O(n)", "space": "O(1)",
        "desc": "Checks values one by one and works even when data is unsorted.",
        "why": "The only standard searching algorithm that works directly on unsorted data without preparation."
    },
    "Binary Search": {
        "best": "O(1)", "worst": "O(log n)", "space": "O(1)",
        "desc": "Checks the middle of sorted data and removes half the search range each step.",
        "why": "Industry standard for sorted data, halving search space at each step in O(log n) time."
    },
    "Jump Search": {
        "best": "O(1)", "worst": "O(√n)", "space": "O(1)",
        "desc": "Jumps through blocks of size √n and then performs a short linear scan.",
        "why": "Traverses back fewer steps than binary search, suitable for systems where jumping back is costly."
    },
    "Interpolation Search": {
        "best": "O(1)", "worst": "O(n)", "space": "O(1)",
        "desc": "Estimates where target should be in sorted, uniformly distributed data.",
        "why": "Super-fast O(log log n) average time when values are uniformly distributed (like a phonebook)."
    },
    "Exponential Search": {
        "best": "O(1)", "worst": "O(log n)", "space": "O(1)",
        "desc": "Doubles the search range exponentially and then applies binary search.",
        "why": "Ideal for unbounded or infinite lists where the upper bound is unknown."
    },
    "Ternary Search": {
        "best": "O(1)", "worst": "O(log₃n)", "space": "O(1)",
        "desc": "Divides a sorted range into three parts using two midpoints.",
        "why": "Splits into thirds; often used for unimodal function optimization."
    },
    "Fibonacci Search": {
        "best": "O(1)", "worst": "O(log n)", "space": "O(1)",
        "desc": "Uses Fibonacci numbers to choose division positions in sorted data.",
        "why": "Uses only addition and subtraction instead of division/multiplication."
    }
}

GRAPH_METADATA = {
    "BFS": {
        "best": "O(V+E)", "worst": "O(V+E)", "space": "O(V)",
        "desc": "Visits a graph level by level using a queue.",
        "why": "Finds shortest paths in unweighted graphs and explores connected components level-by-level."
    },
    "DFS": {
        "best": "O(V+E)", "worst": "O(V+E)", "space": "O(V)",
        "desc": "Explores as deeply as possible before backtracking.",
        "why": "Essential for topological sorting, cycle detection, and strongly connected components."
    },
    "Dijkstra": {
        "best": "O((V+E)log V)", "worst": "O((V+E)log V)", "space": "O(V)",
        "desc": "Finds shortest paths from a source when edge weights are non-negative.",
        "why": "Most efficient single-source shortest path algorithm for non-negative edge weights."
    },
    "Bellman-Ford": {
        "best": "O(VE)", "worst": "O(VE)", "space": "O(V)",
        "desc": "Relaxes edges repeatedly and can handle negative edge weights.",
        "why": "Can handle negative edge weights and reliably detect negative weight cycles."
    },
    "Floyd-Warshall": {
        "best": "O(V³)", "worst": "O(V³)", "space": "O(V²)",
        "desc": "Finds shortest paths between every pair of vertices.",
        "why": "Dynamic programming approach for all-pairs shortest paths on dense graphs."
    },
    "Prim": {
        "best": "O(E log V)", "worst": "O(E log V)", "space": "O(V)",
        "desc": "Builds a minimum spanning tree by repeatedly choosing a cheap connecting edge.",
        "why": "Grows a single connected tree from a starting vertex; faster for dense graphs."
    },
    "Kruskal": {
        "best": "O(E log E)", "worst": "O(E log E)", "space": "O(V)",
        "desc": "Builds a minimum spanning tree by considering edges from smallest weight upward.",
        "why": "Processes edges globally using Disjoint Set Union (Union-Find); faster for sparse graphs."
    },
    "Topological Sort": {
        "best": "O(V+E)", "worst": "O(V+E)", "space": "O(V)",
        "desc": "Creates a dependency order for vertices in a directed acyclic graph.",
        "why": "Solves task scheduling, prerequisite resolution, and build pipelines in O(V+E)."
    }
}

RECURRENCE_METADATA = {
    "Master Theorem": {
        "desc": "Direct asymptotic bounds for divide-and-conquer recurrences T(n) = aT(n/b) + f(n).",
        "why": "Provides an immediate closed-form solution by comparing recursive work with non-recursive work."
    },
    "Substitution Method": {
        "desc": "Assume/guess a bound, substitute it into the recurrence, and prove by induction.",
        "why": "General method that works for any recurrence once a suitable mathematical guess is formed."
    },
    "Recursion Tree": {
        "desc": "Expand recursive calls into tree levels and sum the work performed across levels.",
        "why": "Visualizes work distribution across recursive levels and builds intuition for the asymptotic bound."
    },
    "Iteration Method": {
        "desc": "Repeatedly expand the recurrence step by step until the base case is reached.",
        "why": "Clear method for linear decrease recurrences like T(n) = T(n-1) + c to expose series summation."
    },
    "Characteristic Equation": {
        "desc": "Convert homogeneous or non-homogeneous linear recurrences into characteristic polynomial roots.",
        "why": "Standard analytical technique for linear recurrences with multiple prior terms (e.g., Fibonacci)."
    }
}

def get_algo_info(problem_type, algo_name):
    """Returns metadata for an algorithm."""
    if problem_type == "Sorting":
        return SORTING_METADATA.get(algo_name, {})
    elif problem_type == "Searching":
        return SEARCHING_METADATA.get(algo_name, {})
    elif problem_type == "Graph":
        return GRAPH_METADATA.get(algo_name, {})
    elif problem_type == "Recurrence Relation" or problem_type == "Recurrence":
        return RECURRENCE_METADATA.get(algo_name, {})
    return {}

# ----------------- SIMULATOR GENERATORS -----------------

def generate_sorting_steps(algo_name, arr):
    """Generates step-by-step states for sorting algorithms."""
    a = list(arr)[:14]
    steps = [{
        "a": list(a),
        "hi": [],
        "text": "Initial array",
        "description": "The algorithm starts with the values in their original order. Highlighted bars show elements currently being compared or swapped."
    }]

    if algo_name == "Bubble Sort":
        n = len(a)
        for i in range(n - 1):
            for j in range(n - i - 1):
                steps.append({
                    "a": list(a),
                    "hi": [j, j + 1],
                    "text": f"Compare {a[j]} and {a[j+1]}",
                    "description": f"Bubble Sort compares adjacent values. If {a[j]} > {a[j+1]}, they swap so the larger value moves to the right."
                })
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    steps.append({
                        "a": list(a),
                        "hi": [j, j + 1],
                        "text": f"Swap {a[j+1]} and {a[j]}",
                        "description": "The two highlighted bars are swapped because they were out of order."
                    })

    elif algo_name == "Selection Sort":
        n = len(a)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                steps.append({
                    "a": list(a),
                    "hi": [min_idx, j],
                    "text": f"Compare current min {a[min_idx]} with {a[j]}",
                    "description": "Selection Sort scans the unsorted partition to identify the index of the smallest remaining value."
                })
                if a[j] < a[min_idx]:
                    min_idx = j
            if min_idx != i:
                a[i], a[min_idx] = a[min_idx], a[i]
                steps.append({
                    "a": list(a),
                    "hi": [i, min_idx],
                    "text": f"Place minimum {a[i]} at index {i}",
                    "description": f"Smallest value {a[i]} is swapped into its permanent position at index {i}."
                })

    elif algo_name == "Insertion Sort":
        for i in range(1, len(a)):
            key = a[i]
            j = i - 1
            steps.append({
                "a": list(a),
                "hi": [i],
                "text": f"Take key {key} at index {i}",
                "description": f"Insertion Sort considers {key} and will shift larger sorted elements to the right to make room."
            })
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                steps.append({
                    "a": list(a),
                    "hi": [j, j + 1],
                    "text": f"Shift {a[j]} right",
                    "description": f"Value {a[j]} is larger than {key}, so it shifts right."
                })
                j -= 1
            a[j + 1] = key
            steps.append({
                "a": list(a),
                "hi": [j + 1],
                "text": f"Insert {key} at index {j+1}",
                "description": f"Inserted {key} into its sorted position."
            })

    elif algo_name == "Merge Sort":
        def merge_sort_helper(l, r):
            if r - l <= 1:
                return
            q = (l + r) // 2
            steps.append({
                "a": list(a),
                "hi": list(range(l, r)),
                "text": f"Divide partition [{l}..{r-1}]",
                "description": f"Merge Sort splits the subarray of length {r-l} into left [{l}..{q-1}] and right [{q}..{r-1}]."
            })
            merge_sort_helper(l, q)
            merge_sort_helper(q, r)

            L = a[l:q]
            R = a[q:r]
            i = j = 0
            merged = []
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    merged.append(L[i])
                    i += 1
                else:
                    merged.append(R[j])
                    j += 1
            merged.extend(L[i:])
            merged.extend(R[j:])
            for idx, val in enumerate(merged):
                a[l + idx] = val

            steps.append({
                "a": list(a),
                "hi": list(range(l, r)),
                "text": f"Merge sorted halves into [{l}..{r-1}]",
                "description": "Elements from both halves are compared and merged back in sorted order."
            })

        merge_sort_helper(0, len(a))

    elif algo_name == "Quick Sort":
        def quick_sort_helper(l, r):
            if l >= r:
                return
            pivot = a[r]
            i = l
            steps.append({
                "a": list(a),
                "hi": [r],
                "text": f"Choose pivot = {pivot}",
                "description": f"Quick Sort selects pivot {pivot} at index {r}. Values < pivot move left; values > pivot move right."
            })
            for j in range(l, r):
                steps.append({
                    "a": list(a),
                    "hi": [j, r],
                    "text": f"Compare {a[j]} with pivot {pivot}",
                    "description": f"Comparing element {a[j]} against pivot {pivot}."
                })
                if a[j] < pivot:
                    a[i], a[j] = a[j], a[i]
                    i += 1
            a[i], a[r] = a[r], a[i]
            steps.append({
                "a": list(a),
                "hi": [i],
                "text": f"Place pivot {pivot} at index {i}",
                "description": f"Pivot {pivot} is locked into its correct position {i}. Subarrays will be recursively sorted."
            })
            quick_sort_helper(l, i - 1)
            quick_sort_helper(i + 1, r)

        quick_sort_helper(0, len(a) - 1)

    elif algo_name == "Heap Sort":
        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and a[left] > a[largest]:
                largest = left
            if right < n and a[right] > a[largest]:
                largest = right
            if largest != i:
                a[i], a[largest] = a[largest], a[i]
                steps.append({
                    "a": list(a),
                    "hi": [i, largest],
                    "text": f"Heapify swap indices {i} and {largest}",
                    "description": "Max-heap property restored by moving larger child upward."
                })
                heapify(n, largest)

        n = len(a)
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
        for e in range(n - 1, 0, -1):
            a[0], a[e] = a[e], a[0]
            steps.append({
                "a": list(a),
                "hi": [0, e],
                "text": f"Extract max {a[e]} to index {e}",
                "description": "Root element of max heap moved to the sorted suffix of the array."
            })
            heapify(e, 0)
    else:
        # Generic fallback
        a.sort()
        steps.append({
            "a": list(a),
            "hi": list(range(len(a))),
            "text": f"{algo_name} transformation complete",
            "description": f"Visualized completed transformation using {algo_name}."
        })

    steps.append({
        "a": list(a),
        "hi": [],
        "text": "Array fully sorted",
        "description": f"Sorting with {algo_name} is complete. Elements are in non-decreasing order."
    })
    return steps

def generate_searching_steps(algo_name, arr, target):
    """Generates step-by-step search states."""
    a = list(arr)[:20]
    needs_sort = (algo_name != "Linear Search")

    steps = [{
        "a": list(a),
        "hi": [],
        "text": "Initial search array",
        "description": "Starting data array. Linear Search works on unsorted data; ordered search algorithms sort data first."
    }]

    if needs_sort:
        a.sort()
        steps.append({
            "a": list(a),
            "hi": list(range(len(a))),
            "text": "Sorted input array",
            "description": f"{algo_name} requires sorted data to perform ordered elimination."
        })

    if algo_name == "Linear Search":
        for i, val in enumerate(a):
            steps.append({
                "a": list(a),
                "hi": [i],
                "text": f"Check index {i}: value = {val}",
                "description": f"Comparing element at index {i} ({val}) with target {target}."
            })
            if val == target:
                steps.append({
                    "a": list(a),
                    "hi": [i],
                    "text": f"Found target {target} at index {i}!",
                    "description": f"Target value {target} was found at index {i}. Search terminates successfully."
                })
                return steps
    else:
        # Binary Search
        l = 0
        r = len(a) - 1
        while l <= r:
            m = (l + r) // 2
            steps.append({
                "a": list(a),
                "hi": list(range(l, r + 1)),
                "focus": [m],
                "text": f"Check mid index {m}: value = {a[m]} (range [{l}..{r}])",
                "description": f"Checking midpoint index {m} having value {a[m]}. Target is {target}."
            })
            if a[m] == target:
                steps.append({
                    "a": list(a),
                    "hi": [m],
                    "focus": [m],
                    "text": f"Target {target} found at mid index {m}!",
                    "description": f"Match found at index {m}! Binary search finished in O(log n) steps."
                })
                return steps
            elif a[m] < target:
                l = m + 1
            else:
                r = m - 1

    steps.append({
        "a": list(a),
        "hi": [],
        "text": f"Target {target} not present",
        "description": "The entire valid range was checked without finding the target."
    })
    return steps

def parse_edges(text):
    """Parses whitespace-separated edge list from text."""
    edges = []
    for line in text.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        u = parts[0]
        v = parts[1] if len(parts) > 1 else u
        w = float(parts[2]) if len(parts) > 2 else 1.0
        edges.append((u, v, w))
    return edges

def generate_graph_steps(algo_name, text):
    """Simulates BFS, DFS, Dijkstra, Bellman-Ford, Prim, Kruskal."""
    es = parse_edges(text)
    if not es:
        es = [("A", "B", 4.0), ("A", "C", 2.0), ("B", "C", 1.0), ("B", "D", 5.0), ("C", "D", 8.0)]

    nodes = sorted(list({u for u, v, w in es} | {v for u, v, w in es}))
    adj = {n: [] for n in nodes}
    for u, v, w in es:
        adj[u].append((v, w))
        adj[v].append((u, w))

    start_node = nodes[0]
    steps = [{
        "visited": [],
        "chosen": [],
        "cur": None,
        "dist": {},
        "text": "Initial graph loaded",
        "description": f"Graph initialized with {len(nodes)} vertices and {len(es)} edges."
    }]

    if algo_name in ("BFS", "DFS"):
        visited = []
        queue = [start_node]
        seen = set()

        while queue:
            u = queue.pop(0) if algo_name == "BFS" else queue.pop()
            if u in seen:
                continue
            seen.add(u)
            visited.append(u)
            steps.append({
                "visited": list(visited),
                "chosen": [],
                "cur": u,
                "dist": {},
                "text": f"Visit vertex {u}",
                "description": f"{algo_name} visits {u} and explores its adjacent neighbors."
            })
            for v, _ in adj[u]:
                if v not in seen:
                    queue.append(v)

    elif algo_name in ("Dijkstra", "Bellman-Ford"):
        dist = {n: float("inf") for n in nodes}
        dist[start_node] = 0
        used = []

        for _ in range(len(nodes)):
            # pick unvisited min dist
            unvisited = [n for n in nodes if n not in used]
            if not unvisited:
                break
            u = min(unvisited, key=lambda n: dist[n])
            if dist[u] == float("inf"):
                break
            used.append(u)
            steps.append({
                "visited": list(used),
                "chosen": [],
                "cur": u,
                "dist": dict(dist),
                "text": f"Process vertex {u} (current min dist = {dist[u]})",
                "description": f"{algo_name} evaluates outgoing edges from vertex {u} to relax paths."
            })
            for v, w in adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    steps.append({
                        "visited": list(used),
                        "chosen": [f"{u}-{v}"],
                        "cur": u,
                        "dist": dict(dist),
                        "text": f"Relax edge {u} -> {v}: new dist({v}) = {dist[v]}",
                        "description": f"Shorter path to {v} discovered via {u} with new weight {dist[v]}."
                    })

    elif algo_name == "Prim":
        used = {start_node}
        chosen = []
        while len(used) < len(nodes):
            cut_edges = []
            for u, v, w in es:
                if (u in used and v not in used) or (v in used and u not in used):
                    cut_edges.append((w, u, v))
            if not cut_edges:
                break
            cut_edges.sort()
            w, u, v = cut_edges[0]
            new_node = v if u in used else u
            used.add(new_node)
            chosen.append(f"{u}-{v}")
            steps.append({
                "visited": list(used),
                "chosen": list(chosen),
                "cur": new_node,
                "dist": {},
                "text": f"Select edge {u}-{v} (weight {w})",
                "description": f"Prim's algorithm connects vertex {new_node} into the MST using the lowest-weight cut edge."
            })

    elif algo_name == "Kruskal":
        parent = {n: n for n in nodes}
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        chosen = []
        sorted_edges = sorted(es, key=lambda x: x[2])
        for u, v, w in sorted_edges:
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_u] = root_v
                chosen.append(f"{u}-{v}")
                steps.append({
                    "visited": [],
                    "chosen": list(chosen),
                    "cur": None,
                    "dist": {},
                    "text": f"Add edge {u}-{v} (weight {w}) to MST",
                    "description": f"Edge {u}-{v} does not form a cycle, so it is merged into the spanning forest."
                })
            else:
                steps.append({
                    "visited": [],
                    "chosen": list(chosen),
                    "cur": None,
                    "dist": {},
                    "text": f"Skip edge {u}-{v} (would create cycle)",
                    "description": f"Vertices {u} and {v} are already connected in the same component. Skipped to prevent cycle."
                })
    else:
        steps.append({
            "visited": list(nodes),
            "chosen": [],
            "cur": None,
            "dist": {},
            "text": f"{algo_name} completed",
            "description": f"Finished simulation for {algo_name}."
        })

    steps.append({
        "visited": list(nodes),
        "chosen": steps[-1].get("chosen", []),
        "cur": None,
        "dist": steps[-1].get("dist", {}),
        "text": "Simulation finished",
        "description": "Algorithm execution has concluded. Step through previous states or examine final results."
    })

    return {"nodes": nodes, "edges": es, "steps": steps}
