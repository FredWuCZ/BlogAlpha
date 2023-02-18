# Introduction to Game Theory
## Game Theory
The study of mathematical models on conflicts and cooperations between rational individuals

### John von Neumann
Inventor of Game Theory

## Prisoner's Dilemma
|                   | Confess (C) | Don't confess (D) |
|:-----------------:|:-----------:|:-----------------:|
|    Confess (C)    |     5,5     |        0,10       |
| Don't confess (D) |     10,0    |        2,2        |

Base on the payoffs,  
Player A: $(C, D) > (D, D) > (C, C) > (D, C)$  
Player B: $(D, C) > (D, D) > (C, C) > (C, D)$

## Dating Game
Better together
|          | Football | Dinner |
|:--------:|:--------:|:------:|
| Football |    2,1   |   0,0  |
|  Dinner  |    0,0   |   1,2  |

Player A: $(C, C) > (D, D) > (C, D) = (D, C)$  
Player B: $(D, D) > (C, C) > (C, D) = (D, C)$

## Dominant Strategy
A strategy which is always better than any other strategy

In personer's dilemma, both players will choose confess.  
Outcome: confess, confess

## Dominant Strategy Equilibrium
If every player has a dominant strategy, then dominant strategy equilibrium exists, and it will be the outcome.

In dating game, it does not exist.

## Zero-sum Game
In zero-sum games, one player's loss is the other player's gain.

For any zero-sum game, (mixed) dominant strategy equilibrium always exists.

## Nash Equilibrium
If no individual will change his position, given that the others do not change their positions.

### Splitting the Bill
Everyone cheap meal -> not Nash equilibrium  
Everyone excellent meal -> Nash equilibrium

A dominant strategy equilibrium must be a Nash equilibrium

## Mixed Nash Equilibrium
If no individual will change his mixed strategy, given that the other do not change their mixed strategies.

Showing fingers  
$(1,1,2), (1,2,1), (2,1,1), (1,2,2), (2,1,2), (2,2,1)$ are Nash equilibria  
Each player decide for what percentage of the games should he/she choose one finger. -> Mixed strategy  
100% for one strategy -> Pure strategy (included in mixed strategy)  
The mixed Nash equilibrium is $((41\%, 59\%), (41\%, 59\%), (41\%, 59\%))$, or $(41\%, 41\%, 41\%)$

## Every Finite N-player Non-cooperative Game Has a Mixed Nash Equilibrium.

## Applicatons
Evolutionary Biology  


# Game Theory and Auctions
## Matching Pennies Game
A and B choose to show head or tail of a coin.

Same side: B pays A $2  
Different sides: A pays B $2

Zero-sum game?: YES  
Nash equilibrium exists?: NO  
Dominant Strategy equilibrium exists?: NO  
Mixed Nash equilibrium exist?: YES

### Find Mixed Nash Equilibria
Let p and q be probability for A, B to choose head respectively.
|           | Head(q) | Tail(1-q) |
|:---------:|:-------:|:---------:|
|  Head(p)  |   2,-2  |    -2,2   |
| Tail(1-p) |  -2,2   |    2,-2   |

$E_A(p, q)$ = expected payoff of A when a chooses p and b chooses q
$$ \begin{align}
E_A(p, q) &= 2pq + 2(1-p)(1-q) + (-2)p(1-q)+(-2)(1-p)q \\
&=p[2q - 2(1 - q)] + (1 - p)[-2q+2(1-q)] \\
&= pE_A(1, q) + (1 - p)E_A(0, q) \\
&= [E_A(1, q) - E_A(0, q)]p + E_A(0, q)
\end{align} $$
(4): a linear function in $p$  
$E_B(p, q)$ = expected payoff of B when a chooses p and b chooses q
$$ \begin{align}
E_B(p, q) &= -2pq -2(1-p)(1-q) + 2p(1-q)+2(1-p)q \\
&= q[2(1 - p) - 2p] + (1-q)(2p - 2(1 - p)) \\
&= [E_B(p, 1) - E_B(p, 0)]q + E_B(p, 0)
\end{align} $$

Suppose $(p^*, q^*)$ is a mixed Nash equilibrium  
For all $0 \leq p, q \leq 1$,
$$
\begin{align}
E_A(p^*, q^*) \geq E_A(p, q^*) \\
E_B(p^*, q^*) \geq E_B(p^*, q)
\end{align}
$$
If $0 < p^* < 1$, then (8) holds only if $E_A(1, q^*) - E_A(0, q^*) = 0$,  so $4q^* - 4(1 - q^*) = 0$,  
so $p^* = q^* = 0.5$ if $0 < p^*, q^* < 1$  
Nash equilibrium must be one of the following: $(0, 1), (1, 0), (0, 0), (1, 1)$ and $(0.5, 0.5)$

$E_A(p, 0.5) = 0$ for $0 \leq p \leq 1$, so A has no incentive to change  
$E_A(0.5, q) = 0$ for $0 \leq q \leq 1$, so B has no incentive to change  
So $(0.5, 0.5)$ is the only mixed Nash equilibrium.  

## Auction

### Sources of Uncertainty
Private value: different value for each bidder  

Common value: roughtly equal value for each bidder, but unknown

English auction: start low, add price  
Dutch auction: start high, reduce price  
First price sealed-bid auction (equivalent to Dutch auction in payoff)  
Second price sealed-bid auction (Vickrey's auction)

### Auction Design
(Strange: second bidder wins)

### Winner's Curse
The winner tends to overpay

## Dominant Strategy of Sealed Second-price Auction
Bidding according to your valuation is the dominant strategy

Avoid winner's curse

## Equivalence
The expected price paid to the auctionerer is the same.

Reason: in second price, bidders tend to bid higher.