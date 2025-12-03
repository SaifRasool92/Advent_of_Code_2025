
def max_joltage_from_bank(bank_line: str) -> int:
    """
    Given a string of digits, pick two digits (in order)
    that form the largest possible number.
    """
    max_val = 0
    n = len(bank_line)
    for i in range(n - 1):
        for j in range(i + 1, n):
            num = int(bank_line[i] + bank_line[j])
            if num > max_val:
                max_val = num
    return max_val


def total_max_joltage(path="input.txt") -> int:
    total = 0
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                total += max_joltage_from_bank(line)
    return total


if __name__ == "__main__":
    print(total_max_joltage("input.txt"))
