def forward_chaining(facts, rules, query):
    print("\n--- FORWARD CHAINING TRACE ---")

    # If the query is already in facts, return immediately
    if query in facts:
        print("Goal '" + query + "' is already known!")
        return True

    # Build the count list
    unmet_count = []
    for rule in rules:
        premises = rule[0]
        unmet_count.append(len(premises))

    # Initialize agenda queue
    agenda = []
    for f in facts:
        agenda.append(f)

    known = set()
    for f in facts:
        known.add(f)

    print("Starting facts on queue: " + str(agenda))

    while len(agenda) > 0:
        fact = agenda.pop(0)
        print("Checking fact: " + str(fact))

        for i in range(len(rules)):
            premises = rules[i][0]
            conclusion = rules[i][1]

            if fact in premises:
                unmet_count[i] = unmet_count[i] - 1
                print("  Satisfied condition in rule: " + str(premises) + " => " + conclusion + 
                      " (Remaining needed: " + str(unmet_count[i]) + ")")

                # If all premises of this rule are satisfied
                if unmet_count[i] == 0:
                    print("  ==> Rule fired! Deduced: " + conclusion)
                    if conclusion == query:
                        print("  ==> Target '" + query + "' reached successfully!")
                        return True

                    if conclusion not in known:
                        known.add(conclusion)
                        agenda.append(conclusion)

    print("Queue empty. Could not prove '" + query + "'.")
    return False

def negate(lit):
    #Complements the Literl
    if lit.startswith("~"):
        return lit[1:]
    return "~" + lit

def resolution(cnf_clauses, query):
    print("\n--- RESOLUTION TRACE ---")

    # Convert list of clause lists into a set of frozensets
    # Frozen sets are immutable sets and hence can be used to put a set inside a set
    # In logical resolution, the knowledge base is a set of clauses, and each clause is a set of literals
    clauses = set()
    for c in cnf_clauses:
        clause_frozenset = frozenset(c)
        clauses.add(clause_frozenset)

    # Negate the query and add it as a clause
    negated_lit = negate(query)
    neg_q = frozenset([negated_lit])
    clauses.add(neg_q)

    printable_clauses = []
    for c in clauses:
        printable_clauses.append(set(c))

    print("Goal: Prove '" + query + "' by refuting " + str(set(neg_q)))
    print("Starting clauses: " + str(printable_clauses))

    step = 1
    while True:
        new_clauses = set()
        clause_list = list(clauses)
        n = len(clause_list)

        # Compare every unique pair of clauses
        for i in range(n):
            for j in range(i + 1, n):
                c1 = clause_list[i]
                c2 = clause_list[j]

                # Check if any literal in c1 has its opposite in c2
                for lit in c1:
                    opposite = negate(lit)
                    if opposite in c2:
                        # Drop complementary pair and combine remaining literals
                        c1_remaining = c1 - {lit}
                        c2_remaining = c2 - {opposite}
                        resolvent = frozenset(c1_remaining | c2_remaining)

                        # Empty clause derived: Contradiction found
                        if len(resolvent) == 0:
                            print("Step " + str(step) + ": Resolved " + str(set(c1)) + 
                                  " and " + str(set(c2)) + " => {} (Empty Clause / Contradiction!)")
                            print("==> Contradiction found! Therefore '" + query + "' is TRUE.")
                            return True

                        if resolvent not in clauses and resolvent not in new_clauses:
                            print("Step " + str(step) + ": Resolved " + str(set(c1)) + 
                                  " and " + str(set(c2)) + " => " + str(set(resolvent)))
                            new_clauses.add(resolvent)
                            step = step + 1

        # If no new clauses were formed, entailment fails
        if new_clauses.issubset(clauses):
            print("No new clauses can be derived. No contradiction found.")
            print("==> Query '" + query + "' is FALSE.")
            return False

        # Add newly derived clauses to the main clause
        for c in new_clauses:
            clauses.add(c)

# Forward Chaining setup
fc_facts = {"Cloudy", "Humid"}
fc_rules = [
    (["Cloudy", "Humid"], "Rainy"),
    (["Rainy"], "WetGround"),
    (["Rainy"], "TakeUmbrella")
]

# 2. Resolution setup :
cnf_kb = [
    ["Cloudy"],
    ["Humid"],
    ["~Cloudy", "~Humid", "Rainy"],
    ["~Rainy", "WetGround"],
    ["~Rainy", "TakeUmbrella"]
]

query1 = "TakeUmbrella"
print("==================== QUERY 1: " + query1 + " ====================")
res_fc1 = forward_chaining(fc_facts, fc_rules, query1)
res_res1 = resolution(cnf_kb, query1)
print("\nFinal Results for '" + query1 + "':")
print("  Forward Chaining: " + str(res_fc1))
print("  Resolution:       " + str(res_res1))

query2 = "Snowy"
print("\n==================== QUERY 2: " + query2 + " ====================")
res_fc2 = forward_chaining(fc_facts, fc_rules, query2)
res_res2 = resolution(cnf_kb, query2)
print("\nFinal Results for '" + query2 + "':")
print("  Forward Chaining: " + str(res_fc2))
print("  Resolution:       " + str(res_res2))