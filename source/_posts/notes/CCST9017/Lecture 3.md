# Shapley Value
Set of all players: $N = \{1, 2, 3\}$ 

## Coalition (subset)
Set of all coalitions $2^N$

Coalition function $v$

### Example: House Transaction
Seller 1: values the house 1  
Buyer 2: value 2  
Buyer 3: value 2

Price of house: $p \, (1 < p \leq 2)$  
$v(1, 2) = (0 + p) + [(2 - p) + 2] = 4$  
$v(1, 3) = 4$  
$v(2, 3) = 4$  
If $p < 2$, then player 3 can offer $q (> p)$ to player 1  
Thus $p = 2$  
$v(1, 2, 3) = (0 + 2) + [(2 - 2) + 2] + 2 = 6$

## Weighted Voting Games
Weight: $w_i$

Notation: $[8; 5, 3, 7]$ (quota; weights)

Example: $w_1 = 5, w_2 = 3, w_3 = 7$  
$$
v(S) = \begin{cases}
1 & \quad \text{if } \sum_{i \in S} w_i \geq 8 \\
0 & \quad \text{if } \sum_{i \in S} w_i < 8
\end{cases} $$

### Symmetric Players
Player $i$ and player $j$ of the game are symmetric players in the game if for all subsets $S$ containing neither $i$ nor $j$,
$$v(S \cup \{i\}) = v(S \cup \{j\})$$

### Null Players
Player $i$ is a null player if $v(S \cup i) = v(S)$ for all $S \subsetneq N$

### Sum of Games
1. If $i$ and $j$ are symmetric players in $(N; v)$, then $\phi_i(v) = \phi_j(v)$  
2. If $i$ is a null player, then $\phi_i = 0$
3. $\sum_{i \in N} \phi_i(v) = v(N)$
4. $\phi_i(v + w) = \phi_i(v) + \phi_i(w)$, for all $i$ in $N$
*Proved by linear algebra*

### Carrier Game
$$
v(S) = \begin{cases}
v(T) & \quad \text{if } S \supseteq T \\
0 & \quad \text{otherwise}
\end{cases} $$

$\sigma$ is a permutation  
$N_\sigma^i$ is the numbers before $i$

## Find the Shapley Value

## Shapley's Formula
$$\phi_i = \frac{1}{n!} \sum_{\text{all permutations $\sigma$}}[v(N_\sigma^i \cup \{i\}) - v(N_\sigma^i)]$$

Marginal contributions: $v(N_\sigma^i \cup \{i\}) - v(N_\sigma^i)$