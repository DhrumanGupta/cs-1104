def soln(n):
    return -7 * (n**3) - 42 * (n**2) + 210 * (n) + 518 + 2 ** (n + 1)


def main():
    a = [2]
    for i in range(1, 10):
        a_i = 2 * a[i - 1] + 7 * (i**3)
        print(f"a_{i} = {a_i}")
        print(f"soln({i}) = {soln(i)}")
        a.append(a_i)


if __name__ == "__main__":
    main()
