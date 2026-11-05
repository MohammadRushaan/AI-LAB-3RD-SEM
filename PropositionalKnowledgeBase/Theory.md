# Propositional Logic & Automated Reasoning

## 1. The Core Architecture: Knowledge Base ($KB$)

In Artificial Intelligence, a **Knowledge Base ($KB$)** is a central repository of formal representations of facts about the world and relationships between them.

A knowledge-based agent operates via two primary interfaces:

- **TELL**: Adds new assertions (sentences) to the knowledge base.
- **ASK**: Queries whether a given hypothesis or goal sentence logically follows from what the agent currently knows.

The fundamental guarantee of an inference engine is **Entailment**:

$$KB \models \alpha$$

This means that in every possible world (or model) where all sentences in $KB$ evaluate to True, the query sentence $\alpha$ must also evaluate to True.

---

## 2. Syntax & Semantics of Propositional Logic

### A. Syntax (The Grammar)

- **Proposition Symbols (Atomic Sentences)**: Uppercase labels representing indivisible declarative statements that can either be true or false (e.g., $P$, $Q$, $\text{Rainy}$, $\text{WetGround}$).
- **Logical Connectives**:
  - **Negation** ($\neg$ or $\sim$): NOT ($\neg P$ is true if and only if $P$ is false).
  - **Conjunction** ($\land$): AND ($P \land Q$ is true if and only if both $P$ and $Q$ are true).
  - **Disjunction** ($\lor$): OR ($P \lor Q$ is true if at least one of $P$ or $Q$ is true).
  - **Implication** ($\implies$): IF...THEN ($P \implies Q$ is false only when $P$ is true and $Q$ is false; otherwise true).
  - **Biconditional** ($\iff$): IF AND ONLY IF ($P \iff Q$ is true when both have identical truth values).

### B. Semantics (Truth and Interpretation)

A **Model** $m$ is a complete assignment of truth values (True or False) to every atomic proposition symbol present in the universe. If a universe contains $n$ symbols, there exist exactly $2^n$ distinct models.

A sentence $\alpha$ is satisfied by a model $m$ if $\alpha$ evaluates to True under that assignment.

- $M(KB)$: The set of all models in which all sentences of $KB$ are true.
- $M(\alpha)$: The set of all models in which sentence $\alpha$ is true.

**Entailment Definition via Models:**

$$KB \models \alpha \iff M(KB) \subseteq M(\alpha)$$

If $KB$ is true, $\alpha$ is guaranteed to be true without contradiction.

---

## 3. Sentence Normal Forms for Automated Reasoning

Raw propositional formulas can have arbitrary nesting (parentheses, double implications, etc.). To run deterministic inference algorithms, sentences must be transformed into standardized canonical forms.

### A. Definite Clauses & Horn Clauses (Used by Forward Chaining)

- A **Horn Clause** is a disjunction of literals with at most one positive literal.
- A **Definite Clause** is a Horn clause with exactly one positive literal:

$$\neg P_1 \lor \neg P_2 \lor \dots \lor \neg P_k \lor Q$$

Applying De Morgan's laws and material implication transforms this directly into:

$$(P_1 \land P_2 \land \dots \land P_k) \implies Q$$

- $(P_1 \land \dots \land P_k)$ is called the **Premise** (or Body / Antecedents).
- $Q$ is called the **Conclusion** (or Head / Consequent).
- When $k = 0$, there are no premises: $\text{True} \implies Q$, which simply asserts an unconditional **Fact**: $Q$.

> **Why it matters**: Definite clauses allow polynomial-time (linear in practice) inference via Modus Ponens.

### B. Conjunctive Normal Form (CNF) (Used by Resolution)

A sentence is in **Conjunctive Normal Form (CNF)** if it is structured as a conjunction of one or more clauses, where each clause is a disjunction of literals:

$$\underbrace{(A \lor \neg B \lor C)}_{\text{Clause 1}} \land \underbrace{(\neg A \lor D)}_{\text{Clause 2}} \land \underbrace{(B)}_{\text{Clause 3}}$$

Every arbitrary propositional sentence can be converted to CNF using systematic equivalence laws:

1. **Eliminate biconditionals**: Replace $\alpha \iff \beta$ with $(\alpha \implies \beta) \land (\beta \implies \alpha)$.
2. **Eliminate implications**: Replace $\alpha \implies \beta$ with $\neg \alpha \lor \beta$.
3. **Push negations inward (De Morgan’s & Double Negation)**:
   - $\neg (\alpha \land \beta) \equiv \neg \alpha \lor \neg \beta$
   - $\neg (\alpha \lor \beta) \equiv \neg \alpha \land \neg \beta$
   - $\neg (\neg \alpha) \equiv \alpha$
4. **Distribute $\lor$ over $\land$**: Replace $\alpha \lor (\beta \land \gamma)$ with $(\alpha \lor \beta) \land (\alpha \lor \gamma)$.

---

## 4. The Two Inference Paradigms

```text
                           Knowledge Base (KB)
                                    |
         +--------------------------+--------------------------+
         |                                                     |
  [Horn / Definite Form]                                 [CNF Form]
         |                                                     |
         v                                                     v
  FORWARD CHAINING                                     RESOLUTION
  (Data-Driven Reasoning)                              (Refutation-Based Reasoning)
- Bottom-up derivation                               - Top-down contradiction search
- Starts with known base facts                       - Starts with KB + NOT(Query)
- Applies Modus Ponens repeatedly                    - Resolves complementary literals
- Terminates when goal is reached                    - Terminates when empty clause {}
    or no more rules fire                                (contradiction) is derived

```

### Approach 1: Forward Chaining (Data-Driven / Bottom-Up)

**Rule of Inference: Generalized Modus Ponens**

$$\frac{P_1, \quad P_2, \quad \dots, \quad P_k, \quad (P_1 \land P_2 \land \dots \land P_k \implies Q)}{Q}$$

**Mechanism:**

1. Place all known base facts into an **Agenda** (queue or set).
2. For each rule, track a counter representing how many of its premises remain unproven.
3. Dequeue a fact $P$, find all rules where $P$ appears as a premise, and decrement their counters.
4. If a rule's counter reaches $0$, all its premises are satisfied: fire the rule, derive its conclusion $Q$, and enqueue $Q$.
5. Repeat until the target query is added to the known facts or the agenda runs dry.

---

### Approach 2: Resolution (Proof by Refutation)

**Rule of Inference: Propositional Resolution**

$$\frac{\ell_1 \lor \dots \lor \ell_i \lor \dots \lor \ell_k, \quad m_1 \lor \dots \lor m_j \lor \dots \lor m_n}{\ell_1 \lor \dots \lor \ell_{i-1} \lor \ell_{i+1} \lor \dots \lor \ell_k \lor m_1 \lor \dots \lor m_{j-1} \lor m_{j+1} \lor \dots \lor m_n}$$

where $\ell_i$ and $m_j$ are complementary literals (i.e., $\ell_i = \neg m_j$).

**Mechanism (Refutation Completeness):**

1. To prove that $KB \models \alpha$, negate the query ($\neg \alpha$) and add it to the clauses of the $KB$.
2. The foundation rests on the **Refutation Principle**:

$$KB \models \alpha \iff (KB \land \neg \alpha) \text{ is unsatisfiable}$$

3. Resolve pairs of clauses containing complementary literals to produce new resolvents.
4. If resolving two unit complementary clauses (e.g., $\{P\}$ and $\{\neg P\}$) yields the empty clause ($\emptyset$ or $\{\}$), a mathematical contradiction has been forced.
5. The contradiction proves that $\neg \alpha$ cannot coexist with $KB$; therefore, $KB \models \alpha$ is decisively True.