import numpy as np
import numpy as np
def pagerank(M, damping_factor=0.85, tol=1e-6):
     
     N = M.shape[1] # Total number of pages
     rank = np.ones(N) / N # Initial rank for each page, equally distributed
     teleport = np.ones(N) / N # Teleportation (uniform distribution)
     print(teleport)
     while True:
         new_rank = (1 - damping_factor) * teleport + damping_factor * M @ rank

         if np.linalg.norm(new_rank - rank, ord=1) < tol: # Convergence check
             break
         rank = new_rank
     return new_rank
    # Example usage:
if __name__ == "__main__":
    # Example adjacency matrix
    # Each column corresponds to a page, each row indicates links to it.
    M=np.array([[0, 0, 1, 0],

    [0.5, 0, 0, 0],
    [0.5, 0, 0, 1],
    [0, 1, 0, 0]])

    # Normalize columns to ensure stochastic matrix
    #M = M / M.sum(axis=0)
    print(M)
    # Compute PageRank with damping factor and teleportation
    pagerank_values = pagerank(M, damping_factor=0.85)
    print("PageRank values:", pagerank_values)
        
   