# Data Structures

<div align="center">
  <strong>🏗️ Fundamental Building Blocks of Computer Science 🏗️</strong><br>
  <em>Master the art of organizing and managing data efficiently</em>
</div>

---

## 📖 Overview

This section contains comprehensive implementations and analyses of essential data structures. Each data structure is implemented from scratch with detailed explanations of operations, time/space complexities, and practical use cases.

## 🎯 Learning Objectives

- Understand the theory and implementation of fundamental data structures
- Master time and space complexity trade-offs
- Choose appropriate data structures for specific problems
- Implement custom data structures when needed

---

## 📚 Data Structure Categories

### 🔤 Linear Data Structures

#### **Arrays**
- **Description:** Contiguous memory storage with fixed/dynamic size
- **Operations:** Access O(1), Search O(n), Insert O(n), Delete O(n)
- **Use Cases:** Random access, cache-friendly operations
- **Variants:** Static arrays, dynamic arrays, circular arrays

#### **Linked Lists**
| Type | Description | Use Case |
|:-----|:------------|:---------|
| **Singly Linked** | One-way traversal | Stack, Queue implementation |
| **Doubly Linked** | Bidirectional traversal | Browser history, LRU cache |
| **Circular Linked** | Last node points to first | Round-robin scheduling |

**Operations:** 
- Access: O(n)
- Search: O(n)
- Insert (at head): O(1)
- Delete (at head): O(1)

#### **Stacks**
- **Principle:** Last In First Out (LIFO)
- **Operations:** Push O(1), Pop O(1), Peek O(1)
- **Applications:**
  - Function call management
  - Expression evaluation
  - Undo mechanisms
  - Backtracking algorithms
  - Browser back button

#### **Queues**
- **Principle:** First In First Out (FIFO)
- **Variants:**
  - Simple Queue
  - Circular Queue
  - Priority Queue
  - Deque (Double-ended queue)
- **Operations:** Enqueue O(1), Dequeue O(1)
- **Applications:**
  - Task scheduling
  - BFS traversal
  - Print spooling
  - Buffering

---

### 🌳 Tree Data Structures

#### **Binary Trees**
- **Properties:** Each node has at most 2 children
- **Types:**
  - Full Binary Tree - Every node has 0 or 2 children
  - Complete Binary Tree - All levels filled except possibly last
  - Perfect Binary Tree - All internal nodes have 2 children
  - Balanced Binary Tree - Height difference ≤ 1

#### **Binary Search Tree (BST)**
- **Property:** Left < Root < Right
- **Operations:**
  - Search: O(log n) average, O(n) worst
  - Insert: O(log n) average, O(n) worst
  - Delete: O(log n) average, O(n) worst
- **Applications:** Dictionaries, sorted data maintenance

#### **Balanced Trees**
| Type | Balance Criterion | Operations | Use Case |
|:-----|:------------------|:-----------|:---------|
| **AVL Tree** | Height diff ≤ 1 | O(log n) | Frequent searches |
| **Red-Black Tree** | Color properties | O(log n) | Frequent insertions |
| **B-Tree** | Multi-way search | O(log n) | Databases, filesystems |
| **B+ Tree** | Leaf-linked B-Tree | O(log n) | Database indexing |

#### **Heaps**
- **Types:** Min Heap, Max Heap
- **Properties:** Complete binary tree with heap property
- **Operations:**
  - Insert: O(log n)
  - Extract min/max: O(log n)
  - Get min/max: O(1)
- **Applications:**
  - Priority queues
  - Heap sort
  - Dijkstra's algorithm
  - K largest/smallest elements

#### **Tries (Prefix Trees)**
- **Description:** Tree for storing strings with common prefixes
- **Operations:**
  - Insert: O(L) where L is length
  - Search: O(L)
  - Delete: O(L)
- **Applications:**
  - Autocomplete
  - Spell checker
  - IP routing
  - Dictionary implementation

---

### 📊 Graph Data Structures

#### **Graph Representations**
| Representation | Space | Edge Lookup | Add Edge | Use Case |
|:---------------|:------|:------------|:---------|:---------|
| **Adjacency Matrix** | O(V²) | O(1) | O(1) | Dense graphs |
| **Adjacency List** | O(V+E) | O(V) | O(1) | Sparse graphs |
| **Edge List** | O(E) | O(E) | O(1) | Simple graphs |

#### **Graph Types**
- **Directed vs Undirected**
- **Weighted vs Unweighted**
- **Cyclic vs Acyclic**
- **Connected vs Disconnected**
- **Simple vs Multi-graph**

---

### 🗂️ Hash-Based Structures

#### **Hash Tables**
- **Principle:** Key → Hash Function → Index
- **Collision Resolution:**
  - Chaining (Linked lists at each bucket)
  - Open Addressing (Linear/Quadratic probing, Double hashing)
- **Operations:** O(1) average for insert, delete, search
- **Load Factor:** α = n/m (entries/buckets)
- **Applications:**
  - Dictionaries
  - Caching
  - Symbol tables
  - Database indexing

#### **Hash Sets**
- **Description:** Set implementation using hash table
- **Operations:** Add O(1), Remove O(1), Contains O(1)
- **Use Cases:** Uniqueness checking, fast lookups

#### **Hash Maps**
- **Description:** Key-value mapping using hash table
- **Operations:** Put O(1), Get O(1), Remove O(1)
- **Use Cases:** Caching, counting, grouping

---

### 🔗 Advanced Data Structures

#### **Disjoint Set (Union-Find)**
- **Operations:**
  - Find: O(α(n)) with path compression
  - Union: O(α(n)) with union by rank
- **Applications:**
  - Kruskal's MST algorithm
  - Network connectivity
  - Cycle detection

#### **Segment Trees**
- **Purpose:** Range queries on arrays
- **Operations:**
  - Build: O(n)
  - Query: O(log n)
  - Update: O(log n)
- **Use Cases:** Range sum/min/max queries

#### **Fenwick Tree (Binary Indexed Tree)**
- **Purpose:** Efficient prefix sum queries
- **Operations:**
  - Update: O(log n)
  - Query: O(log n)
- **Space:** O(n)
- **Use Cases:** Cumulative frequency tables

#### **LRU Cache**
- **Components:** Hash map + Doubly linked list
- **Operations:** Get O(1), Put O(1)
- **Use Cases:** Caching systems, memory management

---

## 📊 Comparison Matrix

### Time Complexity Overview
| Data Structure | Access | Search | Insert | Delete | Space |
|:---------------|:-------|:-------|:-------|:-------|:------|
| **Array** | O(1) | O(n) | O(n) | O(n) | O(n) |
| **Linked List** | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| **Stack** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Queue** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Hash Table** | N/A | O(1)† | O(1)† | O(1)† | O(n) |
| **BST** | O(log n)† | O(log n)† | O(log n)† | O(log n)† | O(n) |
| **AVL Tree** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **Heap** | O(n) | O(n) | O(log n) | O(log n) | O(n) |
| **Trie** | O(L) | O(L) | O(L) | O(L) | O(n×L) |

*With pointer to position  
†Average case

---

## 🎓 Study Resources

### Books
- "Data Structures and Algorithms in Python" by Goodrich
- "Introduction to Algorithms" (CLRS)
- "Cracking the Coding Interview" by McDowell

### Online Courses
- UC Berkeley CS 61B
- MIT 6.006 Introduction to Algorithms
- Princeton Algorithms (Coursera)

### Visualization Tools
- [VisuAlgo](https://visualgo.net/) - Interactive data structure visualizations
- [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/)

---

## 🗂️ Directory Structure

```
Data-Structures/
├── Linear/
│   ├── array.py
│   ├── linked_list.py
│   ├── stack.py
│   └── queue.py
├── Trees/
│   ├── binary_tree.py
│   ├── bst.py
│   ├── avl_tree.py
│   ├── heap.py
│   └── trie.py
├── Graphs/
│   ├── adjacency_list.py
│   ├── adjacency_matrix.py
│   └── graph_algorithms.py
├── Hash-Based/
│   ├── hash_table.py
│   ├── hash_set.py
│   └── hash_map.py
├── Advanced/
│   ├── union_find.py
│   ├── segment_tree.py
│   ├── fenwick_tree.py
│   └── lru_cache.py
└── README.md
```

---

## 📈 Progress Tracking

### Data Structures Implemented: 0/25
- [ ] Dynamic Array
- [ ] Linked List (Singly & Doubly)
- [ ] Stack & Queue
- [ ] Binary Search Tree
- [ ] Hash Table
- [ ] Heap
- [ ] Trie
- [ ] Graph representations

### Mastery Levels
- 🔴 **Novice** - Basic understanding, needs reference
- 🟡 **Intermediate** - Can implement with guidance
- 🟢 **Advanced** - Can implement from scratch
- ⭐ **Expert** - Deep understanding, can optimize

---

## 🎯 Learning Roadmap

### Phase 1: Fundamentals (Weeks 1-3)
- Arrays and linked lists
- Stacks and queues
- Basic hash tables

### Phase 2: Trees (Weeks 4-6)
- Binary trees and BST
- Tree traversals
- Balanced trees (AVL)
- Heaps and tries

### Phase 3: Graphs (Weeks 7-9)
- Graph representations
- Graph traversals
- Common graph algorithms

### Phase 4: Advanced (Weeks 10-12)
- Union-Find
- Segment trees
- Advanced applications
- Performance optimization

---

## 💡 When to Use Which?

### Array vs Linked List
- **Use Array:** Fixed size, random access needed, cache-friendly
- **Use Linked List:** Dynamic size, frequent insertions/deletions at ends

### Stack vs Queue
- **Use Stack:** LIFO needed, backtracking, function calls
- **Use Queue:** FIFO needed, BFS, task scheduling

### Array vs Hash Table
- **Use Array:** Small dataset, ordered data, predictable size
- **Use Hash Table:** Large dataset, fast lookups, key-value pairs

### BST vs Hash Table
- **Use BST:** Ordered data, range queries, in-order traversal
- **Use Hash Table:** Unordered data, fastest lookups, no range queries

---

<div align="center">
  <em>"Data structures are the scaffolding of software"</em><br>
  <small>Last Updated: February 2026</small>
</div>
