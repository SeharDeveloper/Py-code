from itertools import count, cycle, repeat, product, permutations, combinations, combinations_with_replacement, compress, filterfalse, dropwhile, takewhile, groupby, accumulate, chain, islice, zip_longest
import operator

# 1. Infinite Iterators

# count(start=0, step=1): Generates consecutive numbers indefinitely
for i in count(10, 2):  # Starts at 10, increments by 2
    print(i)  # Output: 10, 12, 14, ...
    if i > 20:
        break

# cycle(iterable): Cycles through the iterable indefinitely
for item in cycle([1, 2, 3]):
    print(item)  # Output: 1, 2, 3, 1, 2, 3, ...
    break  # Break after one cycle for demonstration

# repeat(elem, n): Repeats an element n times
for item in repeat('Hello', 3):
    print(item)  # Output: Hello, Hello, Hello

# 2. Combinatoric Iterators

# product(*iterables, repeat=1): Cartesian product of input iterables
print(list(product([1, 2], ['a', 'b'])))
# Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# permutations(iterable, r=None): All possible r-length permutations
print(list(permutations([1, 2, 3], 2)))
# Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations(iterable, r): All possible r-length combinations
print(list(combinations([1, 2, 3], 2)))
# Output: [(1, 2), (1, 3), (2, 3)]

# combinations_with_replacement(iterable, r): Like combinations, but allows repeated elements
print(list(combinations_with_replacement([1, 2], 2)))
# Output: [(1, 1), (1, 2), (2, 2)]

# 3. Filtering Iterators

# compress(data, selectors): Filters elements based on selectors
data = ['A', 'B', 'C', 'D']
selectors = [1, 0, 1, 0]
print(list(compress(data, selectors)))
# Output: ['A', 'C']

# filterfalse(predicate, iterable): Filters elements where predicate is False
print(list(filterfalse(lambda x: x % 2, range(10))))
# Output: [0, 2, 4, 6, 8]

# dropwhile(predicate, iterable): Drops elements as long as predicate is True
print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 7, 3])))
# Output: [6, 7, 3]

# takewhile(predicate, iterable): Takes elements as long as predicate is True
print(list(takewhile(lambda x: x < 5, [1, 4, 6, 7, 3])))
# Output: [1, 4]

# 4. Grouping Iterators

# groupby(iterable, key=None): Groups consecutive elements with the same value or key
data = [1, 1, 2, 3, 3, 3, 4]
for key, group in groupby(data):
    print(key, list(group))
# Output:
# 1 [1, 1]
# 2 [2]
# 3 [3, 3, 3]
# 4 [4]

# 5. Other Utility Functions

# accumulate(iterable, func=operator.add): Accumulates sums or other operations
print(list(accumulate([1, 2, 3, 4], operator.mul)))
# Output: [1, 2, 6, 24]

# chain(*iterables): Chains multiple iterables into a single sequence
print(list(chain([1, 2], ['a', 'b'])))
# Output: [1, 2, 'a', 'b']

# islice(iterable, start, stop, step=1): Slices an iterable like list slicing
print(list(islice(range(10), 2, 8, 2)))
# Output: [2, 4, 6]

# zip_longest(*iterables, fillvalue=None): Zips two iterables, filling missing values
print(list(zip_longest('AB', '1234', fillvalue='-')))
# Output: [('A', '1'), ('B', '2'), ('-', '3'), ('-', '4')]
