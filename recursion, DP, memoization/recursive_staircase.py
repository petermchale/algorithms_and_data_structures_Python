# https://www.youtube.com/watch?v=eREiwuvzaUM&list=PLOuZYwbmgZWXvkghUyMLdI90IwxbNCiWK&index=25


# O(3^n) time; O(1) space
def count_paths_recursive(steps):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1
    return count_paths_recursive(steps - 1) + count_paths_recursive(steps - 2) + count_paths_recursive(steps - 3)


def count_paths_memo(steps):
    return count_paths_memo_core(steps, (steps+1)*[-1])


# O(n) time; O(n) space
def count_paths_memo_core(steps, memo):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1
    if memo[steps] == -1:
        memo[steps] = count_paths_memo_core(steps - 1, memo) + count_paths_memo_core(steps - 2, memo) + \
                      count_paths_memo_core(steps - 3, memo)
    return memo[steps]


# O(n) time; O(n) space; but cuts out stack space
def count_paths_DP(steps):  # could label this iterative too
    if steps < 0:
        return 0
    elif steps <= 1:
        return 1
    number_paths = (steps+1)*[-1]
    number_paths[0] = 1
    number_paths[1] = 1
    number_paths[2] = 2
    for i in range(3, steps+1):
        number_paths[i] = number_paths[i-1] + number_paths[i-2] + number_paths[i-3]
    return number_paths[steps]


# O(n) time; O(1) space
def count_paths_iterative(steps):
    if steps < 0:
        return 0
    elif steps <= 1:
        return 1
    number_paths = [1, 1, 2]
    for i in range(3, steps+1):
        count = number_paths[0] + number_paths[1] + number_paths[2]
        number_paths[0] = number_paths[1]
        number_paths[1] = number_paths[2]
        number_paths[2] = count
    return number_paths[2]


def test_count_paths():
    steps = 20
    print 'steps:', steps
    print 'memoization approach:', count_paths_memo(steps)
    print 'recursive approach:', count_paths_recursive(steps)
    print 'DP approach:', count_paths_DP(steps)
    print 'iterative approach:', count_paths_iterative(steps)


if __name__ == '__main__':
    test_count_paths()
