import numpy as np
from scipy.stats import norm
from .simulation import simulate_ST

def bs_call_price(S0, K, r, sigma, T):
    d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S0 * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)

def mc_european_call(S0, K, r, sigma, T, N, rng):
    ST = simulate_ST(S0, r, sigma, T, N, rng)
    payoff = np.maximum(ST - K, 0.0)
    return np.exp(-r*T) * payoff.mean()

def mc_european_call_stratified(S0, K, r, sigma, T, N, rng):
    U = (np.arange(N) + rng.random(N)) / N
    Z = norm.ppf(U)
    ST = S0 * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
    payoff = np.maximum(ST - K, 0.0)
    return np.exp(-r*T) * payoff.mean()
