**Our core curriculum contains 129 unique problems.** Below is the entire list, organized by chapter and technique, followed by **16 targeted extensions** for additional coverage.

You’ve reported independently solving **100, 104, 509, and 1342**. That leaves **125 core problems without confirmed independent completion**, including problems we’ve already worked through together.

One boundary: **no checklist guarantees complete preparation for every DSA interview.** Our goal is broad technique coverage plus demonstrated ability to solve unfamiliar variations. LeetCode itself offers a 150-question comprehensive plan intended for three or more months; our sequence is personalized around your recursion restart and learning needs. 

**How we’ll use this list**

- **✓** = independently solved, as reported by you.
- Listed order is the teaching route within each technique; harder combinations can be deferred until their prerequisites are solid.
- Practice remains adaptive. We can skip a redundant exercise after independent success or add a targeted variation after a specific mistake.
- An explained or scaffolded solution is **not yet an independent solve**.

**1. Recursion fundamentals — 2 problems**

| Technique | Problems |
|---|---|
| Base case, smaller input, progress toward termination | **1342. Number of Steps to Reduce a Number to Zero ✓** |
| Multiple recursive calls, returning answers, repeated work | **509. Fibonacci Number ✓** |

Tree problems develop these foundations further. We revisit Fibonacci during DP without counting it twice.

**2. Binary trees — 18 problems**

| Technique | Problems |
|---|---|
| Return a subtree’s height | **104. Maximum Depth of Binary Tree ✓** |
| Modify child connections recursively | **226. Invert Binary Tree** |
| Compare corresponding nodes and entire structures | **100. Same Tree ✓** |
| Compare mirrored positions | **101. Symmetric Tree** |
| Pass a remaining target downward | **112. Path Sum** |
| Handle missing branches when minimizing | **111. Minimum Depth of Binary Tree** |
| Search for a candidate, then compare subtrees | **572. Subtree of Another Tree** |
| Carry a path value downward; add results upward | **129. Sum Root to Leaf Numbers** |
| Return multiple facts about a subtree | **110. Balanced Binary Tree** |
| Separate subtree height from the best complete path | **543. Diameter of Binary Tree — next** |
| Explicit DFS stack and traversal order | **144. Binary Tree Preorder Traversal** → **94. Binary Tree Inorder Traversal** |
| BFS with a queue and level boundaries | **102. Binary Tree Level Order Traversal** → **199. Binary Tree Right Side View** |
| Combine searches to locate a shared ancestor | **236. Lowest Common Ancestor of a Binary Tree** |
| Reconstruct structure from traversal information | **105. Construct Binary Tree from Preorder and Inorder Traversal** |
| Encode structure, including missing children | **297. Serialize and Deserialize Binary Tree** |
| Return an extendable path while tracking the best complete path | **124. Binary Tree Maximum Path Sum** |

We’ve discussed **226, 101, 112, 111, 572, 129, and 110**, but they still need independent reconstruction or verification. We won’t treat them as unseen, nor assume they’re mastered.

**3. Binary search trees — 5 problems**

| Technique | Problems |
|---|---|
| Use ordering to choose a branch | **700. Search in a Binary Search Tree** |
| Locate where ordered searches diverge | **235. Lowest Common Ancestor of a Binary Search Tree** |
| Carry ancestor constraints downward | **98. Validate Binary Search Tree** |
| Exploit sorted inorder traversal | **230. Kth Smallest Element in a BST** |
| Maintain traversal state across operations | **173. Binary Search Tree Iterator** |

**4. Arrays, strings, and hashing — 10 problems**

| Technique | Problems |
|---|---|
| Set membership | **217. Contains Duplicate** |
| Complement lookup | **1. Two Sum** |
| Frequency counting and canonical signatures | **242. Valid Anagram** → **49. Group Anagrams** |
| Prefix sums | **303. Range Sum Query — Immutable** |
| Prefix sums combined with frequency lookup | **560. Subarray Sum Equals K** |
| Combine prefix and suffix information | **238. Product of Array Except Self** |
| Identify sequence boundaries with a set | **128. Longest Consecutive Sequence** |
| Matrix boundaries and traversal | **54. Spiral Matrix** |
| In-place matrix transformation | **48. Rotate Image** |

**5. Two pointers and sliding windows — 12 problems**

| Technique | Problems |
|---|---|
| Opposite-end comparisons | **125. Valid Palindrome** |
| Move pointers using sorted order | **167. Two Sum II — Input Array Is Sorted** → **15. 3Sum** |
| Read/write pointers | **26. Remove Duplicates from Sorted Array** → **283. Move Zeroes** |
| Three-way partitioning | **75. Sort Colors** |
| Fixed-size window with counts | **567. Permutation in String** |
| Variable-size window with a validity invariant | **3. Longest Substring Without Repeating Characters** |
| Window with a modification budget | **424. Longest Repeating Character Replacement** |
| Minimum window satisfying required counts | **76. Minimum Window Substring** |
| Eliminate candidates using the limiting boundary | **11. Container With Most Water** |
| Reason about left and right boundaries | **42. Trapping Rain Water** |

For these, explaining **why a pointer can move safely** is part of solving the problem.

**6. Linked lists — 8 problems**

| Technique | Problems |
|---|---|
| Reverse pointers without losing the remaining list | **206. Reverse Linked List** |
| Merge with a dummy node and moving tail | **21. Merge Two Sorted Lists** |
| Fast/slow pointers | **876. Middle of the Linked List** |
| Detect a cycle | **141. Linked List Cycle** |
| Locate the cycle entrance | **142. Linked List Cycle II** |
| Maintain a fixed pointer gap | **19. Remove Nth Node From End of List** |
| Combine midpoint, reversal, and merging | **143. Reorder List** |
| Preserve object identity and cross-references | **138. Copy List with Random Pointer** |

**7. Stacks and queues — 8 problems**

| Technique | Problems |
|---|---|
| Match nested structure | **20. Valid Parentheses** |
| Evaluate expressions with an operand stack | **150. Evaluate Reverse Polish Notation** |
| Preserve nested parsing context | **394. Decode String** |
| Maintain auxiliary information per operation | **155. Min Stack** |
| Implement a queue with amortized analysis | **232. Implement Queue using Stacks** |
| Monotonic stack: resolve waiting elements | **739. Daily Temperatures** |
| Monotonic stack: determine maximal boundaries | **84. Largest Rectangle in Histogram** |
| Monotonic deque: retain useful window candidates | **239. Sliding Window Maximum** |

**8. Binary search — 7 problems**

| Technique | Problems |
|---|---|
| Maintain a valid search interval | **704. Binary Search** |
| Find an insertion boundary | **35. Search Insert Position** |
| Find first and last occurrences | **34. Find First and Last Position of Element in Sorted Array** |
| Identify the ordered portion of rotated data | **153. Find Minimum in Rotated Sorted Array** → **33. Search in Rotated Sorted Array** |
| Binary search over possible answers | **875. Koko Eating Bananas** → **1011. Capacity To Ship Packages Within D Days** |

**9. Heaps and priority queues — 6 problems**

| Technique | Problems |
|---|---|
| Maintain the largest `k` values in a stream | **703. Kth Largest Element in a Stream** |
| Select an order statistic | **215. Kth Largest Element in an Array** |
| Retain the best `k` candidates under a metric | **973. K Closest Points to Origin** |
| Merge multiple sorted streams | **23. Merge k Sorted Lists** |
| Maintain two ordered partitions | **295. Find Median from Data Stream** |
| Schedule by priority and availability | **621. Task Scheduler** |

For **215**, we’ll also study **quickselect**, including expected versus worst-case complexity. One problem can teach more than one technique.

**10. Intervals and greedy algorithms — 8 problems**

| Technique | Problems |
|---|---|
| Sort and merge overlapping intervals | **56. Merge Intervals** |
| Insert while preserving interval invariants | **57. Insert Interval** |
| Make a provably safe endpoint choice | **435. Non-overlapping Intervals** → **452. Minimum Number of Arrows to Burst Balloons** |
| Maintain the farthest reachable position | **55. Jump Game** |
| Advance a reachable frontier using the fewest jumps | **45. Jump Game II** |
| Determine when a segment can safely end | **763. Partition Labels** |
| Eliminate impossible starting candidates | **134. Gas Station** |

A greedy solution requires an explanation of **why the choice is safe**.

**11. Backtracking — 9 problems**

| Technique | Problems |
|---|---|
| Enumerate subsets | **78. Subsets** |
| Choose a fixed-size subset | **77. Combinations** |
| Track which choices are already used | **46. Permutations** |
| Allow repeated choices | **39. Combination Sum** |
| Control reuse and skip duplicate branches | **40. Combination Sum II** → **90. Subsets II** |
| Maintain validity while constructing a result | **22. Generate Parentheses** |
| Partition an input through recursive choices | **131. Palindrome Partitioning** |
| Track and restore visited state along one path | **79. Word Search** |

Here we explicitly practice **choose → explore → undo**, and when immutable arguments make undo unnecessary.

**12. Graphs — 11 problems**

| Technique | Problems |
|---|---|
| Traverse neighbors and mark visited nodes | **733. Flood Fill** |
| Find connected components | **200. Number of Islands** |
| Copy a graph while preserving identity | **133. Clone Graph** |
| Multi-source BFS | **994. Rotting Oranges** |
| Compute unweighted distances from multiple sources | **542. 01 Matrix** |
| Reverse the direction of a search | **417. Pacific Atlantic Water Flow** |
| Detect directed cycles and dependency feasibility | **207. Course Schedule** |
| Produce a topological ordering | **210. Course Schedule II** |
| Union-find for connectivity and cycle detection | **684. Redundant Connection** |
| Merge groups through shared identifiers | **721. Accounts Merge** |
| Dijkstra’s algorithm for nonnegative edge weights | **743. Network Delay Time** |

We’ll implement adjacency representations, DFS, BFS, and union-find—not merely recognize their names.

**13. Tries — 3 problems**

| Technique | Problems |
|---|---|
| Store and search shared prefixes | **208. Implement Trie (Prefix Tree)** |
| Branch during wildcard matching | **211. Design Add and Search Words Data Structure** |
| Combine prefix pruning with backtracking | **212. Word Search II** |

**14. Dynamic programming — 14 problems**

| Technique | Problems |
|---|---|
| Convert repeated recursive work into reusable state | **70. Climbing Stairs** |
| Choose or skip with an adjacency constraint | **198. House Robber** |
| Reduce a circular constraint to simpler cases | **213. House Robber II** |
| Minimize over choices | **322. Coin Change** |
| Determine whether a prefix can be constructed | **139. Word Break** |
| Count combinations; understand loop order | **518. Coin Change II** |
| Count paths over grid states | **62. Unique Paths** |
| Minimize cost over grid states | **64. Minimum Path Sum** |
| Compare prefixes of two sequences | **1143. Longest Common Subsequence** |
| Optimize operations on two prefixes | **72. Edit Distance** |
| Track the best subarray ending here | **53. Maximum Subarray** |
| Track both minimum and maximum states | **152. Maximum Product Subarray** |
| Optimize a subsequence ending at each position | **300. Longest Increasing Subsequence** |
| Capacity/subset-sum state | **416. Partition Equal Subset Sum** |

We derive **state → transition → base cases → evaluation order**. For **300**, we’ll compare the quadratic DP with the faster binary-search approach.

**15. Bit manipulation and arithmetic — 5 problems**

| Technique | Problems |
|---|---|
| XOR cancellation | **136. Single Number** |
| Inspect or remove set bits | **191. Number of 1 Bits** |
| Reuse results through a bit recurrence | **338. Counting Bits** |
| Exponentiation by squaring | **50. Pow(x, n)** |
| Detect cycles in a generated sequence | **202. Happy Number** |

**16. Data-structure design — 3 problems**

| Technique | Problems |
|---|---|
| Combine constant-time lookup and recency ordering | **146. LRU Cache** |
| Combine indexing, hashing, and swap-delete | **380. Insert Delete GetRandom O(1)** |
| Combine timestamped storage and binary search | **981. Time Based Key-Value Store** |

These test whether you can maintain several invariants across a sequence of operations.

**Targeted extensions — 16 additional problems**

These are **explicit additions to the earlier core plan**. They address additional techniques or provide stronger transfer checks. We’ll insert them into the appropriate chapters when useful, rather than automatically doing all of them after problem 129.

| Area | Problem | Purpose |
|---|---|---|
| Sorting | **912. Sort an Array** | Implement merge sort; explain stability, time, and auxiliary space |
| Frequency selection | **347. Top K Frequent Elements** | Compare heap and bucket approaches |
| Binary search | **74. Search a 2D Matrix** | Map a structured search space to an ordered index |
| Matrix state | **73. Set Matrix Zeroes** | Use the input itself to store markers |
| Linked lists | **2. Add Two Numbers** | Carry state while traversing two lists |
| Linked lists | **25. Reverse Nodes in k-Group** | Coordinate local reversal with global connections |
| Graph coloring | **785. Is Graph Bipartite?** | Assign and verify two-color constraints |
| Shortest paths | **1091. Shortest Path in Binary Matrix** | Single-source BFS with distance |
| Implicit graphs | **127. Word Ladder** | Generate neighbors from transformations |
| Minimum spanning trees | **1584. Min Cost to Connect All Points** | Learn Prim’s or Kruskal’s algorithm |
| Constrained shortest paths | **787. Cheapest Flights Within K Stops** | Recognize when node identity alone is insufficient state |
| Palindromes | **5. Longest Palindromic Substring** | Expand around centers |
| Palindromes | **647. Palindromic Substrings** | Transfer center expansion to counting |
| Optimization | **121. Best Time to Buy and Sell Stock** | Maintain the best earlier candidate |
| State-machine DP | **309. Best Time to Buy and Sell Stock with Cooldown** | Model holding, selling, and cooldown states |
| Interval DP | **312. Burst Balloons** | Advanced practice choosing the last action within an interval |

That gives us **129 core + 16 extensions = 145 named problems**, with no duplicates.

**What makes this interview preparation rather than a completed checklist**

Alongside these problems, we’ll practice:

- **Independent reconstruction:** no scaffold or solution visible.
- **Correctness reasoning:** explain the invariant, recursive promise, or greedy argument.
- **Complexity analysis:** include stack space, output space, expected complexity, and amortized cost where relevant.
- **Adversarial examples:** empty inputs, duplicates, missing branches, skewed trees, disconnected graphs, and boundary cases.
- **Unlabeled mixed attempts:** you choose the technique without the chapter title giving it away.
- **Follow-up changes:** modify a constraint and explain whether your approach still works.

Those mixed problems cannot all be preannounced without weakening their purpose. We’ll select them based on what you can solve independently.

**Your current position is Chapter 2, immediately before 543.** We’ll keep going from there, using the slower “define the function’s promise, then derive the cases” approach that helped you construct Balanced Tree.