import random
import time
import os
import sys

# ======================== Configuration ========================
GRID_HEIGHT = 35
GRID_WIDTH = 80
TIMER_SECONDS = 301  # 5 minutes
# ===============================================================
print('='*150)
print(f'\n\n\nWelcome to your first problem Agent X,\n')
time.sleep(3)
print(f'We have received a cryptic link from an anonymous source who appears to have a personal grudge with a suspect but cannot reveal their identity,\n')
time.sleep(8)
print (f'The link displays the below table appears to contain a random array of dots and dashes, possibly morse code ? but it also has another twist...\n')
time.sleep(8)
print(f'The connection to the link disconnects after 5 minutes, meaningyou will be reconnected with an antirely new grid \n. Our experts have failed to find the correct code and have left you with their Morse Code Table,\n')
time.sleep(10)
print(f'You need to be fast agent, you are our only hope!\n\n\n ')
time.sleep(10)

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/', ':': '---...', '.': '.-.-.-'
}
# Expanded word pool for red herrings
RED_HERRING_WORDS = [
    'FOG','KEY','ASH','SUN','OAK','JET','DOT','RAY','POP','RED',
    'BEE','ICE','CAT','DOG','MOON','STAR','SKY','SEA','TREE','BARK',
    'LEAF','WAVE','FIRE','ROCK','PEAR'
]

# ==================== Utility Functions ========================
def text_to_morse_word(word):
    """Convert a single word to compact Morse code."""
    return ''.join(MORSE_CODE.get(ch.upper(), '?') for ch in word)

def double_space_words(words_list):
    """Convert a list of words to Morse with double spaces between them."""
    morse_words = [text_to_morse_word(word) for word in words_list]
    return '  '.join(morse_words)

def generate_fake_words_line(max_width):
    """Generate a line of random words (red herrings) with double spaces."""
    fake_words = []
    while len(double_space_words(fake_words)) < max_width:
        word = random.choice(RED_HERRING_WORDS)
        fake_words.append(word)
    line = double_space_words(fake_words)
    return line[:max_width]

def generate_random_password(length=5):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

def generate_random_hint():
    word = random.choice(['RED','POP','SUN','JET','OAK','ASH','RAY','MOB','SAD'])
    number = random.randint(10,99)
    return f"{word}{number}"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def beep(times=1, delay=0.2):
    for _ in range(times):
        sys.stdout.write('\a')
        sys.stdout.flush()
        time.sleep(delay)

def display_morse_code_table():
    """Display the Morse code translations clearly."""
    print("\nMORSE CODE TRANSLATIONS:\n")
    items = list(MORSE_CODE.items())
    for i in range(0, len(items), 5):
        line = '   '.join(f"{ch}:{code}" for ch, code in items[i:i+5])
        print(line)
    print("\n" + "="*80 + "\n")

# ==================== Grid Generator ==========================
def generate_grid(password, start_hint, end_hint):
    start_line = random.randint(2, GRID_HEIGHT//3)
    password_line = random.randint(start_line+1, 2*GRID_HEIGHT//3)
    end_line = random.randint(password_line+1, GRID_HEIGHT-2)

    grid = []
    for i in range(GRID_HEIGHT):
        if i == start_line:
            words = ["START", "AT", start_hint]
            line = double_space_words(words)
        elif i == password_line:
            line = double_space_words([password])
        elif i == end_line:
            words = ["END", "AT", end_hint]
            line = double_space_words(words)
        else:
            line = generate_fake_words_line(GRID_WIDTH)

        # Fill remaining characters to exact width if needed
        while len(line) < GRID_WIDTH:
            line += random.choice(['.', '-'])
        grid.append(line[:GRID_WIDTH])
    return grid, start_line, password_line, end_line

# ==================== Main Game Loop ==========================
def play_game():
    while True:
        # Generate a new password and hints each reset
        password = generate_random_password()
        start_hint = generate_random_hint()
        end_hint = generate_random_hint()

        grid, start_line, password_line, end_line = generate_grid(password, start_hint, end_hint)

        clear_screen()
        print("\n----- 🛰️ MORSE GRID PUZZLE -----\n")
        time.sleep(4)
        display_morse_code_table()
        for line in grid:
            print(line)

        print("\n🕒 You have 5 minutes to find the password!\n")
        print(f"Start hint: {start_hint}")
        print(f"End hint: {end_hint}")
        print("\n" + "="*80)
        print("🔑 PASSWORD ENTRY SECTION 🔑")
        print("="*80)

        start_time = time.time()
        end_time = start_time + TIMER_SECONDS

        while True:
            remaining = int(end_time - time.time())
            if remaining <= 0:
                beep(times=3, delay=0.3)
                print("\n⏰ Time's up! Generating new password and hints...\n")
                time.sleep(2)
                break  # Will regenerate password and hints on next loop iteration

            mins, secs = divmod(remaining, 60)
            print(f"\n⏳ Time left: {mins:02}:{secs:02}")
            guess = input("➡ Enter password here: ").strip().upper()

            if guess == password:
                beep(times=2, delay=0.2)
                print("\n✅ Correct! Clue: Tom Carroll never eats in the WGB Cafe.\n")
                return
            else:
                print("❌ Incorrect password, try again.")

if __name__ == "__main__":
    play_game()
