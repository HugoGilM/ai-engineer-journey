nums = [3, 1, 2]
nums.append(4)  # Add
nums.extend([5, 6])  # AddRange
nums.insert(0, 99)  # Insert
nums.pop()  # removes and returns the last item (pop(0) removes the first)
nums.remove(99)  # removes the first matching value; raises ValueError if it's missing
len(nums), 2 in nums  # Count, Contains
nums[-1], nums[1:3]  # indexing and slicing work exactly like strings

nums.sort()  # sorts in place and returns None
new = sorted(nums)  # returns a new list, like OrderBy().ToList()


ages = {"ana": 30, "luis": 25}
ages["eva"] = 28  # add or overwrite
# ages["zoe"]  # KeyError if the key is missing (C# throws KeyNotFoundException)
ages.get("zoe", 0)  # 0 -> like GetValueOrDefault
"ana" in ages  # ContainsKey; don't write `in ages.keys()`
for name, age in ages.items():  # like foreach (var (k, v) in dict)
    print(name, age)


a = {1, 2, 3}
b = {2, 3, 4}
a | b, a & b, a - b  # union, intersection, difference


print(a | b, a & b, b - a)
