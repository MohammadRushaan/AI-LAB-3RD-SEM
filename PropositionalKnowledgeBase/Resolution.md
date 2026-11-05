# Propositional Resolution & Refutation Theorem Proving

## 1. Conceptual Foundation: Proof by Refutation

Resolution is a theorem-proving technique based on **refutation** (proof by contradiction).

Instead of showing directly that a Knowledge Base entails a query sentence ($KB \models \alpha$), resolution shows that it is logically impossible for the knowledge base to be true while the query is false.

The mathematical principle behind it is:

$$KB \models \alpha \iff (KB \land \neg \alpha) \text{ is unsatisfiable}$$

- **Satisfiable:** There exists at least one model (truth assignment) that makes the statement true.
- **Unsatisfiable:** No possible truth assignment makes the statement true (it is an absolute contradiction, like $P \land \neg P \equiv \text{False}$).

To prove $KB \models \alpha$:

1. We assume the opposite of what we want to prove by asserting $\neg \alpha$.
2. We add $\neg \alpha$ into the knowledge base: $S = KB \cup \{\neg \alpha\}$.
3. We systematically combine clauses using the **Resolution Rule**.
4. If this process derives the empty clause ($\emptyset$ or $\{\}$), a contradiction is reached.
5. Because the base $KB$ is assumed consistent, the assumption $\neg \alpha$ must be false, proving that $KB \models \alpha$ is True.

---

## 2. The Propositional Resolution Rule

The resolution inference rule operates exclusively on disjunctive clauses (literals connected only by $\lor$).

### The Basic Rule (Unit Resolution)

Given a clause containing literal $P$ and another clause containing its complement $\neg P$:

$$\frac{P \lor A, \quad \neg P \lor B}{A \lor B}$$

- $P$ and $\neg P$ are called **complementary literals**.
- They cancel each other out.
- The resulting clause $(A \lor B)$ is called the **Resolvent**.

#### Why is this sound?

Consider the truth value of $P$:
- If $P$ is True, then $\neg P$ is False. For the second clause $(\neg P \lor B)$ to hold true, $B$ must be True.
- If $P$ is False, then for the first clause $(P \lor A)$ to hold true, $A$ must be True.

In all possible worlds, either $A$ is true or $B$ is true. Therefore, $(A \lor B)$ is guaranteed to be true.

### The Empty Clause ($\emptyset$)

When resolving two single-literal clauses that are direct negations of each other:

$$\frac{P, \quad \neg P}{\emptyset \quad \text{(Empty Clause / Contradiction)}}$$

Deriving the empty clause means that no truth value can satisfy the formula. The proof immediately terminates with True (entailment holds).

---

## 3. Canonical Form: Conjunctive Normal Form (CNF)

Resolution cannot directly process raw implication arrows ($\implies$) or biconditionals ($\iff$). Every sentence must first be converted into **Conjunctive Normal Form (CNF)** — an AND of ORs:

$$(C_1) \land (C_2) \land (C_3) \dots \land (C_m)$$

where each clause $C_i$ is a disjunction of literals $(L_{i1} \lor L_{i2} \lor \dots \lor L_{in})$.

### Standard Conversion Steps

1. **Eliminate Biconditionals ($\iff$):**
   $$A \iff B \equiv (A \implies B) \land (B \implies A)$$

2. **Eliminate Implications ($\implies$):**
   $$A \implies B \equiv \neg A \lor B$$

3. **Move Negations Inward (De Morgan's Laws & Double Negation):**
   $$\neg (A \land B) \equiv \neg A \lor \neg B$$
   $$\neg (A \lor B) \equiv \neg A \land \neg B$$
   $$\neg (\neg A) \equiv A$$

4. **Distribute $\lor$ over $\land$:**
   $$A \lor (B \land C) \equiv (A \lor B) \land (A \lor C)$$

5. **Flatten and Separate into Clauses:**
   $$(A \lor B) \land (C \lor D) \implies \text{Clauses: } \{A, B\} \text{ and } \{C, D\}$$

---

## 4. Step-by-Step Algorithmic Mechanism

```text
Input: Knowledge Base KB, Query α

1. Convert all sentences in KB to CNF clauses.
2. Negate the query: ¬α, convert to CNF, and add to the clause set.
3. Let Clauses = set of all CNF clauses.
4. Loop:
     a. For each pair of clauses C1, C2 in Clauses:
          i. Resolve C1 and C2 on any complementary literal.
         ii. If resolvent is empty (contradiction reached):
               RETURN True (KB entails α)
        iii. Otherwise, add non-trivial resolvents to NewClauses.
     b. If NewClauses is a subset of Clauses (no new clauses generated):
          RETURN False (KB does NOT entail α)
     c. Clauses = Clauses ∪ NewClauses

```
## 5. Detailed Worked Trace

Let's walk through an explicit, step-by-step resolution refutation on a weather domain:

- **Known Facts & Rules:**
  1. $\text{Cloudy}$
  2. $\text{Humid}$
  3. $\text{Cloudy} \land \text{Humid} \implies \text{Rainy}$
  4. $\text{Rainy} \implies \text{TakeUmbrella}$

- **Query ($\alpha$):** $\text{TakeUmbrella}$

### Step 1: Convert $KB$ and $\neg \alpha$ to CNF Clauses

- **Fact 1:** $\{\text{Cloudy}\}$
- **Fact 2:** $\{\text{Humid}\}$
- **Rule 1:** $\neg(\text{Cloudy} \land \text{Humid}) \lor \text{Rainy} \equiv \{\neg\text{Cloudy}, \neg\text{Humid}, \text{Rainy}\}$
- **Rule 2:** $\neg\text{Rainy} \lor \text{TakeUmbrella} \equiv \{\neg\text{Rainy}, \text{TakeUmbrella}\}$
- **Negated Query ($\neg \alpha$):** $\{\neg\text{TakeUmbrella}\}$

**Active Clause Pool:**
- $C_1: \{\text{Cloudy}\}$
- $C_2: \{\text{Humid}\}$
- $C_3: \{\neg\text{Cloudy}, \neg\text{Humid}, \text{Rainy}\}$
- $C_4: \{\neg\text{Rainy}, \text{TakeUmbrella}\}$
- $C_5: \{\neg\text{TakeUmbrella}\}$

### Step 2: Resolution Derivations

- **Derivation 1:**
  - Select $C_5: \{\neg\text{TakeUmbrella}\}$ and $C_4: \{\neg\text{Rainy}, \text{TakeUmbrella}\}$
  - Complementary literal: $\text{TakeUmbrella}$ and $\neg\text{TakeUmbrella}$
  - Resolvent $C_6$:
    $$C_6 = \{\neg\text{Rainy}\}$$

- **Derivation 2:**
  - Select $C_6: \{\neg\text{Rainy}\}$ and $C_3: \{\neg\text{Cloudy}, \neg\text{Humid}, \text{Rainy}\}$
  - Complementary literal: $\text{Rainy}$ and $\neg\text{Rainy}$
  - Resolvent $C_7$:
    $$C_7 = \{\neg\text{Cloudy}, \neg\text{Humid}\}$$

- **Derivation 3:**
  - Select $C_7: \{\neg\text{Cloudy}, \neg\text{Humid}\}$ and $C_1: \{\text{Cloudy}\}$
  - Complementary literal: $\text{Cloudy}$ and $\neg\text{Cloudy}$
  - Resolvent $C_8$:
    $$C_8 = \{\neg\text{Humid}\}$$

- **Derivation 4:**
  - Select $C_8: \{\neg\text{Humid}\}$ and $C_2: \{\text{Humid}\}$
  - Complementary literal: $\text{Humid}$ and $\neg\text{Humid}$
  - Resolvent $C_9$:
    $$C_9 = \emptyset \quad \text{(Empty Clause / Contradiction)}$$

Because the empty clause was derived, the set $\{KB \land \neg\text{TakeUmbrella}\}$ is unsatisfiable. Therefore, $KB \models \text{TakeUmbrella}$ is proven **True**.

---

## 6. Key Theoretical Properties

| Metric | Property | Technical Reasoning |
| :--- | :--- | :--- |
| **Soundness** | Yes | Resolution only infers valid logical consequences of the parent clauses. It never derives false assertions from true premises. |
| **Completeness** | Refutation Complete | If $KB \models \alpha$, resolution is guaranteed to derive the empty clause in finite steps. (Note: It cannot derive all true consequences directly, but it will always detect unsatisfiability). |
| **Expressiveness** | Full Propositional Logic | Unlike Forward Chaining, resolution does not require definite Horn clauses; it handles disjunctions ($\lor$), negations ($\neg$), and arbitrary boolean formulas. |
| **Complexity** | Exponential in worst case ($O(2^n)$) | The number of distinct clauses that can be generated is bounded by $3^n$ (each proposition can appear positive, negative, or be absent), making it exponential in the worst-case scenario. |