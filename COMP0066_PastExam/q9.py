import random


def guess_number():
    count = 0
    lower_bound = 0
    upper_bound = 21
    while True:
        if lower_bound == upper_bound:
            break
        num = random.randrange(lower_bound, upper_bound, 1)
        is_ans = input(f"Is it {num}?\n")
        if is_ans.lower() == "yes":
            break
        elif is_ans.lower() == "no":
            while True:
                high_or_low = input("higher or lower?\n")
                if high_or_low.lower() == "lower":
                    upper_bound = num
                    break
                elif high_or_low.lower() == "higher":
                    lower_bound = num + 1
                    break
                else:
                    print("please answer higher or lower only")
        else:
            print("please answer yes or no only")
        count += 1
    print(f"It took me {count+1} try!"
          f"\nThanks for playing!")


guess_number()
