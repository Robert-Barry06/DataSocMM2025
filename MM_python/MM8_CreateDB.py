import sqlite3, random, os

# 1. Connect / create DB
db_name = "master_words2.db"
conn = sqlite3.connect(db_name)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS mystery_words;")
cur.execute("CREATE TABLE mystery_words (ID_number INTEGER PRIMARY KEY, word TEXT);")

# 2. Base English words + red herrings
base_words = [
    "admissions","scandal","ranking","funding","department","analysis","secret","model",
    "assistant","professor","evidence","bias","suspect","lab","time","method","data","number",
    "truth","source","financial","mitchell","received","external","two","weeks","ago",
    "university","research","student","faculty","college","campus","lecture","classroom",
    "study","experiment","evaluation","report","presentation","project","assignment","exam",
    "curriculum","syllabus","lecturehall","library","textbook","publication","journal","conference",
    "seminar","thesis","dissertation","dataset","database","statistics","algorithm","model","simulation",
    "metrics","methodology","observation","measurement","sample","survey","questionnaire","result",
    "finding","outcome","proof","hypothesis","theory","interpretation","conclusion","validation",
    "review","peer","citation","reference","document","archive","record","budget","grant","donation",
    "expense","investment","accounting","audit","ledger","transaction","revenue","cost","profit",
    "loss","forecast","prediction","schedule","deadline","timeline","plan","strategy","policy",
    "procedure","protocol","regulation","compliance","ethics","integrity","conflict","risk","security",
    "privacy","confidential","sensitive","access","control","authorization","login","password",
    "encryption","network","system","software","hardware","platform","application","tool",
    "supervisor","manager","director","coordinator","leader","team","group","division","office",
    "administration","organization","institution"
]
red_herrings = ["Wong","Kowalski","Okonkwo","Koestler","James","Elena","Amara","Harry","Nguyen",
                "mathematics","advisor","admin","tenure","colleague","encryption"]
base_words.extend(red_herrings)

# Expand to 10,000 rows
while len(base_words) < 10000:
    base_words.extend(base_words)
base_words = base_words[:10000]
random.shuffle(base_words)

# 3. Clues for 5 problems × 4 steps (split each clue into words)
clues = [
    # Problem 1
    "Find all entries where ID_number contains 112 and is divisible by 12",
    "Now search for records whose ID ends with 77 or 33",
    "Locate words where ID contains 5 and is divisible by 9",
    "Proceed to IDs between 2000 and 2015 to uncover the next phase",
    # Problem 2
    "Find all IDs containing 24 and divisible by 8",
    "Now search for IDs ending with 19 or 29",
    "Choose words with IDs greater than 5000 but not divisible by 10",
    "The next sequence begins in range 3050 to 3065",
    # Problem 3
    "Find all words with ID containing 66 and divisible by 6",
    "Select all entries where ID is even but does not contain 2",
    "Now find entries whose ID sum of digits equals 9",
    "The next clue begins at IDs 4070 through 4080",
    # Problem 4
    "Find all entries where ID contains 91 or 37 and is divisible by 7",
    "Now choose IDs that end in 4 but not 44",
    "Look for entries where ID contains 8 and 2 together",
    "The final mystery begins at IDs 9000 to 9010",
    # Problem 5
    "Select IDs containing 50 and divisible by 10",
    "Now find IDs ending in 99 or 100",
    "Find entries with ID greater than 9500 but not containing 8",
    "Financial records reveal Dr. Mitchell received a $50,000 research grant from a mysterious external source two weeks ago"
]

# 4. Define unique ID conditions for each clue
conditions = [
    # Problem 1
    lambda x: '112' in str(x) and x % 12 == 0,
    lambda x: str(x).endswith('77') or str(x).endswith('33'),
    lambda x: '5' in str(x) and x % 9 == 0,
    lambda x: 2000 <= x <= 2015,
    # Problem 2
    lambda x: '24' in str(x) and x % 8 == 0,
    lambda x: str(x).endswith('19') or str(x).endswith('29'),
    lambda x: x > 5000 and x % 10 != 0,
    lambda x: 3050 <= x <= 3065,
    # Problem 3
    lambda x: '66' in str(x) and x % 6 == 0,
    lambda x: x % 2 == 0 and '2' not in str(x),
    lambda x: sum(int(d) for d in str(x)) == 9,
    lambda x: 4070 <= x <= 4080,
    # Problem 4
    lambda x: '91' in str(x) or '37' in str(x) and x % 7 == 0,
    lambda x: str(x).endswith('4') and not str(x).endswith('44'),
    lambda x: '8' in str(x) and '2' in str(x),
    lambda x: 9000 <= x <= 9010,
    # Problem 5
    lambda x: '50' in str(x) and x % 10 == 0,
    lambda x: str(x).endswith('99') or str(x).endswith('100'),
    lambda x: x > 9500 and '8' not in str(x),
    lambda x: x == 9999  # final clue
]

# 5. Fill database
for i, word in enumerate(base_words, start=1):
    cur.execute("INSERT INTO mystery_words VALUES (?, ?)", (i, word))

# 6. Overwrite IDs satisfying conditions with clue words
for clue, cond in zip(clues, conditions):
    words = clue.split()
    # Find candidate IDs that satisfy condition
    candidate_ids = [i for i in range(1, 10001) if cond(i)]
    # Randomly select IDs for each word
    random.shuffle(candidate_ids)
    for idx, wid in enumerate(candidate_ids[:len(words)]):
        cur.execute("UPDATE mystery_words SET word=? WHERE ID_number=?", (words[idx], wid))

conn.commit()
conn.close()

# 7. Confirmation
full_path = os.path.abspath(db_name)
print(f"\n✅ Database created successfully!")
print(f"File: {db_name}")
print(f"Full path: {full_path}\n")
print("Solve the mystery by running the correct SQL queries for each step!\n")
