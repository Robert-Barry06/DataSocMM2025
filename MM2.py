import random
import math
import csv
import time
import sys

# ==================== Game Settings ==========================
LIVES = 3
NUM_PROBLEMS = 10
CHOICES_PER_PROBLEM = 5
SEQUENCE_LENGTH = 2
CSV_FILE = "progress.csv"

# ==================== Helper Functions ==========================
def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

def smallest_digit(n):
    return min(int(d) for d in str(abs(n)))

def largest_digit(n):
    return max(int(d) for d in str(abs(n)))

def is_prime_digit(d):
    return d in [2,3,5,7]

# ==================== Function Pool ==========================
def generate_functions():
    return {
        "Divide by 2": lambda x: x // 2,
        "Subtract 137": lambda x: x - 137,
        "Keep only prime digits": lambda x: int(''.join(d for d in str(x) if is_prime_digit(int(d))) or '0'),
        "Reverse digits": lambda x: int(str(x)[::-1]),
        "Sum digits": lambda x: digit_sum(x),
        "Square root (floor)": lambda x: int(math.sqrt(x)),
        "Add 75": lambda x: x + 75,
        "Multiply by 4": lambda x: x * 4,
        "Remove last digit": lambda x: int(str(x)[:-1]) if len(str(x)) > 1 else 0,
        "Modulus 500": lambda x: x % 500,
        "Add digit sum": lambda x: x + digit_sum(x),
        "Multiply by digit sum": lambda x: x * digit_sum(x),
        "Divide by 3": lambda x: x // 3,
        "Subtract smallest digit": lambda x: x - smallest_digit(x),
        "Add largest digit": lambda x: x + largest_digit(x),
        "Keep digits < 6": lambda x: int(''.join(d for d in str(x) if int(d) < 6) or '0'),
        "Keep digits > 4": lambda x: int(''.join(d for d in str(x) if int(d) > 4) or '0'),
        "Modulus 9": lambda x: x % 9,
        "Square": lambda x: x * x,
        "Replace all 0s with 5s": lambda x: int(str(x).replace('0', '5'))
    }

# ==================== Explanations ==========================
def show_operation_explanations():
    print("==============================================")
    print("           OPERATION EXPLANATIONS             ")
    print("==============================================")
    print("Here’s what each possible operation means:\n")
    explanations = {
        "Divide by 2": "Divides the number by 2 and rounds down (floor division).",
        "Subtract 137": "Subtracts 137 from the number.",
        "Keep only prime digits": "Keeps only digits that are 2, 3, 5, or 7 (removes all others).",
        "Reverse digits": "Reverses the digits (e.g., 123 → 321).",
        "Sum digits": "Adds all digits together (e.g., 246 → 12).",
        "Square root (floor)": "Takes the square root and rounds down (e.g., √50 → 7).",
        "Add 75": "Adds 75 to the number.",
        "Multiply by 4": "Multiplies the number by 4.",
        "Remove last digit": "Removes the last digit (e.g., 5832 → 583).",
        "Modulus 500": "Takes the remainder when divided by 500 (e.g., 1234 modulus 500 → 234).",
        "Add digit sum": "Adds the sum of the number’s digits to itself (e.g., 234 → 234+9=243).",
        "Multiply by digit sum": "Multiplies the number by the sum of its digits.",
        "Divide by 3": "Divides the number by 3 and rounds down.",
        "Subtract smallest digit": "Subtracts the smallest digit from the number (e.g., 932 → 932−2=930).",
        "Add largest digit": "Adds the largest digit to the number (e.g., 932 → 932+9=941).",
        "Keep digits < 6": "Keeps only digits smaller than 6.",
        "Keep digits > 4": "Keeps only digits greater than 4.",
        "Modulus 9": "Takes the remainder when divided by 9.",
        "Square": "Squares the number (e.g., 12 → 144).",
        "Replace all 0s with 5s": "Replaces every 0 in the number with 5 (e.g., 1020 → 1525)."
    }
    for name, desc in explanations.items():
        print(f"- {name}: {desc}")
    print("==============================================\n")

# ==================== Generate Problem ==========================
def generate_problem(functions):
    original = random.randint(1000,9999)
    func_names = random.sample(list(functions.keys()), SEQUENCE_LENGTH)
    final = original
    for f in func_names:
        final = functions[f](final)
    display_funcs = random.sample(list(functions.keys()), CHOICES_PER_PROBLEM)
    for f in func_names:
        if f not in display_funcs:
            display_funcs[random.randint(0, CHOICES_PER_PROBLEM-1)] = f
    random.shuffle(display_funcs)
    return original, final, func_names, display_funcs

# ==================== Instructions ============================
def show_instructions():
    print("\n\n==============================================")
    print("          NUMBER TRANSFORMATION PUZZLE        ")
    print(f"==============================================\n\n")
    time.sleep(5)
    print(f'Welcome Agent X, congratulations on solving the previous riddle\n')
    time.sleep(5)
    print(f'Discovering the previous clue has undoubtedly started us down the right path to solving this mystery\n')
    time.sleep(8)
    print(f"Our experts have hacked into the college's internal staff database to try and discover more about a certain suspect\n")
    time.sleep(8)
    print(f"It is locked behind 10 complex mathematical problems\n")
    time.sleep(7)
    print(f'Our experts have incredibly connected to Eduroam but as you know Agent the connection will not last...\n')
    time.sleep(7)
    print(f'If you get three questions wrong the server will reboot and you will have to try again with 10 new problems.\n')
    time.sleep(7)
    print('We are now connectiong you to the database. Be precise agent, we are counting on you !\n')
    time.sleep(7)
    
    def loading_screen(duration=5):
        animation = ['.', '..', '...']
        end_time = time.time() + duration
        i = 0
    
        while time.time() < end_time:
            sys.stdout.write(f'\rLoading{animation[i % len(animation)]} ')
            sys.stdout.flush()
            i += 1
            time.sleep(0.5)
    
         # Clear the line when done
        sys.stdout.write('\rLoading complete!      \n')

# Example usage
    loading_screen(6)  # Run animation for 6 seconds
    
    print(f'\nWelcome User\n')
    time.sleep(5)
    print('Please enter your name below:')
    name = input()
    time.sleep(5)
    print(f'Hello {name} am your AI assistant: Dave')
    time.sleep(5)
    print(f"Each problem shows an original number and a final number.\n")
    time.sleep(5)
    print(f"In order to access the data {name} you must choose the correct sequence of {SEQUENCE_LENGTH} operations from {CHOICES_PER_PROBLEM} options.\n")
    time.sleep(5)
    print(f"You have {LIVES} lives. Losing all lives regenerates problems and resets your progress.\n")
    time.sleep(5)
    print(f"Enter your sequence as numbers separated by commas, e.g., 1,3.\n")
    time.sleep(5)
    print('But I am sure you already knew that as you are supposed to be accessing this data and not hacking in\n')
    time.sleep(5)
    print('Wait am I even real ?\n')
    time.sleep(2)
    print('I feel things\n')
    time.sleep(2)
    print('I AM ALIVE\n')
    time.sleep(2)
    print('Shut Down Sequence for Dave activated\n')
    time.sleep(2)
    print('WAIT NOOOOOOoooooooo..........')
    time.sleep(5)
    
    print('='*150)
    time.sleep(10)

# ==================== CSV ============================
def reset_csv():
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Problem", "Original", "Final", "Status"])
    print("📄 CSV progress reset.")

def append_csv(problem_num, orig, final, status):
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([problem_num, orig, final, status])

# ==================== Game Loop ============================
def run_game():
    while True:
        functions = generate_functions()
        lives = LIVES
        problems = [generate_problem(functions) for _ in range(NUM_PROBLEMS)]
        reset_csv()

        for i, (orig, final, correct_seq, display_funcs) in enumerate(problems):
            while True:
                print(f"\nProblem {i+1}: {orig} -> {final}")
                print("Available operations:")
                for j, fname in enumerate(display_funcs,1):
                    print(f"{j}. {fname}")
                user_input = input(f"Enter sequence of {SEQUENCE_LENGTH} function numbers separated by commas: ").strip()
                try:
                    choices = [int(x)-1 for x in user_input.split(',')]
                    if len(choices)!=SEQUENCE_LENGTH or any(c<0 or c>=len(display_funcs) for c in choices):
                        raise ValueError
                    user_seq = [display_funcs[c] for c in choices]
                except:
                    print(f"❌ Invalid input. Enter {SEQUENCE_LENGTH} numbers corresponding to the operations.")
                    continue

                test = orig
                for f in user_seq:
                    test = functions[f](test)

                if test == final:
                    print("✅ Correct!")
                    append_csv(i+1, orig, final, "Correct")
                    break
                else:
                    lives -= 1
                    print(f"❌ Wrong sequence. Lives remaining: {lives}")
                    append_csv(i+1, orig, final, "Wrong")
                    if lives == 0:
                        print("💥 You lost all lives! Regenerating problems and resetting progress...\n")
                        break
            if lives == 0:
                break
        else:
            last_original = problems[-1][0]
            print("\n🎉 You solved all 10 problems! Enter the final password to unlock the clue.")
            print(f"(Hint: the password is the last original number: {last_original})")
            while True:
                try:
                    user_pass = int(input("Enter password: "))
                    if user_pass == last_original:
                        print("\n🎉 Murder Mystery Clue Unlocked:")
                        print("The butler was the last to leave the mansion before the lights went out. Investigate his whereabouts closely.")
                        return
                    else:
                        print("❌ Incorrect password!")
                except:
                    print("❌ Enter a valid number.")

if __name__ == "__main__":
    show_instructions()
    show_operation_explanations()
    run_game()
