
PI = 3.14
def my_sum(a):
    s = a[0]
    for value in a[1:]:
        s = s+value
    return s
print my_sum([1, 2, 3]), PI