from dice import Dice

# Create a D6
dice = Dice()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):  # 1
    result = dice.roll()
    results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(1, dice.num_sides + 1)  # 2
for value in poss_results:
    frequency = results.count(value)  # 3
    frequencies.append(frequency)  # 4

print(frequencies)

# Because we’re no longer printing the results, we can increase the number of simulated rolls to 1000 ❶. To analyze the rolls, we create the empty list frequencies to store the number of times each value is rolled. We then generate all the possible results we could get; in this example, that’s all the numbers from 1 to however many sides die has ❷. We loop through the possible values, count how many times each number appears in results ❸, and then append this value to frequencies ❹.
