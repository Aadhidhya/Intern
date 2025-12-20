# Max Profit Problem — Python solution
# Each building:
#  - Theatre: build_time=5, rate=1500
#  - Pub:     build_time=4, rate=1000
#  - CommPk:  build_time=10, rate=2000
#
# The function max_profit(n) returns (best_earnings, best_counts_dict)
# and also prints a readable solution.

def max_profit(n: int):
    build = {
        'T': {'time': 5, 'rate': 1500},
        'P': {'time': 4, 'rate': 1000},
        'C': {'time': 10, 'rate': 2000},
    }

    best_earn = -1
    best_choice = {'T': 0, 'P': 0, 'C': 0}
    # We will iterate counts of T, P, C consistent with total build time <= n.
    # Order of construction assumed optimal: all T, then all P, then all C.
    max_T = n // build['T']['time']
    for t in range(max_T + 1):
        time_after_T = n - t * build['T']['time']
        max_P = time_after_T // build['P']['time'] if time_after_T >= 0 else 0
        for p in range(max_P + 1):
            time_after_TP = time_after_T - p * build['P']['time']
            max_C = time_after_TP // build['C']['time'] if time_after_TP >= 0 else 0
            for c in range(max_C + 1):
                total_build_time = (t * build['T']['time'] +
                                    p * build['P']['time'] +
                                    c * build['C']['time'])
                if total_build_time > n:
                    continue  # not feasible
                # compute earnings: sum over completion times
                earnings = 0
                # Theatres complete at times 5,10,15,... (5*i)
                for i in range(1, t + 1):
                    completion = i * build['T']['time']
                    op_time = n - completion
                    if op_time > 0:
                        earnings += build['T']['rate'] * op_time
                # Pubs complete after all theatres: base_time = 5*t
                base_after_T = t * build['T']['time']
                for j in range(1, p + 1):
                    completion = base_after_T + j * build['P']['time']
                    op_time = n - completion
                    if op_time > 0:
                        earnings += build['P']['rate'] * op_time
                # Commercials complete after theatres+p ubs
                base_after_TP = base_after_T + p * build['P']['time']
                for k in range(1, c + 1):
                    completion = base_after_TP + k * build['C']['time']
                    op_time = n - completion
                    if op_time > 0:
                        earnings += build['C']['rate'] * op_time

                if earnings > best_earn:
                    best_earn = earnings
                    best_choice = {'T': t, 'P': p, 'C': c}

    return best_earn, best_choice

# Helper to pretty-print and test
def print_solution(n):
    earn, choice = max_profit(n)
    print(f"Input Time Unit: {n}")
    print(f"Best Earnings: ${earn}")
    print(f"Solution: T: {choice['T']} P: {choice['P']} C: {choice['C']}")
    print("Explanation: buildings are constructed sequentially in order: Theatre(s) -> Pub(s) -> Commercial(s).")
    print()

# Example test cases from the problem statement
if __name__ == "__main__":
    for test_n in (7, 8, 13):
        print_solution(test_n)
