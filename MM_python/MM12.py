#!/usr/bin/env python3
import random, textwrap, time, sys

# ---------- Color Codes ----------
class Colors:
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    RED = '\033[91m'
    RESET = '\033[0m'

WRAP = 78

# ---------- Print and Pause ----------
def print_delayed(text, color=None, delay=0.001):
    if color:
        text = color + text + Colors.RESET
    for line in textwrap.wrap(text, WRAP):
        print("\n" + line)
        time.sleep(delay)

def pause(seconds=4):
    time.sleep(seconds)

# ---------- Witty statements ----------
WITTY_STATEMENTS = [
    "'I should have been a cat; nine lives would help in this line of work.'",
    "'Nothing like paperwork and murder to start the day.'",
    "'If I stare at this chair long enough, maybe it will confess.'",
    "'I didn’t choose the detective life; the detective life chose me.'",
    "'Another clue? Or just a dust bunny pretending to be one?'",
    "I’d like to interrogate my coffee next—it’s been acting suspicious.'",
    "'I’m starting to think the victim had enemies in low places… everywhere.'",
    "'If only criminals read manuals, this would be easier.'",
    "'Why is the fridge always hiding secrets?'",
    "'Yes, I’m talking to a plant. No, it hasn’t admitted anything yet.'",
    "'I love a good murder mystery, said no one ever before 7 AM.'",
    "'I hope the killer left a Yelp review of their plan. It might help.'",
    "'I’ve inspected chairs, tables, and now my patience.'",
    "'At least the houseplants aren’t accusing me back.'",
    "'If only my life came with hints and a skip button.'",
    "'I’m detecting more dust than clues today.'",
    "'Is it paranoia if everyone really is suspicious?'",
    "'The safe laughs at me silently.'",
    "'Why do criminals always use knives? Aren’t blunt objects more fun?'",
    "'At least no one’s hidden the coffee… yet.'",
    "'Sometimes I wonder if the victim staged this for attention.'",
    "'I’m beginning to think the chandelier knows more than me.'",
    "'Another day, another convoluted murder mystery.'",
    "'If only suspects talked as much as my conscience.'",
    "'I didn’t choose the detective life; it chose me. And my coffee consumption.'",
    "'This journal might be more dramatic than any TV show I’ve watched.'",
    "'I think the chairs are plotting against me.'",
    "'Patience is a virtue; clues are not.'",
    "'I’ll take a break… said no detective ever.'",
    "'I bet the candlestick has a better alibi than most suspects.'"
]

def witty_comment():
    if random.random() < 0.25:
        print_delayed(random.choice(WITTY_STATEMENTS), Colors.CYAN)

# ---------- Game Data ----------
MOTIVES = {
    'money': 'Financial desperation or debt owed.',
    'revenge': 'Get back at the victim for past wrongs.',
    'jealousy': 'Envy of victim’s success or relationships.',
    'coverup': 'Needed to hide a secret the victim knew.',
    'love_triangle': 'Romantic feelings entangled with the victim.'
}

MOTIVE_STORIES = {
    'money': "Driven by financial desperation, the suspect could no longer tolerate debts owed to the victim. Every transaction, every unpaid loan became a source of simmering anger.",
    'revenge': "Years ago, the victim betrayed the suspect by stealing an important contract. The grudge festered quietly until it erupted into violence.",
    'jealousy': "The suspect envied the victim’s wealth, charm, and influence. Every achievement of the victim deepened the suspect's resentment until it became unbearable.",
    'coverup': "The victim had uncovered a secret that could ruin the suspect’s reputation or career. The suspect felt the only way to protect themselves was to silence the victim.",
    'love_triangle': "Romantic tension spiraled out of control. The suspect’s feelings, tangled with the victim and another party, ultimately drove them to a tragic decision."
}

WEAPONS = ['knife', 'poison', 'briefcase', 'rope', 'candlestick']

SUSPECTS_DATA = {
    'trevor': {'name': 'TREVOR VALE', 'role': 'Brother', 'intro': 'A brooding man with a gambling streak.'},
    'emma': {'name': 'EMMA HARROW', 'role': 'Assistant', 'intro': 'Graceful and composed, tending plants.'},
    'lyle': {'name': 'DR. ARTHUR LYLE', 'role': 'Physician', 'intro': 'Calm, scholarly; checking his medical bag.'},
    'marcus': {'name': 'MARCUS FINCH', 'role': 'Courier', 'intro': 'Always in a hurry, seems to know everyone’s business.'},
    'vanessa': {'name': 'VANESSA CROSS', 'role': 'Neighbor', 'intro': 'Observant and sharp, often visiting the estate.'},
    'gerald': {'name': 'GERALD STONE', 'role': 'Lawyer', 'intro': 'Smooth talker, fond of legal maneuvering.'}
}

ROOM_ASSIGNMENT = {
    'trevor': 'kitchen',
    'emma': 'conservatory',
    'lyle': 'guest',
    'marcus': 'office',
    'vanessa': 'study',
    'gerald': 'study'
}

ROOM_ITEMS = {
    'study': [
        {'name':'Desk','desc':'A grand oak desk dominates the room, cluttered with letters and papers. Dust and old ink smell.','clue_id':'desk_note','clue_text':'A note hints at tension with the victim.'},
        {'name':'Bookshelf','desc':'Rows of dusty books, some open to underlined passages.','clue_id':'bookshelf_note','clue_text':'Some books seem out of place.'},
        {'name':'Fireplace','desc':'Cold ashes, a half-burned matchstick. Faint smell of smoke.'},
        {'name':'Chair','desc':'Worn leather chair with faint red stains. Creaks when moved.','clue_id':'chair_stain','clue_text':'Could indicate blood or wine.'},
        {'name':'Window','desc':'Slightly ajar, a chill breeze. Curtains askew, garden shadows visible.'}
    ],
    'kitchen': [
        {'name':'Knife Block','desc':'Knives neatly placed; one missing. Metallic scent.','clue_id':'missing_knife','clue_text':'Possibly the murder weapon.'},
        {'name':'Oven','desc':'Warm, remnants of dinner remain. Aroma of spices.'},
        {'name':'Tea Cup','desc':'Porcelain cup with dark liquid traces. Smells like valerian tea.','clue_id':'tea_cup','clue_text':'Possible sedative used.'},
        {'name':'Fridge','desc':'Quiet hum; magnets hold notes, photo of couple. Vial hidden inside.','clue_id':'fridge_note','clue_text':'Hidden recipe clue!','puzzle':True,'solution':'APPLE'},
        {'name':'Apron','desc':'Cotton apron with flour and faint stains.','clue_id':'apron_stain','clue_text':'Stains suggest cooking or violence.'}
    ],
    'conservatory': [
        {'name':'Plants','desc':'Tropical plants, orchids. Scent of wet soil and flowers.'},
        {'name':'Dual Teacups','desc':'Two cups, one warm. Herbs faintly smell.','clue_id':'dual_teacups','clue_text':'Someone drank recently.'},
        {'name':'Window','desc':'Cracked glass, sunlight streams in, vines outside.'},
        {'name':'Journal','desc':'Emma’s diary, detailed handwriting shows resentment.','clue_id':'journal','clue_text':'Hints at motive.','puzzle':True,'solution':'LOVE'},
        {'name':'Letter','desc':'Folded letter about debts and meetings.','clue_id':'letter','clue_text':'Suggests financial dealings.'}
    ],
    'office': [
        {'name':'Ledgers','desc':'Pages with numbers and notes. Ink and paper smell strong.','clue_id':'ledger','clue_text':'Shows debts and transactions.'},
        {'name':'Desk','desc':'Worn desk with scattered papers and small drawer.'},
        {'name':'Safe','desc':'Heavy safe, scratched lock. Metallic scent.','clue_id':'safe_puzzle','clue_text':'Hidden letter inside.','puzzle':True,'solution':'0420'},
        {'name':'Documents','desc':'Torn contracts and letters hint at cover-ups.','clue_id':'documents','clue_text':'Suggests a cover-up.'},
        {'name':'Clock','desc':'Ornate clock ticks. Hands frozen at significant time.'}
    ],
    'guest': [
        {'name':'Medical Bag','desc':'Leather bag with vials and syringes. Some compartments recently disturbed.'},
        {'name':'Bed','desc':'Neatly made with slight pillow indentation. Lavender scent lingers.'},
        {'name':'Ampoule','desc':'One ampoule missing contents. Broken fragments nearby.','clue_id':'missing_ampoule','clue_text':'Could indicate poisoning.'},
        {'name':'Envelope','desc':'Courier envelope with smudged fingerprints.','clue_id':'envelope','clue_text':'Links suspect to victim.'},
        {'name':'Journal','desc':'Dr. Lyle’s notes on victim behavior and health.'}
    ]
}

# ---------- Intro ----------
def intro_story():
    print("\nIt’s a foggy evening when your phone buzzes on the desk, you sigh audibly as you reach for it.", Colors.CYAN)
    time.sleep(5)
    print("\n'Detective X here. I am on holiday, what's the problem ?'\n", Colors.RED)
    time.sleep(5)
    print("'This is the Police Chief, there has been a murder in downtown at the Harrow Mansion. I need you there ASAP'",Colors.CYAN)
    time.sleep(5)
    print("\n[Must be serious I think to myself]'I'll be there in 20 Chief'\n", Colors.RESET)
    time.sleep(5)
    print("\nYou grab your coat, hat, and trusty notebook, feeling the weight of another case rest heavy on your shoulders.")
    time.sleep(5)
    print("\nThe streets glisten with rain as you make your way to the mansion, the road is long and winding, speaking to the wealth of the area.")
    time.sleep(5)
    print("\nYou arrive at the mansion and open its large sweeping doors, time to go to work, Detective X.\n")
    witty_comment()
    time.sleep(5)
    print('You start your investigation in the study.')
    time.sleep(5)
    print('\nYou are Detective X, called to solve a murder at the Mansion. Your goal is:\n 1. Explore all rooms (study, kitchen, conservatory, office, guest). \n 2. Inspect items to find clues, some hidden behind interactive puzzles.\n 3. Collect clues into your inventory—each clue can only be collected once.\n 4. Interrogate suspects, paying attention to their emotional tone (happy, sad, worried, aggressive).\n 5. Deduce the killer, the weapon, and the motive using the clues you’ve gathered.\n 6. Accuse carefully—you only get a gentle hint after three wrong attempts.\n 7. Solve the case by accusing the correct suspect with the correct weapon and motive!\n\n')
    time.sleep(15)

# ---------- Game Class ----------
class Game:
    def __init__(self):
        # ---------- Initialization ----------
        self.suspects = list(SUSPECTS_DATA.keys())
        self.victim = random.choice(self.suspects)
        remaining = [s for s in self.suspects if s != self.victim]
        self.killer = random.choice(remaining)
        self.motive = random.choice(list(MOTIVES.keys()))
        self.weapon = random.choice(WEAPONS)
        print_delayed(f"\nThe victim was {SUSPECTS_DATA[self.victim]['name']}, found dead earlier this evening at the Harrow Mansion.", Colors.RED)
        time.sleep(5)
        print_delayed("The air is thick with suspicion — every face hides a secret.", Colors.MAGENTA)
        time.sleep(3)
        self.current_room = 'study'
        self.clues_found = set()
        self.clue_inventory = {}
        self.guess_attempts = 0
        self.questions_asked = {}
        self.suspect_questions = {s:[
            f"What were you doing on the day of the murder?",
            f"Did you notice anyone acting suspicious around the {ROOM_ASSIGNMENT[s]}?",
            f"How did you feel about {self.victim.upper()}?",
            f"Do you know anything about the {self.weapon}?",
            f"Did you have any reason to harm {self.victim.upper()}?"
        ] for s in self.suspects}
        self.relationships = {s: random.choice(['friendly','tense','neutral']) for s in self.suspects}

        # Each suspect has an alibi — truthful unless they’re the killer
        self.alibis = {}
        rooms = list(ROOM_ITEMS.keys())
        for s in self.suspects:
            if s == self.killer:
                self.alibis[s] = random.choice([
                    "I was alone, taking a walk — no one saw me.",
                    "I stepped out for some air; I don’t remember where exactly.",
                    f"I think I was in the {random.choice(rooms)}, but I can’t be sure.",
                    "Just... around. Does it matter?"
                ])
            else:
                self.alibis[s] = random.choice([
                    f"I was in the {ROOM_ASSIGNMENT[s]}, talking with someone.",
                    "I was cleaning up after dinner, several people saw me.",
                    "I was reading near the fireplace; others can confirm.",
                    "I was sorting papers in the office — I never left."
                ])
        self.main_menu()

    # ---------- Main Menu ----------
    def main_menu(self):
        while True:
            time.sleep(3)
            witty_comment()
            print("\nMenu: \n1) Move Rooms \n2) Inspect Room \n3) Interrogate Suspect \n4) Accuse suspect  \n5) Review Clues \n6) Quit (this will reset your progress)", Colors.YELLOW)
            choice = input("\nChoose an action detective (1,2,3,4,5,6): ")
            if choice=='1': self.move_rooms()
            elif choice=='2': self.inspect_room()
            elif choice=='3': self.interrogate()
            elif choice=='4': self.accuse()
            elif choice=='5': self.review_clues()
            elif choice=='6':
                print_delayed("\nExiting game. Goodbye, Detective X.", Colors.RED)
                sys.exit()
            else: print_delayed("\nInvalid option.", Colors.RED)

    # ---------- Move Rooms ----------
    def move_rooms(self):
        print("\nRooms: study, kitchen, conservatory, office, guest", Colors.MAGENTA)
        room = input("\nEnter room to go(e.g.'study'): ").lower()
        if room in ROOM_ITEMS:
            self.current_room = room
            print_delayed(f"\nYou move to the {room}. The air feels different here.", Colors.CYAN)
            time.sleep(2)

            # Show suspects in the room
            suspects_here = [s for s in self.suspects if ROOM_ASSIGNMENT[s] == self.current_room]
            if suspects_here:
                print_delayed("\nSuspects present in the room:", Colors.MAGENTA)
                for s in suspects_here:
                    print_delayed(f"- {SUSPECTS_DATA[s]['name']} ({SUSPECTS_DATA[s]['role']})", Colors.YELLOW)
            else:
                print_delayed("\nNo suspects present here.", Colors.RED)

            witty_comment()
            time.sleep(3)
        else:
            print_delayed("\nUnknown room.", Colors.RED)

    # ---------- Inspect Room ----------
    def inspect_room(self):
        while True:
            items = ROOM_ITEMS[self.current_room]
            print_delayed("\nItems in room:", Colors.MAGENTA)
            for i, item in enumerate(items):
                print_delayed(f"{i+1}) {item['name']}", Colors.YELLOW)
            print_delayed(f"{len(items)+1}) Return to center of room", Colors.YELLOW)
            choice = input("\nChoose item number to inspect (1,2,3...): ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(items):
                    self.inspect_item(items[choice-1])
                elif choice == len(items)+1:
                    return
                else:
                    print_delayed("\nInvalid choice.", Colors.RED)
            else:
                print_delayed("\nInvalid input.", Colors.RED)

    def inspect_item(self, item):
        print_delayed(f"\nYou inspect {item['name']}: {item['desc']}", Colors.CYAN)
        time.sleep(3)
        clue_id = item.get('clue_id')
        if clue_id:
            if clue_id in self.clues_found:
                print_delayed(f"\nThis clue is already in your inventory: {self.clue_inventory[clue_id]}", Colors.YELLOW)
            else:
                self.clues_found.add(clue_id)
                self.clue_inventory[clue_id] = item['clue_text']
                print_delayed(f"\nClue found: {item['clue_text']}", Colors.YELLOW)
                time.sleep(3)
            if item.get('puzzle'):
                self.solve_puzzle(item)

    def solve_puzzle(self, item):
        attempts = 0
        while attempts < 3:
            answer = input(f"\nPuzzle! Enter solution for {item['name']}: ").strip().upper()
            if answer == item['solution']:
                print_delayed(f"\nPuzzle solved! Clue confirmed: {item['clue_text']}", Colors.YELLOW)
                time.sleep(3)
                return
            else:
                print_delayed("\nIncorrect.", Colors.RED)
                attempts += 1
        print_delayed(f"\nHint: The solution contains {len(item['solution'])} characters.", Colors.CYAN)

    # ---------- Review Clues ----------
    def review_clues(self):
        if self.clues_found:
            print_delayed("\nClues collected:", Colors.MAGENTA)
            for c in self.clues_found:
                print_delayed(f"- {self.clue_inventory[c]}", Colors.YELLOW)
                time.sleep(3)
        else:
            print_delayed("\nNo clues collected yet.", Colors.RED)



     # ---------- Interrogate ----------
    def interrogate(self):
        suspects_here = [s for s in self.suspects if ROOM_ASSIGNMENT[s] == self.current_room]
        if not suspects_here:
            print_delayed("\nNo one to interrogate here.", Colors.RED)
            return

        print_delayed("\nSuspects here:", Colors.MAGENTA)
        for i, s in enumerate(suspects_here):
            print_delayed(f"{i+1}) {SUSPECTS_DATA[s]['name']}", Colors.YELLOW)

        choice = input("\nChoose suspect number: ")
        if not (choice.isdigit() and 1 <= int(choice) <= len(suspects_here)):
            print_delayed("\nInvalid suspect choice.", Colors.RED)
            return

        suspect = suspects_here[int(choice) - 1]
        questions = self.suspect_questions[suspect]

        print_delayed(f"\nQuestions for {SUSPECTS_DATA[suspect]['name']} (type 'quit' to stop):", Colors.MAGENTA)
        for i, q in enumerate(questions):
            print_delayed(f"{i+1}) {q}", Colors.YELLOW)
        print_delayed(f"{len(questions) + 1}) Ask for their alibi", Colors.YELLOW)

        while True:
            q_choice = input("\nChoose question number (or 'quit' to stop): ").lower().strip()
            if q_choice == "quit":
                print_delayed(f"\nYou end the interrogation with {SUSPECTS_DATA[suspect]['name']}.", Colors.MAGENTA)
                break

            if not q_choice.isdigit():
                print_delayed("\nInvalid input.", Colors.RED)
                continue

            q_choice = int(q_choice)

            # Normal question response
            if 1 <= q_choice <= len(questions):
                q = questions[q_choice - 1]
                print_delayed(f"\nYou ask: {q}", Colors.YELLOW)
                time.sleep(2)

                # Generate random emotional tone
                tone = random.choice(['neutral', 'happy', 'sad', 'worried', 'aggressive'])
                answer = f"{SUSPECTS_DATA[suspect]['name']} responds: 'I prefer not to say.'"

                # Add emotional tone flavor
                if tone == 'happy':
                    answer += " They seem unusually cheerful while speaking."
                elif tone == 'sad':
                    answer += " Their voice is low and heavy with sadness."
                elif tone == 'worried':
                    answer += " They glance around nervously as they speak."
                elif tone == 'aggressive':
                    answer += " Their tone is sharp and confrontational."

                print_delayed(answer, Colors.CYAN)
                witty_comment()

            # Alibi option
            elif q_choice == len(questions) + 1:
                alibi = self.alibis[suspect]
                print_delayed(f"\n{SUSPECTS_DATA[suspect]['name']} says: '{alibi}'", Colors.CYAN)
                witty_comment()

            else:
                print_delayed("\nInvalid question choice.", Colors.RED)

    # ---------- Accuse ----------
    def accuse(self):
        print_delayed("\nSuspects:", Colors.MAGENTA)
        for i, s in enumerate(self.suspects):
            print_delayed(f"{i+1}) {SUSPECTS_DATA[s]['name']}", Colors.YELLOW)

        try:
            s_choice = int(input("\nWho is the killer? Enter number: "))
            suspect = self.suspects[s_choice - 1]
        except:
            print_delayed("\nInvalid suspect.", Colors.RED)
            return

        w_choice = input(f"\nWeapon? Options: {', '.join(WEAPONS)}: ").strip().lower()
        m_choice = input(f"\nMotive? Options: {', '.join(list(MOTIVES.keys()))}: ").strip().lower()

        self.guess_attempts += 1
        correct = sum([suspect == self.killer, w_choice == self.weapon, m_choice == self.motive])

        if correct == 3:
            print_delayed(f"\nCongratulations, Detective X! You solved the case!", Colors.CYAN)
            time.sleep(3)
            print_delayed(f"\nClue: Witness comes forward: They saw {SUSPECTS_DATA[self.killer]['name']} near the crime scene.", Colors.YELLOW)
            time.sleep(3)
            print_delayed(f"\nMotive: {MOTIVE_STORIES[self.motive]}", Colors.YELLOW)
            sys.exit()
        else:
            print_delayed(f"\n{SUSPECTS_DATA[suspect]['name']} says: 'I think you should go back to the drawing board.'", Colors.RED)
            if correct > 0 and self.guess_attempts > 2:
                print_delayed(f"\nGentle hint: You got {correct} out of 3 correct, but which ones?", Colors.CYAN)
            time.sleep(3)
            if self.guess_attempts >= 3:
                print_delayed("\nToo many wrong guesses. Restarting case with new killer...", Colors.RED)
                time.sleep(3)
                self.__init__()

# ---------- Start Game ----------
intro_story()
game = Game()
