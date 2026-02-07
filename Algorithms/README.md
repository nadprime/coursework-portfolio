# Algorithms

<div align="center">
  <strong>📊 Comprehensive Study of Algorithmic Techniques 📊</strong><br>
  <em>From fundamentals to advanced problem-solving patterns</em>
</div>

---

## 📖 Overview

This section contains in-depth implementations and analyses of fundamental and advanced algorithms. Each algorithm is implemented with detailed explanations, time/space complexity analysis, and practical applications.

## 🎯 Learning Objectives

- Master core algorithmic paradigms and design patterns
- Understand time and space complexity analysis
- Implement efficient solutions to classic problems
- Recognize when to apply specific algorithmic techniques

---

## 📚 Algorithm Categories

### 🔍 Searching Algorithms
- **Linear Search** - O(n) time, sequential scanning
- **Binary Search** - O(log n) time, divide and conquer
- **Jump Search** - O(√n) time, block jumping
- **Interpolation Search** - O(log log n) average for uniform data
- **Exponential Search** - Unbounded search with doubling

### 🔄 Sorting Algorithms
| Algorithm | Time (Best) | Time (Average) | Time (Worst) | Space | Stable |
|:----------|:------------|:---------------|:-------------|:------|:-------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n+k) | ✅ |

### 🌳 Tree Algorithms
- **Tree Traversals** - Inorder, Preorder, Postorder, Level Order
- **Binary Search Tree Operations** - Insert, Delete, Search
- **Tree Height & Depth** - Recursive and iterative approaches
- **Lowest Common Ancestor** - Multiple approaches
- **Tree Serialization** - Converting tree to/from string

### 📊 Graph Algorithms
- **Graph Traversals**
  - Breadth-First Search (BFS) - O(V+E)
  - Depth-First Search (DFS) - O(V+E)
- **Shortest Path**
  - Dijkstra's Algorithm - O((V+E) log V)
  - Bellman-Ford - O(VE)
  - Floyd-Warshall - O(V³)
- **Minimum Spanning Tree**
  - Kruskal's Algorithm - O(E log E)
  - Prim's Algorithm - O(E log V)
- **Topological Sorting** - O(V+E)
- **Cycle Detection** - Union-Find / DFS

### 💡 Dynamic Programming
- **Classic Problems**
  - Fibonacci Sequence
  - Climbing Stairs
  - Coin Change
  - Longest Common Subsequence
  - Longest Increasing Subsequence
  - Edit Distance (Levenshtein)
  - Knapsack Problem (0/1 and Unbounded)
  - Matrix Chain Multiplication
- **Patterns**
  - Memoization (Top-Down)
  - Tabulation (Bottom-Up)
  - State Optimization

### 🔙 Backtracking
- **N-Queens Problem**
- **Sudoku Solver**
- **Permutations & Combinations**
- **Subset Generation**
- **Word Search**
- **Palindrome Partitioning**

### ⚡ Greedy Algorithms
- **Activity Selection**
- **Huffman Coding**
- **Fractional Knapsack**
- **Job Sequencing**
- **Minimum Platforms**

### 🔢 Mathematical Algorithms
- **Prime Numbers** - Sieve of Eratosthenes
- **GCD & LCM** - Euclidean Algorithm
- **Modular Arithmetic** - Fast exponentiation
- **Combinatorics** - Permutations, combinations
- **Number Theory** - Factorization, divisors

### 🎯 String Algorithms
- **Pattern Matching**
  - Naive approach - O(nm)
  - KMP Algorithm - O(n+m)
  - Rabin-Karp - O(n+m) average
- **String Manipulation**
  - Palindrome checking
  - Anagram detection
  - String rotation
  - Longest palindrome

### 🔀 Bit Manipulation
- **Basic Operations** - AND, OR, XOR, NOT, shifts
- **Common Patterns**
  - Check/set/clear/toggle bits
  - Count set bits
  - Power of 2 check
  - XOR properties and tricks

### 🎲 Divide and Conquer
- **Merge Sort**
- **Quick Sort**
- **Binary Search**
- **Closest Pair of Points**
- **Strassen's Matrix Multiplication**

---

## 📊 Complexity Analysis Guide

### Time Complexity Hierarchy
```
O(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

### Common Time Complexities
| Complexity | Name | Example |
|:-----------|:-----|:--------|
| O(1) | Constant | Array access, hash table lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search, array traversal |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Bubble sort, nested loops |
| O(2ⁿ) | Exponential | Recursive Fibonacci |
| O(n!) | Factorial | Permutations |

---

## 🎓 Study Resources

### Books
- "Introduction to Algorithms" (CLRS)
- "Algorithm Design Manual" by Steven Skiena
- "Grokking Algorithms" by Aditya Bhargava
- "The Algorithm Design Manual" by Skiena

### Online Courses
- MIT 6.006 Introduction to Algorithms
- Princeton Algorithms (Coursera)
- UC Berkeley CS 61B

### Practice Platforms
- LeetCode (Algorithm patterns)
- HackerRank (Implementation focus)
- Codeforces (Competitive programming)

---

## 🗂️ Directory Structure

```
Algorithms/
├── Searching/
│   ├── binary_search.py
│   ├── linear_search.py
│   └── ternary_search.py
├── Sorting/
│   ├── bubble_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   └── heap_sort.py
├── Dynamic-Programming/
│   ├── fibonacci.py
│   ├── coin_change.py
│   ├── knapsack.py
│   └── lcs.py
├── Graph/
│   ├── bfs.py
│   ├── dfs.py
│   ├── dijkstra.py
│   └── topological_sort.py
├── Backtracking/
│   ├── n_queens.py
│   ├── sudoku_solver.py
│   └── permutations.py
└── README.md
```

---

## 📈 Progress Tracking

### Algorithms Implemented: 0/50
- [ ] Binary Search
- [ ] Merge Sort
- [ ] Quick Sort
- [ ] BFS & DFS
- [ ] Dijkstra's Algorithm
- [ ] Dynamic Programming classics

### Mastery Levels
- 🔴 **Not Started** - No implementation yet
- 🟡 **In Progress** - Basic understanding, needs practice
- 🟢 **Proficient** - Can implement independently
- ⭐ **Mastered** - Can teach others, optimize variants

---

## 🎯 Learning Path

### Foundation (Weeks 1-2)
1. Master time/space complexity analysis
2. Implement basic searching and sorting
3. Understand recursion fundamentals

### Intermediate (Weeks 3-6)
1. Tree and graph traversals
2. Introduction to dynamic programming
3. Common string algorithms

### Advanced (Weeks 7-12)
1. Advanced DP patterns
2. Complex graph algorithms
3. Optimization techniques

---

<div align="center">
  <em>"Understanding algorithms is understanding computer science"</em><br>
  <small>Last Updated: February 2026</small>
</div>
