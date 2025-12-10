import numpy as np
from scipy.stats import norm
from .pricing import mc_european_call

def bs_call_delta(S, K, r, sigma, tau):
    if tau <= 0:
        return np.where(S > K, 1.0, 0.0)
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*tau) / (sigma*np.sqrt(tau))
    return norm.cdf(d1)

def bs_call_gamma(S, K, r, sigma, tau):
    if tau <= 0:
        return 0.0
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*tau) / (sigma*np.sqrt(tau))
    return norm.pdf(d1) / (S * sigma * np.sqrt(tau))

def mc_delta_pathwise(S0, K, r, sigma, T, N, rng):
    Z = rng.standard_normal(N)
    ST = S0 * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
    indicator = (ST > K).astype(float)
    delta = indicator * ST / S0
    return np.exp(-r*T) * delta.mean()

def mc_delta_finite_difference(S0, K, r, sigma, T, N, h, rng):
    price_up   = mc_european_call(S0 + h, K, r, sigma, T, N, rng)
    price_down = mc_european_call(S0 - h, K, r, sigma, T, N, rng)
    return (price_up - price_down) / (2*h)

def mc_gamma_finite_difference(S0, K, r, sigma, T, N, h, rng):
    p_up   = mc_european_call(S0 + h, K, r, sigma, T, N, rng)
    p_mid  = mc_european_call(S0,     K, r, sigma, T, N, rng)
    p_down = mc_european_call(S0 - h, K, r, sigma, T, N, rng)
    return (p_up - 2*p_mid + p_down) / (h*h)
