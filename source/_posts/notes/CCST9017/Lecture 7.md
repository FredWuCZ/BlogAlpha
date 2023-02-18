# Probability
## Personal Probabilities
Condition: Between 0 and 1, coherent

## Probability Rules
Rule 0: $0 \leq P(A) \leq 1$  
Rule 1: $P(A) + P(A^C) = 1$  
Rule 2: If $A$ and $B$ are mutually exclusive, then $P(A  \cup B) = P(A) + P(B)$  
Rule 3: If $A$ and $B$ are independent, then $P(A \cap B) = P(A) P(B)$  
Rule 4: If $B \subseteq A$, then $P(B) \leq P(A)$

### Independent
If two events do not influence each other
$$P(A \cap B) = P(A) P(B)$$

## Long-term Outcomes

## Certainty Effect

## Tree Diagram
Fake positives

## Traps
Manipulation of results

### Fabricated Toss
$(i, j)$: $j$ tosses to go, last $i$ tosses are of the same outcome.  
$$u(i, j) = 0.5u(i + 1, j - 1) + 0.5u(1, j - 1)$$
Boundary conditions:
$u(i, 0) = 0$ for $i = 1, 2, ..., r - 1$  
$u(r, j) = 1$ for $j = 0, 1, 2, ..., n - r$

## Benford's Law
$P(\text{the first significant digit} = d) = \lg(1 + \frac{1}{d})$