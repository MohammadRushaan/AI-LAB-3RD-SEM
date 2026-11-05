# =====================================================================
# 1. FORWARD CHAINING
# =====================================================================
def forward_chaining(facts, rules, query):
    """facts: set of known facts (e.g., {'Cloudy', 'Humid'})

    rules: list of tuples (premises_list, conclusion)
    query: target string to test
    """
    print("\n--- FORWARD CHAINING TRACE ---")

    # If already a known fact, we are done
    if query in facts:
        print(f"Query '{query}' is already a base fact!")
        return True

    # Track how many premises remain unsatisfied for each rule
    count = [len(premises) for premises, _ in rules]

    # Queue of facts whose implications are yet to be checked
    agenda = list(facts)
    known = set(facts)

    print(f"Initial facts on agenda: {agenda}")

    while len(agenda) > 0:
        p = agenda.pop(0)
        print(f"Processing symbol: {p}")

        for i in range(len(rules)):
            premises, conclusion = rules[i]

            if p in premises:
                count[i] -= 1
                print(
                    f"  Matched '{p}' in rule: {' ^ '.join(premises)} => {conclusion} (Remaining premises: {count[i]})"
                )

                # When all premises of this rule are satisfied
                if count[i] == 0:
                    print(f"  ==> Rule fired! Inferred: {conclusion}")
                    if conclusion == query:
                        print(f"  ==> Query '{query}' entailed!")
                        return True

                    if conclusion not in known:
                        known.add(conclusion)
                        agenda.append(conclusion)

    print(f"Agenda empty. Query '{query}' could NOT be entailed.")
    return False


# =====================================================================
# 2. RESOLUTION REFUTATION
# =====================================================================
def negate(literal):
    """Returns ~L for positive literal L, and removes ~ for negative."""
    if literal.startswith("~"):
        return literal[1:]
    return "~" + literal


def resolve_two_clauses(c1, c2):
    """Resolves two clauses (frozensets of literals) on complementary pairs."""
    resolvents = []
    for lit in c1:
        comp = negate(lit)
        if comp in c2:
            # Drop the complementary pair and combine the remaining literals
            new_clause = (c1 - {lit}) | (c2 - {comp})
            resolvents.append(frozenset(new_clause))
    return resolvents


def resolution(cnf_clauses, query):
    """cnf_clauses: list of lists representing OR-clauses (e.g.

    [['~A', 'B']])
    query: target string to test
    """
    print("\n--- RESOLUTION TRACE ---")

    # Convert list of clauses to a set of frozensets
    clauses = set(frozenset(c) for c in cnf_clauses)

    # To test KB |= query, assume KB ^ ~query and check for contradiction
    neg_query = frozenset([negate(query)])
    clauses.add(neg_query)

    print(f"Goal: Prove '{query}'")
    print(f"Negated query added: {set(neg_query)}")
    print(f"Total starting clauses: {[set(c) for c in clauses]}")

    step = 1
    while True:
        new_clauses = set()
        clause_list = list(clauses)
        n = len(clause_list)

        # Check all pairs of clauses
        for i in range(n):
            for j in range(i + 1, n):
                c1 = clause_list[i]
                c2 = clause_list[j]

                resolvents = resolve_two_clauses(c1, c2)

                for res in resolvents:
                    # Empty set means contradiction derived (L and ~L resolved)
                    if len(res) == 0:
                        print(
                            f"Step {step}: Resolved {set(c1)} and {set(c2)} => EMPTY CLAUSE {{}} (Contradiction!)"
                        )
                        print(f"==> Query '{query}' is entailed (True).")
                        return True

                    if res not in clauses and res not in new_clauses:
                        print(
                            f"Step {step}: Resolved {set(c1)} and {set(c2)} => {set(res)}"
                        )
                        new_clauses.add(res)
                        step += 1

        # If no new clauses were derived, refutation failed
        if new_clauses.issubset(clauses):
            print("No new resolvents can be produced. No contradiction.")
            print(f"==> Query '{query}' is NOT entailed (False).")
            return False

        clauses.update(new_clauses)


# =====================================================================
# 3. KNOWLEDGE BASE SETUP & TEST RUN
# =====================================================================
# Weather Domain:
# Cloudy ^ Humid => Rainy
# Rainy => WetGround
# Rainy => TakeUmbrella
# WetGround => Slippery

# Forward Chaining format: (premises_list, conclusion)
fc_facts = {"Cloudy", "Humid"}
fc_rules = [
    (["Cloudy", "Humid"], "Rainy"),
    (["Rainy"], "WetGround"),
    (["Rainy"], "TakeUmbrella"),
    (["WetGround"], "Slippery"),
]

# Resolution CNF format: list of OR clauses
# (A ^ B => C is logically equivalent to ~A v ~B v C)
cnf_kb = [
    ["Cloudy"],
    ["Humid"],
    ["~Cloudy", "~Humid", "Rainy"],
    ["~Rainy", "WetGround"],
    ["~Rainy", "TakeUmbrella"],
    ["~WetGround", "Slippery"],
]

# Display Knowledge Base
print("=" * 60)
print("KNOWLEDGE BASE FACTS AND RULES:")
print("Base Facts:", fc_facts)
print("Rules (Horn Form):")
for prems, concl in fc_rules:
    print(f"  {' ^ '.join(prems)} => {concl}")
print("=" * 60)

# Test 1: Query that should be True
query1 = "TakeUmbrella"
print(f"\n================ TESTING QUERY 1: {query1} ================")
res_fc = forward_chaining(fc_facts, fc_rules, query1)
res_reso = resolution(cnf_kb, query1)
print(f"\nResult for '{query1}':")
print(f"  Forward Chaining: {res_fc}")
print(f"  Resolution:       {res_reso}")

# Test 2: Query that should be False
query2 = "Snowy"
print(f"\n================ TESTING QUERY 2: {query2} ================")
res_fc2 = forward_chaining(fc_facts, fc_rules, query2)
res_reso2 = resolution(cnf_kb, query2)
print(f"\nResult for '{query2}':")
print(f"  Forward Chaining: {res_fc2}")
print(f"  Resolution:       {res_reso2}")