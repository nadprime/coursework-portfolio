# LeetCode Practice

<div align="center">
  <strong>💻 Systematic Problem-Solving Journey 💻</strong><br>
  <em>Building mastery through consistent practice and pattern recognition</em>
</div>

---

## 📊 Progress Dashboard

### Overall Statistics
| Metric | Count | Target | Progress |
|:-------|:------|:-------|:---------|
| **Total Solved** | 1 | 500 | 0.2% |
| **Easy** | 1 | 200 | 🟢 0.5% |
| **Medium** | 0 | 250 | 🟡 0% |
| **Hard** | 0 | 50 | 🔴 0% |
| **Daily Streak** | 1 days | ∞ | 🔥 |

### By Category
| Category | Solved | Total | Proficiency |
|:---------|:-------|:------|:------------|
| Array | 1 | 150 | 🟢 Beginner |
| String | 0 | 100 | ⚪ Not Started |
| Hash Table | 1 | 80 | 🟢 Beginner |
| Dynamic Programming | 0 | 120 | ⚪ Not Started |
| Tree | 0 | 80 | ⚪ Not Started |
| Graph | 0 | 70 | ⚪ Not Started |
| Linked List | 0 | 40 | ⚪ Not Started |

---

## 🎯 Learning Strategy

### Current Focus Areas
1. **Foundation Building** (Weeks 1-4)
   - Master arrays and strings
   - Hash table patterns
   - Two pointers technique
   - Sliding window

2. **Intermediate Patterns** (Weeks 5-12)
   - Dynamic programming
   - Tree traversals
   - Graph algorithms
   - Backtracking

3. **Advanced Topics** (Weeks 13+)
   - Complex DP patterns
   - Hard tree/graph problems
   - Optimization techniques

### Study Methodology
- **Daily Goal:** 2-3 problems (1 easy, 1-2 medium)
- **Weekend Deep Dive:** 1 hard problem with multiple approaches
- **Review Cycle:** Revisit problems after 1 week, 1 month
- **Pattern Recognition:** Document common patterns and techniques

---

## 📚 Problem Patterns & Templates

### 1️⃣ Array Patterns
#### Two Pointers
```python
# Template: Two Sum II (sorted array)
left, right = 0, len(arr) - 1
while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        return [left, right]
    elif current_sum < target:
        left += 1
    else:
        right -= 1
```

#### Sliding Window
```python
# Template: Maximum sum subarray of size k
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, len(arr)):
    window_sum = window_sum - arr[i-k] + arr[i]
    max_sum = max(max_sum, window_sum)
```

#### Fast & Slow Pointers
```python
# Template: Cycle detection
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # Cycle detected
```

### 2️⃣ Hash Table Patterns
#### Frequency Counter
```python
# Template: Character/element frequency
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
```

#### Complement/Pair Finding
```python
# Template: Two Sum
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

### 3️⃣ String Patterns
#### Palindrome Check
```python
# Template: Two-pointer palindrome
left, right = 0, len(s) - 1
while left < right:
    if s[left] != s[right]:
        return False
    left += 1
    right -= 1
return True
```

### 4️⃣ Dynamic Programming Patterns
#### 1D DP
```python
# Template: Climbing stairs
dp = [0] * (n + 1)
dp[0], dp[1] = 1, 1
for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
```

#### 2D DP
```python
# Template: Unique paths
dp = [[0] * n for _ in range(m)]
dp[0][0] = 1
for i in range(m):
    for j in range(n):
        if i > 0: dp[i][j] += dp[i-1][j]
        if j > 0: dp[i][j] += dp[i][j-1]
```

### 5️⃣ Tree Patterns
#### DFS Traversal
```python
# Template: Inorder traversal
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

#### BFS Traversal
```python
# Template: Level order traversal
from collections import deque
queue = deque([root])
result = []
while queue:
    level = []
    for _ in range(len(queue)):
        node = queue.popleft()
        level.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    result.append(level)
```

### 6️⃣ Graph Patterns
#### DFS
```python
# Template: Graph DFS
def dfs(node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)
```

#### BFS
```python
# Template: Graph BFS
from collections import deque
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

---

## 🗂️ Problem Organization

### By Difficulty
```
Leetcode/
├── Easy/
│   ├── 001-two-sum.py
│   └── 001-two-sum.md
├── Medium/
│   └── [problems]
├── Hard/
│   └── [problems]
└── README.md
```

### By Topic
- **Arrays** - Two pointers, sliding window, prefix sum
- **Strings** - Palindrome, anagram, pattern matching
- **Linked Lists** - Fast/slow pointers, reversal, dummy nodes
- **Trees** - Traversals, BST properties, recursion
- **Graphs** - BFS, DFS, shortest path, topological sort
- **Dynamic Programming** - 1D/2D DP, optimization
- **Backtracking** - Permutations, combinations, subsets
- **Hash Tables** - Frequency counting, complement finding

---

## 📈 Problem List

### Easy Problems (1/200)
| # | Title | Topics | Status | Date | Notes |
|:--|:------|:-------|:-------|:-----|:------|
| 1 | [Two Sum](./Python/01-two-sum.md) | Array, Hash Table | ✅ | 2026-02-08 | Hash map pattern |
| 20 | Valid Parentheses | Stack, String | ⬜ | - | - |
| 21 | Merge Two Sorted Lists | Linked List | ⬜ | - | - |
| 121 | Best Time to Buy and Sell Stock | Array, DP | ⬜ | - | - |
| 125 | Valid Palindrome | String, Two Pointers | ⬜ | - | - |

### Medium Problems (0/250)
| # | Title | Topics | Status | Date | Notes |
|:--|:------|:-------|:-------|:-----|:------|
| 3 | Longest Substring Without Repeating Characters | String, Sliding Window | ⬜ | - | - |
| 15 | 3Sum | Array, Two Pointers | ⬜ | - | - |
| 200 | Number of Islands | Graph, BFS, DFS | ⬜ | - | - |
| 322 | Coin Change | DP | ⬜ | - | - |

### Hard Problems (0/50)
| # | Title | Topics | Status | Date | Notes |
|:--|:------|:-------|:-------|:-----|:------|
| 4 | Median of Two Sorted Arrays | Binary Search | ⬜ | - | - |
| 42 | Trapping Rain Water | Two Pointers, Stack | ⬜ | - | - |

---

## 🎓 Must-Do Problem Lists

### Top 75 LeetCode Questions (Blind 75)
Essential problems covering all major patterns and data structures.

**Arrays & Hashing**
- [ ] 1. Two Sum
- [ ] 217. Contains Duplicate
- [ ] 242. Valid Anagram
- [ ] 49. Group Anagrams
- [ ] 347. Top K Frequent Elements

**Two Pointers**
- [ ] 125. Valid Palindrome
- [ ] 15. 3Sum
- [ ] 11. Container With Most Water

**Sliding Window**
- [ ] 3. Longest Substring Without Repeating Characters
- [ ] 424. Longest Repeating Character Replacement

**Stack**
- [ ] 20. Valid Parentheses
- [ ] 155. Min Stack

**Binary Search**
- [ ] 153. Find Minimum in Rotated Sorted Array
- [ ] 33. Search in Rotated Sorted Array

**Linked List**
- [ ] 206. Reverse Linked List
- [ ] 141. Linked List Cycle
- [ ] 21. Merge Two Sorted Lists

**Trees**
- [ ] 104. Maximum Depth of Binary Tree
- [ ] 100. Same Tree
- [ ] 226. Invert Binary Tree
- [ ] 102. Binary Tree Level Order Traversal

**Dynamic Programming**
- [ ] 70. Climbing Stairs
- [ ] 198. House Robber
- [ ] 322. Coin Change
- [ ] 300. Longest Increasing Subsequence

**Graphs**
- [ ] 133. Clone Graph
- [ ] 200. Number of Islands
- [ ] 417. Pacific Atlantic Water Flow

---

## 📝 Learning Notes

### Key Insights
- **Pattern Recognition is Key:** Most problems follow 10-15 common patterns
- **Complexity Analysis:** Always analyze time/space before coding
- **Edge Cases:** Empty input, single element, all same elements
- **Multiple Approaches:** Often trade-off between time and space

### Common Mistakes to Avoid
- Not considering edge cases
- Poor variable naming
- Inefficient brute force when pattern exists
- Not testing with examples before submitting

### Problem-Solving Framework
1. **Understand** - Read carefully, identify constraints
2. **Plan** - Recognize pattern, choose approach
3. **Implement** - Write clean, readable code
4. **Test** - Run through examples and edge cases
5. **Optimize** - Consider time/space improvements
6. **Review** - Learn from optimal solution

---

## 🏆 Milestones & Goals

### Short-term Goals (3 months)
- [ ] Solve 150 problems (50 easy, 90 medium, 10 hard)
- [ ] Complete Blind 75 list
- [ ] Master array and string patterns
- [ ] Build strong DP foundation

### Long-term Goals (1 year)
- [ ] Solve 500+ problems
- [ ] Consistently solve medium in <30 minutes
- [ ] Solve 1-2 hard problems weekly
- [ ] Prepare for technical interviews

### Target Companies Practice
- [ ] Google Interview Problems
- [ ] Meta/Facebook Problems
- [ ] Amazon Leadership Principles
- [ ] Microsoft Patterns

---

## 📊 Weekly Review Template

### Week [Number]: [Date Range]
- **Problems Solved:** X (X easy, X medium, X hard)
- **Time Invested:** X hours
- **Patterns Learned:** [List patterns]
- **Challenges Faced:** [Difficulties encountered]
- **Key Takeaways:** [Lessons learned]
- **Next Week Focus:** [Areas to improve]

---

## 🔗 Resources

### Official Resources
- [LeetCode](https://leetcode.com)
- [LeetCode Discuss](https://leetcode.com/discuss/)
- [LeetCode Patterns](https://seanprashad.com/leetcode-patterns/)

### Study Guides
- NeetCode 150 (curated list)
- Grokking the Coding Interview
- Elements of Programming Interviews

### Community
- r/leetcode
- LeetCode Discord
- YouTube channels (NeetCode, Tech With Tim)

---

<div align="center">
  <em>"Consistency beats intensity. One problem a day keeps the interview anxiety away."</em><br>
  <small>Last Updated: February 2026</small>
</div>
