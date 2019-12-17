import time
from random import randint, randrange

def fitness(combo, attempt):
    """ Compare items in two lists and count number of matches. """
    grade = 0
    for i, j in zip(combo, attempt):
        if i == j:
            grade += 1

    return grade

c = (3, 2, 3, 4, 4)
a = (3, 4, 3, 4, 1)

def main():
    """ Use hill-climbing algorithm to solve this lock combination. """
    combination = '12345'
    print(f"Combination = {combination}")
    # Convert combination to list
    combo = [int(i) for i in combination]

    # Generate guess and grade fitness
    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0

    # Evolve guess
    while best_attempt != combo:
        # Crossover
        next_try = best_attempt[:]

        # Mutate
        lock_wheel = int(randrange(0, len(combo)))
        next_try[lock_wheel] = randint(0, len(combo) -1)

        # Grade and select
        next_try_grade = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
        print(next_try, best_attempt)
        count += 1

    print()
    print("Cracked! {}".format(best_attempt), end=' ')
    print(f"In {count} tries!")

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"\nRuntime for this program was {duration} seconds.")
