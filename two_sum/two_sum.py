nums = [-1, -2, -3, -4, -5]
target = -8


def split_evens_odds(nums_sorted: list) -> tuple[list, list]:
    evens = []
    odds = []
    for num in nums_sorted:
        if num % 2 == 0:
            evens.append(num)
            continue
        odds.append(num)
    return (evens, odds)


def add_even_to_odd(nums: list, evens: list, odds: list, target: int) -> list | None:
    for even in evens:
        for odd in odds:
            solution_sum = even + odd
            if solution_sum == target:
                return [nums.index(even), nums.index(odd)]
    return None


def unique_add_list(nums: list, to_add: list, target: int) -> list | None:
    length = len(to_add)
    for i in range(length):
        for j in range(i + 1, length):
            solution_sum = to_add[i] + to_add[j]
            if solution_sum == target:
                # If the solution includes two identical numbers, looking them
                # up by index in this manner solves this.
                if to_add[i] == to_add[j]:
                    index1 = nums.index(to_add[i])
                    index2 = nums.index(to_add[j], index1 + 1)
                    return [index1, index2]
                return [nums.index(to_add[i]), nums.index(to_add[j])]
    return None


def solve_two_sum(nums, target):
    # First determine if the target is odd. If it is, then we know we need to
    # add an even number to an odd number.
    target_odd = target % 2
    # Split the list of numbers into evens and odds, leaving out any numbers
    # that are greater than the target.
    nums_sorted = sorted(nums)  # Create a copy of the nums list sorted
    evens, odds = split_evens_odds(nums_sorted)
    if target_odd:
        # Since the target is odd, we know the answer will be here.
        answer = add_even_to_odd(nums, evens, odds, target)
        return answer
    else:
        # Check adding evens to themselves, and if that doesn't work, then
        # answer will be two odds added together.
        evens_answer = unique_add_list(nums, evens, target)
        if evens_answer != None:
            return evens_answer
        odds_answer = unique_add_list(nums, odds, target)
        return odds_answer


answer = solve_two_sum(nums, target)
print(answer)
