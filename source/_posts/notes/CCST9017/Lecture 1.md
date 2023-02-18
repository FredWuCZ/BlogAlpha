---
title: CCST9017 Lecture 1
---

# CCST9017
ntw@maths.hku.hk

## Two areas

Information processing

Decision making

<!-- more -->

## Marking

Class work -> due next day after lecture

Assignment and tutorial -> due next Monday

Project report

Oral presentation

In class-test -> Last week, one-hour

# Infectious Disease Modeling I
## Mathematics
Characteristics: abstract, precise, logical reasoning

## SIM
## Infectious Diseases
States: susceptible, latent, infectious, immune/removed
## SIR Model
Assumptions:
- Population size is large and constant
- no latency
- homogeneous mixing (equal opportunities of meeting each person)

Divide total population $N$ into 3 groups:
1. susceptible class, $S_t$
2. infective class, $I_t$
3. removed class, $R_t$

Reasons of removal: recovered, naturally immune, isolated, died

Number of encounters: $S_tI_t$  
Infected proportion: $\alpha$

In the next time interval:
$$S_{t+1} = S_t - \alpha S_tI_t$$

Removal rate: $\gamma$

In the next time interval: <br>
$$I_{t+1} = I_t + \alpha S_tI_t - \gamma I_t$$
$$R_{t+1} = R_t + \gamma I_t$$

Let $\Delta S = S_{t+1} - S_t$, so are $\Delta I$ and $\Delta R$, then
$$\Delta S = - \alpha S_tI_t$$
$$\Delta I = \alpha S_tI_t - \gamma I_t$$
$$\Delta R = \gamma I_t$$

round numbers to integers

### Thread Values and Critical Parameters
Assume epidemic occurs if $\Delta I > 0$, otherwise no outbreak takes place
$$\Delta I > 0 \implies \alpha S_t - \gamma > 0$$
if $I_t = 0$, then $\Delta I = 0$ <br>
if $I_t > 0$, then compare $S_t$ with $\dfrac{\gamma}{\alpha}$ <br>
if $S_t < \dfrac{\gamma}{\alpha}$, there is an outbreak  
$S_t$ is non-increasing, so if $S_0 < \dfrac{\gamma}{\alpha}$, then for all $t$, $S_t < \dfrac{\gamma}{\alpha}$ <br>

Basic reproduction number: $R_0 = \dfrac{\alpha}{\gamma}S_0$ (not removal number)  
Outbreak takes place if $R_0 > 1$

### Biological Meaning
$\alpha S_0$: the number of individuals infected by contact with a single ill individual during the inital time step.

Example: If the period of contagion lasts 7 days, then 
each day we expect roughly $\frac{1}{7}$ or approximately 14% 
of the total number of infectives to move from the 
infective class $I_t$ into the removed class $R_t$

$\dfrac{1}{\gamma}$: average duration of infectious period

$R_0$: average number of secondary infections that would be produced by an infective in a wholly susceptible population of size $S_0$

### Continuous Model
Replace $\dfrac{\Delta S}{\Delta t}$ with $\dfrac{\mathrm{d}S}{\mathrm{d}t}$, so are others

### Case Study
Find $\alpha$, $\gamma$ and $I(0)$ such that
$$\min_{\alpha, \gamma, I(0)} \sum_{t=1}^5(R(t)-R_e(t))^2$$

(HKU has a nice book)

# Infectious Disease Modeling II

## sir Model
Proportions of the population are used  
Useful hen the precise size of the population may not be known

Set $s = \frac{S}{N}$, $i = \frac{I}{N}$, $r = \frac{R}{N}$, and rebuild the model

Notice that $s + i + r = 1$
$$\Delta s = -\beta s_ti_t$$
$$\Delta i = \beta s_ti_t - \gamma i_t$$
$$\Delta r = \gamma i_t$$

$$\Delta S = \Delta sN = -\beta s_ti_tN = -\beta i_tS_t$$
Contact: interaction between individuals that is SUFFICIENT for disease transmission  
Number of contacts during a single time step: $-\Delta S = S_t - S_{t + 1}$  
Average number of contacts a susceptible has with infectives: $\frac{-\Delta S}{S_t} = \beta i_t$  
Hence $\beta$: average number of contacts that an individual has (depends on the particulars of the disease)

$\sigma$: average number of contacts of a typical infective during the entire infectious period
$$\sigma = \frac{\beta}{\gamma}$$

*Exercise: work out the relationship between $R_0$ and $\sigma$ supposing $S_0 = N$*

## Vaccinations
We want $\Delta i < 0$, or $s_t < \frac{\gamma}{\beta} = \frac{1}{\sigma}$  
Vaccination can reduce $s_t$ to less than $\frac{1}{\sigma}$  
Vaccination rate should be at least $1 - \frac{1}{\sigma}$

## Fighting AIDS
