import numpy as np
from .greeks import bs_call_delta
from .simulation import simulate_path_ST

def hedging_error_one_path(S0, K, r, sigma, T, N_steps, rebalance_every, rng):
    S = simulate_path_ST(S0, r, sigma, T, N_steps, rng)
    dt = T / N_steps

    tau = T
    Delta_prev = bs_call_delta(S[0], K, r, sigma, tau)
    stock_pos = Delta_prev
    cash = -stock_pos * S[0]

    for t in range(1, N_steps + 1):
        if t % rebalance_every == 0:
            tau = T - t*dt
            Delta_new = bs_call_delta(S[t], K, r, sigma, tau)
            change = Delta_new - Delta_prev
            cash -= change * S[t]
            Delta_prev = Delta_new

    payoff = max(S[-1] - K, 0.0)
    portfolio = stock_pos * S[-1] + cash * np.exp(r*T)
    return portfolio - payoff

def hedging_error_distribution(S0, K, r, sigma, T, N_paths, N_steps, rebalance_every):
    rng = np.random.default_rng(123)
    errors = np.empty(N_paths)
    for i in range(N_paths):
        errors[i] = hedging_error_one_path(
            S0, K, r, sigma, T,
            N_steps, rebalance_every, rng
        )
    return errors
