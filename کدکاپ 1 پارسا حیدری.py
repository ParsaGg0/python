def count_n_queens_sets(n: int) -> int:
    cols = set()
    diag = set()   # r - c
    anti = set()   # r + c
    count = 0

    def dfs(r: int):
        nonlocal count
        if r == n:
            count += 1
            return
        for c in range(n):
            if c in cols or (r - c) in diag or (r + c) in anti:
                continue
            cols.add(c)
            diag.add(r - c)
            anti.add(r + c)
            dfs(r + 1)
            cols.remove(c)
            diag.remove(r - c)
            anti.remove(r + c)

    dfs(0)
    return count

if __name__ == "__main__":
    n = int(input().strip())
    print(count_n_queens_sets(n))