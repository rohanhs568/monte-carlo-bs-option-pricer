# Monte Carlo Pricing and Greeks under Black-Scholes

This repository contains a numerical study of Monte Carlo option pricing and Greek estimation in the Black-Scholes model. Analytical formulas are available for all quantities, which allows direct comparison between simulation output and the exact values. The aim is to examine accuracy, variance reduction, and hedging performance in a controlled setting.

## 1. Monte Carlo pricing

Terminal prices are generated using the geometric Brownian motion model

$S_T = S_0 \exp\big((r - 0.5\sigma^2)T + \sigma\sqrt{T}\,Z\big)$ with $Z \sim N(0,1)$,

and the discounted payoff is estimated by

$C_0 = e^{-rT} \mathbb{E}[(S_T - K)^+]$.

Empirical convergence follows the expected Monte Carlo rate  
$\text{RMSE} = O(N^{-1/2})$.

## 2. Variance reduction

Three standard variance reduction methods are implemented:

- antithetic variates  
- control variates using $\mathbb{E}[S_T] = S_0 e^{rT}$  
- stratified sampling  

All maintain the $N^{-1/2}$ convergence rate. For this payoff, stratified sampling gives the largest variance reduction.

## 3. Delta estimation

Two estimators are used:

- pathwise derivative  
- central finite difference  
  $\Delta \approx [C(S_0+h) - C(S_0-h)]/(2h)$  

The pathwise estimator has the lowest variance and converges more efficiently.

## 4. Gamma estimation

Gamma is approximated by the second-order finite difference

$\Gamma \approx [C(S_0 + h) - 2C(S_0) + C(S_0 - h)] / h^2$,

with common random numbers to stabilise the estimator.  
The method converges at the Monte Carlo rate but is noisier due to the curvature of the payoff near $K$.

## 5. Hedging error analysis

Full price paths are simulated to study discrete-time delta hedging.  
The hedging error depends mainly on:

- the rebalancing interval  
- the initial Gamma of the option  

Higher Gamma leads to larger residual hedging variance when the hedge is updated discretely.

## Key observations

- Monte Carlo estimates match Black-Scholes prices with the expected $N^{-1/2}$ rate  
- stratified sampling provides the strongest variance reduction  
- the pathwise Delta estimator is significantly more efficient than finite differences  
- Gamma estimation is inherently less stable  
- hedging error increases with both rebalancing interval and initial Gamma  

## Summary

The project gives a compact numerical study of Monte Carlo pricing and Greek estimation under the Black-Scholes model. The approach extends directly to settings without closed-form solutions, including stochastic volatility, local volatility, and path-dependent payoffs, where simulation becomes central in practical quantitative finance.
