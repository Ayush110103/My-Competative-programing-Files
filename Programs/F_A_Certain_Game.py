MOD = 998244353

def main():
    N = int(input())  # Number of players
    matches = []  # To store matches each player participates in

    # Initialize the matches data structure
    for _ in range(N - 1):
        p_i, q_i = map(int, input().split())
        matches.append((p_i, q_i))

    # Create a dictionary to store the number of times each player's team wins
    expected_wins = {player: 0 for player in range(1, N + 1)}

    # Calculate the expected wins using dynamic programming
    for i in range(N - 2, -1, -1):
        p_i, q_i = matches[i]
        total_players = N - i

        p_win = pow(total_players, -1, MOD)  # Probability of first team winning
        q_win = pow(total_players, -1, MOD)  # Probability of second team winning

        # Update expected wins for player p_i and player q_i
        expected_wins[p_i] = (expected_wins[p_i] + (p_win + q_win) * (1 + expected_wins[q_i])) % MOD
        expected_wins[q_i] = (expected_wins[q_i] + (p_win + q_win) * (1 + expected_wins[p_i])) % MOD

    # Print the expected number of wins for each player's team
    for player in range(1, N + 1):
        print(expected_wins[player])
if __name__ == "__main__":
    main()