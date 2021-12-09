# populate lanterns
def get_init_lanterns():
    lanterns = []
    with open("input.txt", "r") as timers_file:
        for line in [line.strip() for line in timers_file]:
            lanterns += list(map(int, line.split(",")))
    return lanterns


def babies(timer, simulation_time):
    while simulation_time - timer - 1 > 0:
        simulation_time -= timer + 1
        timer = 6
        yield (8, simulation_time)


def count_recursive_babies(timer, simulation_time, memo):
    if (timer, simulation_time) in memo:
        return memo[(timer, simulation_time)]
    count = 1 + sum(map(lambda x: count_recursive_babies(*x, memo), babies(timer, simulation_time)))
    memo[(timer, simulation_time)] = count
    return count


lanterns = get_init_lanterns()
memo = {}

result = sum(map(lambda t: count_recursive_babies(t, 80 + 1, memo), lanterns))
print(f"After 80 days: {result}")
result = sum(map(lambda t: count_recursive_babies(t, 256 + 1, memo), lanterns))
print(f"After 256 days: {result}")
