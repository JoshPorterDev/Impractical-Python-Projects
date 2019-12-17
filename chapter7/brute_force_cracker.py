import time
from itertools import product

start_time = time.time()

combo = (9, 1, 7, 6, 8, 4, 3)

# Use Cartesian product to generate permutation with repetition
for perm in product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=len(combo)):
    if perm == combo:
        print(f"Cracked! {combo} {perm}")

end_time = time.time()

print(f"\nRuntime for this program was {end_time - start_time} seconds.")
