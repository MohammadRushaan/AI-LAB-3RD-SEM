# Forward Chaining in Propositional Logic

## 1. Conceptual Foundation: Data-Driven Reasoning

Forward Chaining is a bottom-up, data-driven inference strategy. It begins with an initial set of known facts (ground truths already in the Knowledge Base) and moves forward along logical implication rules to derive new conclusions, repeating this cycle until a designated goal (query) is verified or no further facts can be derived.

- **Direction:** Facts $\longrightarrow$ Intermediate Conclusions $\longrightarrow$ Final Goal / Query.
- **Paradigm:** It answers the question: *"Given everything currently confirmed true, what new truths inevitably follow?"*
- **Core Rule of Inference:** It relies fundamentally on Modus Ponens (and its generalized form):

$$\frac{P, \quad P \implies Q}{Q}$$

When extended to multiple premises:

$$\frac{P_1, \quad P_2, \quad \dots, \quad P_k, \quad (P_1 \land P_2 \land \dots \land P_k \implies Q)}{Q}$$

---

## 2. Theoretical Constraint: Definite Clauses

Forward chaining operates on **definite clauses** (a specific subclass of Horn clauses).

A definite clause is a disjunction of literals with **exactly one positive literal**:

$$\neg P_1 \lor \neg P_2 \lor \dots \lor \neg P_k \lor Q$$

Using the logical equivalence $(\neg A \lor B) \equiv (A \implies B)$ and De Morgan’s Laws, this is rewritten as:

$$(P_1 \land P_2 \land \dots \land P_k) \implies Q$$

- **Premises (Body):** The conjunction of symbols $(P_1 \land \dots \land P_k)$ that must all be satisfied simultaneously.
- **Conclusion (Head):** The single positive literal $Q$ produced once all premises hold true.
- **Base Facts:** Represented as definite clauses with an empty body ($k = 0$), meaning $\text{True} \implies Q$, which simply asserts that $Q$ is unconditionally true.

> **Why this constraint?** Arbitrary formulas (like $A \lor B$, meaning "either A is true or B is true") do not tell us which literal is true, preventing deterministic forward propagation. Definite clauses guarantee that whenever the premises hold, the conclusion $Q$ is strictly and unambiguously derived.

---

## 3. Step-by-Step Algorithmic Mechanism

To make forward chaining run in linear time $O(N)$ (where $N$ is the total size of the knowledge base), the classic algorithm introduced by Dowling and Gallier uses three coordinating structures:

1. **`count` array/table:**
   - Tracks for each rule how many of its premises remain unproven.
   - Initialized to $\text{length}(\text{premises})$ for each rule.
2. **`inferred` table:**
   - A boolean hash map tracking which symbols have already been proven to avoid cyclic redundant computation.
3. **`agenda` (Queue):**
   - A queue holding newly discovered facts whose implications have not yet been propagated through the rule base.

```text
+-----------------------------------------------------------+
| 1. Initialize agenda with all known base facts            |
| 2. Initialize count[rule] = number of premises in rule    |
| 3. Set inferred[fact] = True for each base fact           |
+-----------------------------------------------------------+
                              |
                              v
             +--> [ Is agenda empty? ] -- YES --> Terminate: Query NOT entailed (False)
             |                |
             |               NO
             |                v
             |     [ Pop symbol 'P' from agenda ]
             |                |
             |       Is P == Query? -- YES -----> Terminate: Query Entailed (True)
             |                |
             |               NO
             |                v
             |     For each rule where P is in premises:
             |       - Decrement count[rule] by 1
             |       - If count[rule] == 0:
             |           * Let Q = conclusion of rule
             |           * If Q not in inferred:
             |               - Mark inferred[Q] = True
             +-------------- - Push Q onto agenda

```
## 4. Comprehensive Worked Example

Consider the following knowledge base:

- **Base Facts:**
  1. $A$
  2. $B$

- **Rule Base:**
  - $R_1: A \land B \implies C$
  - $R_2: C \land D \implies E$
  - $R_3: C \implies F$
  - $R_4: F \implies G$

- **Query ($\alpha$):** Prove $G$

### Initial State

- **`agenda`:** `[A, B]`
- **`inferred`:** `{A: True, B: True}`
- **`count`:**
  - $R_1$: `2` (needs $A, B$)
  - $R_2$: `2` (needs $C, D$)
  - $R_3$: `1` (needs $C$)
  - $R_4$: `1` (needs $F$)

### Iteration Trace

- **Iteration 1:**
  - Pop $A$ from agenda.
  - Check rules with $A$ in premises $\to R_1$.
  - Decrement $\text{count}[R_1]$ from $2 \to 1$.
  - Agenda remaining: `[B]`.

- **Iteration 2:**
  - Pop $B$ from agenda.
  - Check rules with $B$ in premises $\to R_1$.
  - Decrement $\text{count}[R_1]$ from $1 \to 0$.
  - All premises of $R_1$ are satisfied $\implies$ Fire $R_1$!
  - Derived conclusion: $C$.
  - Add $C$ to `inferred` and push onto agenda.
  - Agenda remaining: `[C]`.

- **Iteration 3:**
  - Pop $C$ from agenda.
  - Check rules with $C$ in premises $\to R_2, R_3$:
    - For $R_2$: Decrement $\text{count}[R_2]$ from $2 \to 1$ (still waiting on $D$).
    - For $R_3$: Decrement $\text{count}[R_3]$ from $1 \to 0$.
  - All premises of $R_3$ are satisfied $\implies$ Fire $R_3$!
  - Derived conclusion: $F$.
  - Add $F$ to `inferred` and push onto agenda.
  - Agenda remaining: `[F]`.

- **Iteration 4:**
  - Pop $F$ from agenda.
  - Check rules with $F$ in premises $\to R_4$.
  - Decrement $\text{count}[R_4]$ from $1 \to 0$.
  - All premises of $R_4$ are satisfied $\implies$ Fire $R_4$!
  - Derived conclusion: $G$.
  - Query check: $G == \text{Query}$.
  - **Termination:** $KB \models G$ is proven **True**.

---

## 5. Theoretical Properties

| Metric | Property | Explanation |
| :--- | :--- | :--- |
| **Soundness** | Yes (100% Sound) | Every inferred sentence is logically entailed because it applies Modus Ponens, which is truth-preserving. |
| **Completeness** | Yes (For Horn KBs) | If a definite clause $KB$ entails a proposition $\alpha$, forward chaining is guaranteed to derive it. |
| **Time Complexity** | $O(N)$ Linear | Every rule premise is checked a number of times proportional to the number of premises, and each fact is placed on the agenda at most once. |
| **Space Complexity** | $O(S)$ Linear | Storing `count`, `inferred`, and `agenda` requires memory directly proportional to the total number of rules and symbols $S$. |

---

## 6. Forward Chaining vs. Backward Chaining

- **Forward Chaining (Data-Driven):**
  - Starts from known facts and derives all possible consequences.
  - Best suited for situations where new information arrives asynchronously and continuous updates are required (e.g., sensor monitoring, alert systems, automated factory controls, financial fraud detection).

- **Backward Chaining (Goal-Driven):**
  - Starts from the query (goal) and looks backward through rules to find supporting facts (e.g., to prove $G$, need $F$; to prove $F$, need $C$, and so on).
  - Best suited for diagnostic queries, troubleshooting, and proof engines (e.g., Prolog, medical diagnostic tools) where only a specific hypothesis needs evaluation without computing unrelated consequences.