def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    if maximizingPlayer:
        best = -9999
        for i in range(2):
            value = alpha_beta(
                depth + 1,
                nodeIndex * 2 + i,
                False,
                values,
                alpha,
                beta
            )
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 9999
        for i in range(2):
            value = alpha_beta(
                depth + 1,
                nodeIndex * 2 + i,
                True,
                values,
                alpha,
                beta
            )
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
alpha = -9999
beta = 9999
result = alpha_beta(0, 0, True, values, alpha, beta)
print("Optimal value:", result)
