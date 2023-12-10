def finger_conversion():
    count = 0
    while True:
        n = input("Please enter an integer representing the length in fingers: ")
        try:
            n = int(n)
        except ValueError:
            print("\nInvalid integer!")
            continue
        if n == 0:
            break
        cubit = n // (4 * 7)
        n -= cubit * 4 * 7
        palm = n // 4
        n -= palm * 4
        print(f"C:P:F = {cubit}:{palm}:{n}")
        count += 1
    print(f"Number of times the conversion has been performed: {count}")

finger_conversion()