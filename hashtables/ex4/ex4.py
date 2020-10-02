def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for el in a:
        if abs(el) not in cache:
            cache[abs(el)] = 0
        cache[abs(el)] += 1
    for el, count in cache.items():
        if count == 2:
            result.append(int(el))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
