# Portfolio Diversification
Portfolio: a collection of assets

If the expected return is the same, we want low variance.

## Equally Weighted Portfolio
$n$ independent assets  
$\sigma$: standard deviation  
$r$: expected return  
satisfies quare root rule:
$$\sigma_{\text{portfolio}} = \frac{\sigma}{\sqrt{n}}$$
$$r_{\text{portfolio}} = r$$

### Covariance
$$\text{cov}(x, y) = E[(x - E(x))(Y - E(Y))]$$

## Two Asset Case
$n = 2$, not independent  
Asset 1: $r_1$, $\sigma_1$  
Asset 2: $r_2$, $\sigma_2$  
Covariance: $\sigma_{12}$  
Put $x_1$ in asset 1  
$x_2 = 1 - x_1$ in asset 2

Portfolio expected return:
$r = \sum_{i = 1}^n x_ir_i = x_1r_1 + (1 - x_1)r_2$

Variance:
$\sigma^2 = x_1^2\sigma_1^2 + x_2^2\sigma_2^2 + 2x_1x_2\sigma_{12}^2$

## Efficient Portfolio Frontier

## More Assets
$n = 3$, $x_1 + x_2 + x_3 = 1$  
$r = \sum_{i = 1}^n x_ir_i = x_1r_1 + x_2r_2 + x_3r_3$  
$\sigma = x_1^2\sigma_1^2 + x_2^2\sigma_2^2 + x_3^2\sigma_3^2 + 2x_1x_2\sigma_{12} + 2x_2x_3\sigma_{23} + 
2x_1x_3\sigma_{13}$


### Riskless Asset
$r_f$, $\sigma_f = 0$, $\sigma_{if} = 0$  
Graph: a straight line


# Portfolio Theory
$m$ risky assts $i = 1, 2, ..., m$  
Single-period returns:  
$R = [R_1, R_2, ..., R_m]'$  
$w = (w_1, ..., w_m): \sum_{i = 1}^m w_i = 1$  

## Minimum Variance Portfolio
$$\sigma_w^2 = (1 - w)^2\sigma_1^2 + w^2\sigma_2^2$$
$$\frac{\partial\sigma_w^2}{\partial w} = (1 - w)\sigma_1^2(-1) + 2w\sigma_2^2 = 0$$
$$w = \frac{\frac{1}{\sigma_2^2}}{\frac{1}{\sigma_1^2} + \frac{1}{\sigma_2^2}}$$

No portfolio dominates the others after the vertical tangent.

Negative correlation: lower minimum variance  
Positive correlation: higher minimum variance

# Post-modern Portfolio Theory
## Downside Risk
$$d = \sqrt{\int_{-\infin}^t (t - r)^2 f(r)\mathrm{d}r}$$
$t$: Annual target return  
$f(r)$: Distribution for annual

## Sortino Ratio
$$\frac{r - t}{d}$$
$r$: Annual rate of return  
$t$: Target return  
$d$: Downside risk