## Example n=4:

### Phase 1: Exploring Branch with Queen at $(0, 0)$

#### Step 1: Place Queen at $(0, 0)$
* `backtrack(0)` tests column $c = 0$.
* Sets are completely empty, so $(0, 0)$ is safe.
* The queen is placed, updating $\text{cols} = \{0\}$, $\text{diag1} = \{0\}$, $\text{diag2} = \{0\}$.
* Next call: `backtrack(1)`.

**Row 1 Column Checks ($c = 0, 1$):**
* $c = 0$: Pruned because column $0$ is in `cols`.
* $c = 1$: Pruned because $r - c = 1 - 1 = 0$, which is in `diag1` (diagonal clash with $(0, 0)$).

#### Step 2: Place Queen at $(1, 2)$
* $c = 2$: Safe ($2 \notin \text{cols}$, $1 - 2 = -1 \notin \text{diag1}$, $1 + 2 = 3 \notin \text{diag2}$).
* Queen placed at $(1, 2)$. Next call: `backtrack(2)`.

**Row 2 Dead End ($c = 0, 1, 2, 3$):**
* $c = 0$: Column collision with $(0, 0)$.
* $c = 1$: Diagonal collision with $(1, 2)$ since $2 + 1 = 3 \in \text{diag2}$.
* $c = 2$: Column collision with $(1, 2)$.
* $c = 3$: Diagonal collision with $(1, 2)$ since $2 - 3 = -1 \in \text{diag1}$.
* Every column in row 2 fails. The loop terminates, triggering a backtrack.

#### Step 3: Backtrack from $(1, 2)$
* Removes queen from $(1, 2)$ and frees its column and diagonal values from tracking sets.
* Row 1 advances its loop to test $c = 3$.

#### Step 4: Place Queen at $(1, 3)$
* Safe ($3 \notin \text{cols}$, $1 - 3 = -2 \notin \text{diag1}$, $1 + 3 = 4 \notin \text{diag2}$).
* Queen placed at $(1, 3)$. Next call: `backtrack(2)`.

#### Step 5: Place Queen at $(2, 1)$
* Row 2 tests $c = 0$: Pruned ($0 \in \text{cols}$).
* Tests $c = 1$: Safe ($1 \notin \text{cols}$, $2 - 1 = 1 \notin \text{diag1}$, $2 + 1 = 3 \notin \text{diag2}$).
* Queen placed at $(2, 1)$. Next call: `backtrack(3)`.

**Row 3 Dead End ($c = 0, 1, 2, 3$):**
* $c = 0$: In `cols`.
* $c = 1$: In `cols`.
* $c = 2$: Diagonal clash with $(1, 3)$ ($3 - 2 = 1 \in \text{diag1}$) and $(2, 1)$ ($3 + 2 = 5$, safe, but $3 - 2 = 1$).
* $c = 3$: In `cols`.
* No square in row 3 is safe. Loop terminates; unwinding begins.

#### Step 6: Backtrack from $(2, 1)$
* Pulls queen off $(2, 1)$. Row 2 tests remaining columns: $c = 2$ (clashes diagonally with $(1, 3)$) and $c = 3$ (column clash). Row 2 loop ends.

#### Step 7: Backtrack from $(1, 3)$
* Pulls queen off $(1, 3)$. Row 1 has exhausted all columns ($0, 1, 2, 3$). Row 1 loop ends.

#### Step 8: Backtrack from $(0, 0)$
* Pulls queen off $(0, 0)$. Entire $(0, 0)$ subtree yielded 0 solutions.
* Row 0 loop advances to $c = 1$.

---

### Phase 2: Finding Solution #1 via $(0, 1)$

#### Step 9: Place Queen at $(0, 1)$
* Column 1 is open. Queen placed. Next call: `backtrack(1)`.

**Row 1 Checks ($c = 0, 1, 2$):**
* $c = 0$: Diagonal clash with $(0, 1)$ ($1 + 0 = 1$).
* $c = 1$: Column clash.
* $c = 2$: Diagonal clash with $(0, 1)$ ($1 - 2 = -1$).

#### Step 10: Place Queen at $(1, 3)$
* $c = 3$: Completely safe. Queen placed. Next call: `backtrack(2)`.

#### Step 11: Place Queen at $(2, 0)$
* $c = 0$: Safe ($0 \notin \text{cols}$, $2 - 0 = 2 \notin \text{diag1}$, $2 + 0 = 2 \notin \text{diag2}$).
* Queen placed at $(2, 0)$. Next call: `backtrack(3)`.

#### Step 12: Place Queen at $(3, 2)$
* Row 3 tests $c = 0$ (column clash), $c = 1$ (diagonal clash with $(2, 0)$).
* $c = 2$: Safe ($2 \notin \text{cols}$, $3 - 2 = 1 \notin \text{diag1}$, $3 + 2 = 5 \notin \text{diag2}$).
* Queen placed at $(3, 2)$. Next call: `backtrack(4)`.

> **FOUND SOLUTION #1:**  
> Base case triggered ($r = 4 = n$). Board is saved and printed. Function returns.

#### Step 13: Backtrack from $(3, 2)$
* Removes queen from $(3, 2)$. Row 3 tests $c = 3$ (column clash). Row 3 finishes.

#### Step 14: Backtrack from $(2, 0)$
* Removes queen from $(2, 0)$. Row 2 tests remaining columns ($1, 2, 3$); all are blocked. Row 2 finishes.

#### Step 15: Backtrack from $(1, 3)$
* Removes queen from $(1, 3)$. Row 1 has completed all columns. Row 1 finishes.

#### Step 16: Backtrack from $(0, 1)$
* Removes queen from $(0, 1)$. Row 0 loop advances to $c = 2$.

---

### Phase 3: Finding Solution #2 via $(0, 2)$

#### Step 17: Place Queen at $(0, 2)$
* Placed at $(0, 2)$. Next call: `backtrack(1)`.

#### Step 18: Place Queen at $(1, 0)$
* $c = 0$: Safe ($0 \notin \text{cols}$, $1 - 0 = 1 \notin \text{diag1}$, $1 + 0 = 1 \neq 2$).
* Placed at $(1, 0)$. Next call: `backtrack(2)`.

**Row 2 Checks ($c = 0, 1, 2$):**
* $c = 0$: Column clash.
* $c = 1$: Diagonal clash with $(1, 0)$ ($2 - 1 = 1$).
* $c = 2$: Column clash with $(0, 2)$.

#### Step 19: Place Queen at $(2, 3)$
* $c = 3$: Safe. Queen placed at $(2, 3)$. Next call: `backtrack(3)`.

#### Step 20: Place Queen at $(3, 1)$
* $c = 0$ (column clash).
* $c = 1$: Safe ($1 \notin \text{cols}$, $3 - 1 = 2 \notin \text{diag1}$, $3 + 1 = 4 \notin \text{diag2}$).
* Queen placed at $(3, 1)$. Next call: `backtrack(4)`.

> **FOUND SOLUTION #2:**  
> Base case triggered ($r = 4 = n$). Board configuration saved and displayed.

#### Steps 21 to 24: Unwinding Backtracks
* **Step 21:** Backtrack from $(3, 1)$—Row 3 finishes.
* **Step 22:** Backtrack from $(2, 3)$—Row 2 has no other valid columns left.
* **Step 23:** Backtrack from $(1, 0)$—Row 1 checks $c = 1, 2, 3$ (all blocked by diagonals/columns).
* **Step 24:** Backtrack from $(0, 2)$—Row 0 advances to the final column $c = 3$.

---

### Phase 4: Exploring Branch with Queen at $(0, 3)$

#### Step 25: Place Queen at $(0, 3)$
* Placed at $(0, 3)$. Next call: `backtrack(1)`.

#### Step 26: Place Queen at $(1, 0)$
* $c = 0$: Safe ($0 \notin \text{cols}$, $1 - 0 = 1$, $1 + 0 = 1 \neq 3$).
* Placed at $(1, 0)$. Next call: `backtrack(2)`.

#### Step 27: Place Queen at $(2, 2)$
* $c = 0$: Column clash.
* $c = 1$: Diagonal clash with $(1, 0)$ ($2 - 1 = 1$).
* $c = 2$: Safe. Placed at $(2, 2)$. Next call: `backtrack(3)`.

**Row 3 Checks:**
* Columns $0, 1, 2, 3$ are all blocked (e.g., column $0$ by $(1, 0)$, column $1$ by $(2, 2)$, column $2$ by $(2, 2)$, column $3$ by $(0, 3)$).
* Dead end reached.

#### Step 28: Backtrack from $(2, 2)$
* Removes queen from $(2, 2)$. Row 2 tests $c = 3$ (column clash). Row 2 ends.

#### Step 29: Backtrack from $(1, 0)$
* Removes queen from $(1, 0)$. Row 1 loop advances to $c = 1$.

#### Step 30: Place Queen at $(1, 1)$
* Safe ($1 \notin \text{cols}$, $1 - 1 = 0 \notin \text{diag1}$, $1 + 1 = 2 \neq 3$).
* Placed at $(1, 1)$. Next call: `backtrack(2)`.

**Row 2 Dead End:**
* All squares in Row 2 are threatened by $(0, 3)$ and $(1, 1)$. No queen can be placed.

#### Step 31: Backtrack from $(1, 1)$
* Removes queen from $(1, 1)$. Row 1 tests $c = 2$ (diagonal clash with $(0, 3)$) and $c = 3$ (column clash). Row 1 ends.

#### Step 32: Backtrack from $(0, 3)$
* Removes queen from $(0, 3)$.
* Row 0 has tested all possible columns ($c = 0, 1, 2, 3$).
* The search space is exhausted; algorithm terminates with **2 valid solutions** found.