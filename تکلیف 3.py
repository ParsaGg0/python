def my_process(num):
    steps = []
    while num != 6174:
        digits = f"{num:04d}"
        big = int("".join(sorted(digits, reverse=True)))
        small = int("".join(sorted(digits)))
        num = big - small
        steps.append(num)
    return steps

print(my_process(3524))