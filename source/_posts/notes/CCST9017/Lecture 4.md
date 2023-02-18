# Searching Love with Mathematics
Assume meeting $N$ women one by one within the following ten years. Decide whether to reject.
- Cannot return
- In random order

## Maximize the chance of getting the best woman
Assess the quality of $37\%$ of the women, but reject all of them.  
Then choose the first woman who is better of the previously rejected women.

## x% Strategy
Let A be the best of the $N$ men.  
Assume A is in the $k$-th position. (Probability $\frac{1}{N}$)  
Let $C$ be the best man among the first $k - 1$ men.  
Suppose the first $s \, (s < N)$ men will be rejected.

$k \leq s$: Reject A  
$k = s + 1$: Catch A  
$k = s + 2$:
- If $C \leq s$ (Probability: $\frac{s}{s + 1}$): Catch A
- If $C > s$ (Probability: $\frac{1}{s + 1}$): Can't catch A

Probability of catching $A$:
$$ \begin{align} 
p(s) &= \frac{1}{N} (1 + \frac{s}{s + 1} + \frac{s}{s + 2} + ... + \frac{s}{N - 1}) \\
&= \frac{s}{N} \sum_{k = s}^{N - 1} \frac{1}{k} \\
&= \frac{s}{N} \sum_{k = s}^{N - 1} \frac{1}{\frac{k}{N}} \frac{1}{N} \\
&= x\int_x^1 \frac{1}{t} \mathrm{d}t \quad (x = \frac{s}{N} \text{ for large N}) \\
&= -x\ln x
\end{align}$$
$$f(x) = -x\ln x \text{ has a maximum of } x = \frac{1}{e}$$
$$p(\frac{N}{e}) = \frac{1}{e} \approx 37\%$$
Maximum occurs when $s = \frac{N}{e} \approx 0.37N$

$$e = \lim_{n \to \infin} (1 + \frac{1}{n})^n$$

## Misuses of Mathematical Models

## Ramsey Theorem
For every coloring of the $k$-subsets of a sufficiently large set $X$, there is an $s$-element subset of $X$ whose $k$-subsets all have the same color.

### Q Test

### How to Propose
"You will neither kiss me nor marry me."

## Adjusted Winner Procedure
- Both parties get the same score  
- Neither party is willing to give up their share in exchange for the other's
- Ther is no other allocation that increases the total number of points for both parties at the same time