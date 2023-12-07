import random
import time

def dice_simulation(num_simulations, num_dice):
    results = {}

    for _ in range(num_simulations):
        ## we are creating a simulated dice array like [1,2,4,3,1] using list comprehension
        dice = [random.randint(1, 6) for _ in range(num_dice)]

        total_score = 0
        while dice:
            if 3 in dice:
                # Remove all 3's
                dice = [d for d in dice if d != 3]
                total_score += 0  # Score 0 for this roll
            else:
                ## In the question it is not clearly mentioned what will happen if we have multiple lowest die like [2,1,4,1,1]
                ## I added both solution where first solution only remove single lowest die and second one remove all lowest dies 
                
                # first solution -Remove only one of the lowest dice
                min_die = min(dice)
                min_die_index = dice.index(min_die)
                total_score += min_die
                del dice[min_die_index]

                ## second solution
                ## if we want to remove all lowest dies(assuming multiple lowest die appear like [2,1,5,1,2], here 1 appear 2 time and we delete both 1)
                # Remove all the lowest die
                # min_die = min(dice)
                # min_die_count = dice.count(min_die)
                # total_score += min_die * min_die_count
                # dice.remove(min_die)

            # Re-throw the remaining dice
            dice = [random.randint(1, 6) for _ in range(len(dice))]

        if total_score not in results:
            results[total_score] = 1
        else:
            results[total_score] += 1

    return results

def print_simulation_results(results, num_simulations, num_dice, elapsed_time):
    print(f"Number of simulations was {num_simulations} using {num_dice} dice.")
    for score, count in sorted(results.items()):
        percentage = count / num_simulations 
        print(f"Total {score} occurs {percentage} occurred {count} times.")

    print(f"Total simulation took {elapsed_time:.1f} seconds.")

if __name__ == "__main__":
    num_simulations = 10000
    num_dice = 5

    start_time = time.time()
    results = dice_simulation(num_simulations, num_dice)
    elapsed_time = time.time() - start_time

    print_simulation_results(results, num_simulations, num_dice, elapsed_time)