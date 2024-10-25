import numpy as np
def hits_algorithm(adjacency_matrix, max_iter=100, tol=1e-6):
    n = adjacency_matrix.shape[0]
    # Initialize hub and authority scores to 1
    hubs = np.ones(n)
    authorities = np.ones(n)
    for _ in range(max_iter):
    # Update authorities: sum of hub scores of incoming nodes
        new_authorities = adjacency_matrix.T.dot(hubs)
        # Update hubs: sum of authority scores of outgoing nodes
        new_hubs = adjacency_matrix.dot(authorities)
        # Normalize the scores
        new_authorities = new_authorities / np.linalg.norm(new_authorities, 2)

        new_hubs = new_hubs / np.linalg.norm(new_hubs, 2)
    # Check for convergence
        if np.linalg.norm(hubs - new_hubs) < tol and np.linalg.norm(authorities - new_authorities) < tol:
            break
        hubs, authorities = new_hubs, new_authorities
    return hubs, authorities
# Example usage
if __name__ == "__main__":
# Define an adjacency matrix for a small graph
    adjacency_matrix = np.array([[0, 1, 1, 0],
                                [1, 0, 1, 0],
                                [0, 0, 0, 1],
                                [0, 0, 1, 0]])

hubs, authorities = hits_algorithm(adjacency_matrix)

print("Hub Scores:", hubs)
print("Authority Scores:", authorities)