import numpy as np

def simulate_ST(S0, r, sigma, T, N, rng):
    Z = rng.standard_normal(N)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    return ST

def simulate_path_ST(S0, r, sigma, T, N_steps, rng):
    dt = T / N_steps
    S = np.empty(N_steps + 1)
    S[0] = S0
    for t in range(1, N_steps + 1):
        Z = rng.standard_normal()
        S[t] = S[t-1] * np.exp((r - 0.5 * sigma**2)*dt + sigma*np.sqrt(dt)*Z)
    return S
