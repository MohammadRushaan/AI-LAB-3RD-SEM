Beam Search is a heuristic search algorithm that optimizes memory and computation by pruning the search space. It functions as a bounded Breadth-First Search (BFS), keeping only a fixed number of the most promising paths at each level.

## Real-World Analogy: The Reality TV Talent Hunt
Imagine a singing competition where $1{,}000$ contestants audition in Round 1:
* Exhaustive BFS: The judges keep all $1{,}000$ singers, have each sing 5 more songs, resulting in an overwhelming $5{,}000$ performances in Round 2.
* Greedy Search (Best-First with width = 1): The judges keep only the single best singer from Round 1 and ignore everyone else, risking eliminating a late bloomer who could have become the superstar.
* Beam Search (Beam Width $k = 3$): The judges select only the Top 3 singers at the end of each round. In Round 2, only those 3 perform their next songs. From all their combined new performances, the judges again prune down to the Top 3.

## Core Logic & Key Concepts
* Beam Width ($k$): The maximum number of states/paths maintained at any given depth level.
    If $k = 1$, it behaves as Greedy Local Search.
    If $k = \infty$, it degrades into standard Breadth-First Search (BFS).
    
* Heuristic Evaluation ($h(n)$): An estimate of the remaining cost/distance from node $n$ to the goal. Lower values mean the node is closer to the objective.
* Pruning: Discarding all candidate paths outside the top-$k$ rank at the current depth to maintain a strictly bounded memory footprint.
* Incompleteness: Because it aggressively discards paths that do not look immediately promising, Beam Search is not complete (it might miss a valid path) and not optimal (it might not find the shortest path).

## Why and How the Algorithm Works
Standard graph search algorithms suffer from exponential state explosion: if a graph has a branching factor of $b$, exploring depth $d$ requires tracking $O(b^d)$ nodes.
Beam Search caps the number of nodes expanded at each level to $k$. Thus, at depth $d$, it expands at most $k \times b$ candidate states and retains only $k$. This reduces the time complexity to $O(k \cdot b \cdot d)$ and space complexity to $O(k \cdot d)$, making it suitable for large combinatorial search spaces like Natural Language Processing (NLP token generation), speech recognition, and large-scale graph pathfinding.

## Process flow

[Start Node]
      │
      ▼
 [Generate all valid successors]
      │
      ▼
 [Evaluate all successors using heuristic h(n)]
      │
      ▼
 [Sort candidates: lowest h(n) first]
      │
      ▼
 [Keep top-k candidates -> Form new Beam]
      │
   ┌──┴─────────────────────────┐
   │ Goal Found or Beam Empty?  │
   └──┬─────────────────────────┘
      │ No                      │ Yes
      │                         ▼
      └───────────────► [Return Goal Path / Terminate]

## Step-by-Step Code Flow & Data Structure Transitions

Consider a search on the following graph to find a path from $S$ to $G$ with Beam Width $k = 2$:

#### Graph Transitions
* $S \rightarrow A, B$
* $A \rightarrow C, G$
* $B \rightarrow C$

#### Heuristics
* $h(S) = 7$
* $h(A) = 6$
* $h(B) = 2$
* $h(C) = 1$
* $h(G) = 0$

---

### Initialization
* **`beam`**: `[(7, 'S', ['S'])]` *(Format: `(heuristic, current_node, path_history)`)*
* **`visited`**: `{'S'}`

### Level 1 Expansion
* **Pop items from `beam`:** Current state is `'S'`.
* **Generate successors:** `'A'` and `'B'`.
* **Add to candidate list:**
  * **Candidate 1:** `(6, 'A', ['S', 'A'])`
  * **Candidate 2:** `(2, 'B', ['S', 'B'])`
* **Sort candidates by heuristic:**
  * `[(2, 'B', ['S', 'B']), (6, 'A', ['S', 'A'])]`
* **Select top $k = 2$:**
  * **`beam`**: `[(2, 'B', ['S', 'B']), (6, 'A', ['S', 'A'])]`
  * **`visited`**: `{'S', 'A', 'B'}`


### Level 2 Expansion
* **Expand candidates currently in `beam`:**
  * **From `'B'`:** Generates neighbor `'C'` $\rightarrow$ `(1, 'C', ['S', 'B', 'C'])`
  * **From `'A'`:** Generates neighbors `'C'` *(already visited)* and `'G'` $\rightarrow$ `(0, 'G', ['S', 'A', 'G'])`
* **Aggregated candidates pool:**
  * `[(1, 'C', ['S', 'B', 'C']), (0, 'G', ['S', 'A', 'G'])]`
* **Sort candidates by heuristic:**
  * `[(0, 'G', ['S', 'A', 'G']), (1, 'C', ['S', 'B', 'C'])]`
* **Goal Check:** Top candidate contains the target goal `'G'`.
* **Terminate and Return Path:** `['S', 'A', 'G']`

**Beam Search** explores a graph or tree level by level, but at every single depth level, it strictly restricts the number of active paths to a fixed size $k$ (the **Beam Width**).

---

**Step-by-Step Breakdown of What Happens**

* **1. Initialization**
* The search starts at the root/start node.
* The `beam` list holds only the starting path: `[(h(start), start, [start])]`.


* **2. Expansion (Successor Generation)**
* For every path currently inside `beam`, the algorithm looks at its last node and identifies all valid, unvisited neighbors.
* It creates a new extended candidate path for each neighbor and pairs it with that neighbor's heuristic value $h(n)$ (distance to goal).


* **3. Evaluation and Pooling**
* All generated candidate paths from all current beam nodes are collected into a single pool (`candidates`).


* **4. Pruning (The Core Beam Filter)**
* The algorithm sorts the entire `candidates` list by heuristic value in ascending order (best/lowest $h(n)$ first).
* It retains only the top-$k$ paths and permanently discards the rest.
* The remaining $k$ paths become the new `beam` for the next level.


* **5. Termination**
* If any candidate in the current beam matches the target goal, search terminates and returns that path.
* If no unvisited successors exist and the beam becomes empty, search terminates with no valid path found.



---

**Visual Flow of a Single Step ($k = 2$)**

```
Current Beam (k=2):      [Node A]                [Node B]
                             │                       │
Generate Neighbors:      ┌───┴───┐               ┌───┴───┐
                        [C]     [D]             [E]     [F]
Heuristic Scores:      h=12     h=4             h=2     h=9
                         │       │               │       │
Combined Pool:          [C (12), D (4), E (2), F (9)]
                         │
Sort Ascending:         [E (2), D (4), F (9), C (12)]
                         │
Keep Top-2 (k=2):       [E (2), D (4)]  <-- Discards F and C
                         │
New Beam for Next Level: [Node E, Node D]

```

**Difference from Best-First Search (BFS)**

* **Greedy Best-First Search:** Keeps **every** visited branch in a single global priority queue (`open_list`). It never permanently deletes paths, meaning memory grows continually.
* **Beam Search:** Keeps only $k$ paths at each step. Anything outside the top-$k$ is deleted immediately, keeping memory usage constant per level.

## Application and Use cases:

**Natural Language Processing & Large Language Models (LLMs)**

* **Neural Machine Translation (NMT):** When translating across languages (e.g., English to French), the model predicts target sentences word-by-word. Beam Search keeps the top-$k$ partial translations at each token step, preventing greedy errors where early high-probability words produce disjointed full sentences.
* **Text Summarization & Generation:** Autoregressive models (like GPT and T5) use beam search during decoding to generate coherent, grammatically sound paragraphs and summaries instead of choosing single highest-probability tokens that lead to repetitive text.
* **Image Captioning:** Vision-language models (e.g., BLIP, ViT-GPT2) generate descriptive sentences for input images by maintaining candidate descriptions across successive vocabulary predictions.

**Speech & Signal Processing**

* **Automatic Speech Recognition (ASR):** Systems like Whisper or DeepSpeech translate acoustic waveforms into text. Because different phonemes sound identical in isolation, beam search tracks multiple phonetic and word combinations simultaneously until acoustic and language context resolves the correct transcription.
* **Optical Character Recognition (OCR):** Handwriting and degraded document recognition systems use beam search across character sequences, combining visual edge detections with statistical language dictionaries to decipher ambiguous letters.

**Robotics, Path Planning & Optimization**

* **Autonomous Navigation in Dynamic Environments:** Unmanned ground vehicles (UGVs) and drones use beam search for real-time trajectory rollout. It explores multi-step maneuver combinations (steer, brake, accelerate) while pruning high-risk or collision-prone paths to stay within strict onboard compute limits.
* **Robotic Arm Motion Planning:** When calculating multi-axis joint movements around obstacles in 3D space, beam search prunes high-torque or awkward trajectory angles while finding kinematic target poses.

**Computational Biology & Chemistry**

* **RNA Secondary Structure Prediction:** Finding minimum free energy conformations of RNA molecules involves exploring massive combinatorial folds. Beam search prunes high-energy conformations early, keeping plausible structural candidates.
* **De Novo Molecular Design & Drug Discovery:** Generative chemistry pipelines construct chemical SMILES strings or 3D molecular graphs step-by-step. Beam search prioritizes molecules showing high predicted binding affinity and drug-likeness while cutting structurally invalid compounds.

**Games & Decision Systems**

* **Combinatorial Game AI:** For strategy games like Chess, Go, or puzzle games (e.g., Sokoban), beam search acts as an evaluation-driven alternative to full minimax search when time per move is extremely constrained.
* **Syntax Parsing in Compilers:** Natural language parsers and ambiguous grammar compilers use beam search to evaluate alternative parse trees concurrently, resolving ambiguous syntactic structures.

---
## Critical Failsafes:

Critical failsafes prevent beam search from failing silently, entering infinite loops, running out of memory, or returning degraded outputs.

**1. Search Space & Graph Failsafes**

* **Cycle Detection & Visited State Tracking:**
* **Failure:** In cyclic graphs, paths loop endlessly back to previously seen nodes.
* **Failsafe:** Maintain a global `visited` set (for general graph search) or a path-specific visited check `if neighbor not in current_path` to prevent circular traversals.


* **Maximum Depth / Horizon Limit (`max_depth`):**
* **Failure:** If the goal node is unreachable due to early pruning or graph disconnection, the search runs indefinitely.
* **Failsafe:** Enforce a hard stopping depth:
```python
if current_depth > MAX_DEPTH:
    return "Search aborted: Maximum depth reached"

```
* **Empty Beam / Dead-End Handler:**
* **Failure:** If all candidates at level $L$ are dead ends or already visited, `candidates` becomes empty, causing `IndexError` or crashes when indexing.
* **Failsafe:** Explicitly guard against empty candidate pools:
```python
if not candidates:
    return None  # Gracefully terminate search

```
**2. Numeric & Heuristic Failsafes**

* **Missing / Infinite Heuristic Handling:**
* **Failure:** Looking up an unmapped node in the heuristic dictionary causes a `KeyError`, or `NaN` values corrupt sorting.
* **Failsafe:** Fall back safely using `heuristics.get(node, float('inf'))` and filter out non-finite values before sorting.


* **Log-Probability Underflow (Sequence Generation / NLP):**
* **Failure:** In probabilistic search (e.g., token decoding), multiplying many small probabilities $P(w_1) \times P(w_2) \dots \times P(w_n)$ causes floating-point underflow to `0.0`.
* **Failsafe:** Use log-probabilities and sum them instead:

$$\log P(W) = \sum_{t=1}^{T} \log P(w_t \mid w_{<t})$$

**3. Output Quality & Length Failsafes (NLP / Generation Models)**

* **Length Normalization / Penalty:**
* **Failure:** Beam search naturally favors shorter sequences because each added step adds a penalty or reduces cumulative probability.
* **Failsafe:** Normalize cumulative scores by path length:

$$\text{Score}(Y) = \frac{\text{LogProb}(Y)}{(\text{Length}(Y))^\alpha}$$



*(where $\alpha \in [0.6, 0.8]$ is a tuning parameter).*


* **Repetition & N-gram Blocking:**
* **Failure:** Autoregressive models frequently get trapped in repetitive loops (e.g., *"the the the"*).
* **Failsafe:** Enforce a no-repeat $n$-gram rule by setting the score of any candidate that creates a repeated 2-gram or 3-gram to $-\infty$.


* **Diverse Beam Search (Group Pruning):**
* **Failure:** All $k$ beams collapse into minor variations of the exact same path (e.g., differing by only one token).
* **Failsafe:** Divide $k$ beams into sub-groups and apply a diversity penalty against candidates that overlap heavily with other active groups.

---