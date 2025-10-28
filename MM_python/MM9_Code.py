import textwrap

# ---------------- INTRO ---------------- #
def intro():
    print(textwrap.dedent("""
    🕵️‍♂️ Welcome to "The Case of the Coded Confession — Ultimate Detective Edition"

    You are the lead detective. Each scene contains a Python-coded clue.
    Solve the puzzle in each scene to collect evidence.
    The first letters of all puzzle titles form a secret password
    that unlocks the final confession.

    Difficulty levels:
      1. Easy   — Beginner programmers
      2. Medium — Second-year college-level programmers
      3. Hard   — Graduate-level Python mastery
      
    At any input prompt, type:
      🔹 'hint'  → to get a hint about the Python concept or code
      🔹 'break' → to restart and choose a different difficulty
    """))

# ---------------- GET DIFFICULTY ---------------- #
def get_choice():
    while True:
        c = input("Enter difficulty (1/2/3): ").strip().lower()
        if c == "break":
            return "break"
        if c in ("1","2","3"):
            return int(c)
        print("Please enter 1, 2, or 3.")

# ---------------- INPUT HANDLER WITH HINT & BREAK ---------------- #
def get_input(puzzle):
    while True:
        ans = input(f"{puzzle['question']} (or type 'hint'/'break'): ").strip()
        if ans.lower() == "break":
            return "break"
        if ans.lower() == "hint":
            print("\n💡 Hint:", puzzle.get("hint","No hint available."), "\n")
            continue
        return ans

# ---------------- PLAY FUNCTION ---------------- #
def play(puzzles):
    initials = []
    print("\n🕯️ Investigation begins...\n")
    for i, p in enumerate(puzzles, start=1):
        print(f"🔎 Scene {i}: {p['title']}")
        print("-"*60)
        print(p["story"])
        print("\nCode snippet:")
        print(textwrap.indent(p["code"], "  "))
        print()
        guess = get_input(p)
        if guess == "break":
            print("🔄 Restarting difficulty selection...\n")
            return "break"
        if guess.lower() == str(p["answer"]).lower():
            print("✅ Correct!\n")
        else:
            print(f"❌ Wrong. The correct answer was: {p['answer']}\n")
        initials.append(p["title"][0].upper())

    print("🧩 All scenes completed.")
    pwd = get_input({"question":"Enter the first letters of all scene titles (no spaces) to unlock the confession","hint":"Use the first letters of each puzzle title in order."})
    if pwd.lower() == "break":
        print("🔄 Restarting difficulty selection...\n")
        return "break"
    if pwd.upper() == "".join(initials):
        print("\n🔓 Password correct.")
        print("💬 Final confession revealed:")
        print("  'Dr. Kowalski admits she was helping Chen but was scared.'")
    else:
        print("\n🚫 Incorrect password. The confession remains locked.")

# ---------------- PUZZLE SETS ---------------- #

# ---------------- EASY ---------------- #
EASY = [
{"title":"K — Kitchen Knife","story":"You find a knife in the kitchen with a note 'Kowalski'.","code":'clues=["Knife","Apple","Lemon"]\nprint(clues[0])',"question":"What object is mentioned first?","answer":"Knife","hint":"First element of the list."},
{"title":"O — Old Clock","story":"A clock shows an unusual time, perhaps a clue.","code":'time=[12,3,6,9]\nprint(time[-1])',"question":"What number is printed?","answer":"9","hint":"-1 index gives last element."},
{"title":"W — Written Note","story":"A note says 'Water hides the secret.'","code":'word="Water"\nprint(word[0])',"question":"First character?","answer":"W","hint":"Index 0 gets first character."},
{"title":"A — Apple Core","story":"A bitten apple lies on the desk.","code":'fruit="Apple"\nprint(fruit[-1])',"question":"Last character?","answer":"e","hint":"-1 index returns last character."},
{"title":"L — Locked Drawer","story":"Drawer code is sum of digits 4,5,6.","code":'code=[4,5,6]\nprint(sum(code))',"question":"Sum?","answer":"15","hint":"sum() adds list elements."},
{"title":"S — Silver Key","story":"You find a silver key inside the drawer.","code":'key="Silver"\nprint(key.lower())',"question":"Key color?","answer":"silver","hint":".lower() converts string to lowercase."},
{"title":"K — Kowalski Journal","story":"Kowalski wrote 'I tried to help Chen'.","code":'phrase="I tried to help Chen"\nprint(phrase.split()[-1])',"question":"Who did Kowalski help?","answer":"Chen","hint":"split() then -1 for last word."},
{"title":"I — Ink Bottle","story":"An ink bottle spilled over letters.","code":'bottle="Ink"\nprint(bottle[0])',"question":"First character?","answer":"I","hint":"Index 0 returns first character."},
{"title":"H — Hidden Drawer","story":"A hidden drawer behind the desk is found.","code":'compartment=True\nprint(not compartment)',"question":"Is compartment closed? (True/False)","answer":"False","hint":"not True = False."},
{"title":"E — Envelope","story":"Inside the drawer lies an envelope.","code":'letter="Envelope"\nprint(letter[0])',"question":"First character?","answer":"E","hint":"Index 0."},
{"title":"L — Lantern","story":"A lantern lights the dark room.","code":'light="Lantern"\nprint(light.upper())',"question":"What illuminates the room?","answer":"LANTERN","hint":".upper() converts to uppercase."},
{"title":"P — Photograph","story":"A photo shows Chen and Kowalski.","code":'photo=["Chen","Kowalski"]\nprint(photo[0])',"question":"Who appears first?","answer":"Chen","hint":"Index 0 of list."},
{"title":"S — Secret Word","story":"A paper prints 'Safety'.","code":'msg="Safety"\nprint(msg)',"question":"Printed word?","answer":"Safety","hint":"Just read the string."},
{"title":"C — Clock Tower","story":"Midnight, clock tower chimes once.","code":'time=12\nprint(time)',"question":"What time?","answer":"12","hint":"Print variable."},
{"title":"H — Handwriting","story":"Handwriting matches Kowalski's journal.","code":'match=True\nprint(match)',"question":"Does it match? (True/False)","answer":"True","hint":"Variable is True."},
{"title":"E — Evidence Box","story":"All items are sealed into evidence box.","code":'items=16\nprint(items)',"question":"Number of items?","answer":"16","hint":"Print variable."},
{"title":"N — Night Confession","story":"Recording plays: 'I was helping Chen but scared.'","code":'confession="help Chen"\nprint(confession)',"question":"Who did they help?","answer":"Chen","hint":"Last word of string."},
]

# ---------------- MEDIUM ---------------- #
MEDIUM = [
{"title":"K — Key Cipher","story":"A message is encoded with Caesar cipher; decode first shift.","code":'msg="Kowalski"\ndecoded="".join(chr(((ord(c)-65+1)%26)+65) if c.isupper() else c for c in msg)\nprint(decoded)',
 "question":"What prints?","answer":"Lpwalski","hint":"Shift only uppercase letters by 1 using ord/chr arithmetic."},
{"title":"O — Odd Slicer","story":"Take letters in odd positions of a string.","code":'word="Notebook"\nprint(word[1::2])',
 "question":"What prints?","answer":"oebok","hint":"Slicing with step 2; start at index 1."},
{"title":"W — While Generator","story":"Generator yields squares, then exhausted.","code":'g=(i**2 for i in range(3))\nprint(next(g))\nprint(list(g))',
 "question":"Second print line?","answer":"[1,4]","hint":"next() consumes first value; list() returns remaining."},
{"title":"A — Argument Mutation","story":"Mutable default list trick.","code":'def f(x,lst=[]): lst.append(x); return lst\nprint(f(1))\nprint(f(2))',
 "question":"Second print line?","answer":"[1,2]","hint":"Mutable default persists across calls."},
{"title":"L — Lambda in Comprehension","story":"Capture loop variable correctly.","code":'funcs=[lambda i=i:i*3 for i in range(3)]\nprint([f() for f in funcs])',
 "question":"What prints?","answer":"[0,3,6]","hint":"Use default arg in lambda to capture value."},
{"title":"S — Set Operations","story":"Union and intersection of sets.","code":'a={1,2,3}\nb={2,3,4}\nprint(a&b, a|b)',
 "question":"What prints?","answer":"{2,3} {1,2,3,4}","hint":"& is intersection, | is union."},
{"title":"K — Keyword Arguments Puzzle","story":"Function with keyword arguments out of order.","code":'def f(a,b=2): return a+b\nprint(f(b=5,a=3))',
 "question":"What prints?","answer":"8","hint":"Keywords can be used in any order."},
{"title":"I — Immutable Tuple","story":"Attempt to modify tuple element.","code":'t=(1,2,3)\nt[0]=9\nprint(t)',
 "question":"What happens?","answer":"Error","hint":"Tuples are immutable; cannot assign."},
{"title":"H — Hidden Dict Access","story":"Use dict.get() with default.","code":'d={"a":1}\nprint(d.get("b",99))',
 "question":"What prints?","answer":"99","hint":"get() returns default if key missing."},
{"title":"E — Enumerate Custom Start","story":"Enumerate list starting at 10.","code":'lst=["x","y"]\nfor i,v in enumerate(lst,10): print(i,v)',
 "question":"First index printed?","answer":"10","hint":"enumerate(iterable,start) sets index."},
{"title":"L — List Comprehension Squares","story":"Square numbers using comprehension.","code":'nums=[i**2 for i in range(4)]\nprint(nums)',
 "question":"What prints?","answer":"[0,1,4,9]","hint":"i**2 squares each number."},
{"title":"P — Pop and Append","story":"Pop last element, then append new one.","code":'lst=[1,2,3]\nlst.pop()\nlst.append(5)\nprint(lst)',
 "question":"What prints?","answer":"[1,2,5]","hint":"pop removes last, append adds element at end."},
{"title":"S — Split and Index","story":"Split string and access element.","code":'''sentence="help Chen"words=sentence.split()print(words[1])''', #I do not know the purpose of this formatting but this was erroring and this should resolve it for now
 "question":"What prints?","answer":"Chen","hint":"split() separates words; index 1 is second word."},
{"title":"C — Comma Join","story":"Join letters with commas.","code":'letters=["C","H","E","N"]\nprint(",".join(letters))',
 "question":"What prints?","answer":"C,H,E,N","hint":"join() concatenates with separator."},
{"title":"H — Heap Sort","story":"Sort numbers with sorted().","code":'nums=[3,1,2]\nprint(sorted(nums))',
 "question":"What prints?","answer":"[1,2,3]","hint":"sorted() returns sorted list."},
{"title":"E — Enumerate Index","story":"Find index of Chen in list.","code":'lst=["Kowalski","Chen"]\nfor i,v in enumerate(lst):\n if v=="Chen": print(i)',
 "question":"Index printed?","answer":"1","hint":"enumerate() gives index and value."},
{"title":"N — Nested List Access","story":"Access element inside nested list.","code":'lst=[[1,2],[3,4]]\nprint(lst[1][0])',
 "question":"What prints?","answer":"3","hint":"lst[1] is second list; [0] first element."},
]

# ---------------- HARD ---------------- #
HARD = [
{"title":"K — Metaclass Magic","story":"Create a metaclass that injects a dynamic method based on class name.","code":'class Meta(type):\n def __new__(cls,name,bases,dct):\n  dct["reveal"]=lambda self: name[::-1]\n  return super().__new__(cls,name,bases,dct)\nclass Secret(metaclass=Meta): pass\nprint(Secret().reveal())',"question":"What prints?","answer":"terceS","hint":"Metaclass can add methods dynamically; method returns reversed class name."},
{"title":"O — Generator Send & Throw Complex","story":"Generator yields, accepts values, and handles exceptions.","code":'def g():\n try:\n  x=yield "start"\n except ValueError:\n  x=99\n yield x*2\ngen=g()\nprint(next(gen))\nprint(gen.send(5))\nprint(gen.throw(ValueError))',"question":"Third print line?","answer":"198","hint":"throw(ValueError) triggers except block inside generator."},
{"title":"W — Descriptor State Tracker","story":"Descriptor counts accesses and modifies external state.","code":'class D:\n def __init__(self): self.count=0\n def __get__(self,obj,objtype): self.count+=1; return self.count*10\nclass X:\n val=D()\nprint(X().val)\nprint(X().val)',"question":"Second print line?","answer":"20","hint":"__get__ called each access; multiplies internal counter."},
{"title":"A — Decorator of Decorators","story":"A decorator wraps another decorator that modifies function output.","code":'def deco1(f):\n def wrapper(): return f()*2\n return wrapper\ndef deco2(f):\n def wrapper(): return f()+3\n return wrapper\n@deco1\n@deco2\ndef f(): return 5\nprint(f())',"question":"What prints?","answer":"16","hint":"Innermost decorator executes first; deco2 adds 3, deco1 multiplies by 2."},
{"title":"L — Context Manager Side Effect","story":"Context manager modifies a global variable on exit.","code":'x=1\nclass CM:\n def __enter__(self): return self\n def __exit__(self,*args): global x; x+=5\nwith CM(): pass\nprint(x)',"question":"What prints?","answer":"6","hint":"__exit__ runs after with block; modifies global x."},
{"title":"S — MRO Diamond Inheritance","story":"Multiple inheritance with diamond; super() called in each class.","code":'class A: def f(self): return "A"\nclass B(A): def f(self): return super().f()+"B"\nclass C(A): def f(self): return super().f()+"C"\nclass D(B,C): def f(self): return super().f()+"D"\nprint(D().f())',"question":"What prints?","answer":"ACBD","hint":"Python MRO determines the order super() calls."},
{"title":"K — Nested Comprehension Trap","story":"Lambdas inside nested list comprehension capture loop variables.","code":'funcs=[[lambda x=i:x*2 for i in range(2)] for j in range(2)]\nprint([[f() for f in row] for row in funcs])',"question":"What prints?","answer":"[[0,2],[0,2]]","hint":"Each lambda captures i via default argument; outer loop repeats list."},
{"title":"I — Mutable Default Closure Trap","story":"Function with mutable default modifies over multiple calls.","code":'def f(x, lst=[]): lst.append(x); return lst\nprint(f(1))\nprint(f(2))',"question":"Second print line?","answer":"[1,2]","hint":"Mutable default persists across calls."},
{"title":"H — Exec with Dynamic Function","story":"Use exec to define a function and call it.","code":'ns={}\nexec("def f(): return 5", ns)\nprint(ns["f"]())',"question":"What prints?","answer":"5","hint":"Exec creates function in provided dict namespace."},
{"title":"E — Eval with Custom Locals","story":"Evaluate expression in custom local dictionary.","code":'local={"a":3,"b":4}\nexpr="a*b+2"\nprint(eval(expr,{},local))',"question":"What prints?","answer":"14","hint":"Eval can take custom locals to evaluate expression."},
{"title":"L — Property Side Effect","story":"Property increments internal counter every access.","code":'class C:\n def __init__(self): self._c=0\n @property\n def val(self): self._c+=1; return self._c\nc=C()\nprint(c.val)\nprint(c.val)',"question":"Second print line?","answer":"2","hint":"Property method modifies internal state each access."},
{"title":"P — Descriptor with Setter","story":"Descriptor modifies external variable when set.","code":'class D:\n def __get__(self,obj,objtype): return obj._x\n def __set__(self,obj,val): obj._x=val*2\nclass X:\n _x=0\n val=D()\nx=X()\nx.val=3\nprint(x._x)',"question":"What prints?","answer":"6","hint":"__set__ doubles assigned value."},
{"title":"S — Complex Slice Assignment","story":"Replace part of list with iterable of different length.","code":'lst=[1,2,3,4]\nlst[1:3]=[9,8,7]\nprint(lst)',"question":"What prints?","answer":"[1,9,8,7,4]","hint":"Slice assignment adjusts list length automatically."},
{"title":"C — Dynamic Attribute via setattr","story":"Create attribute dynamically and access it.","code":'class X: pass\nx=X()\nsetattr(x,"secret",42)\nprint(x.secret)',"question":"What prints?","answer":"42","hint":"setattr(obj, name, value) creates attribute dynamically."},
{"title":"H — Hashability Trap","story":"Attempt to use mutable set as dict key.","code":'d={}\nd[{1,2}]=5',"question":"What happens?","answer":"Error","hint":"Mutable sets are unhashable."},
{"title":"E — Nested Generator with Yield From","story":"Generator yields from nested iterables.","code":'def g():\n yield from [1,2]\n yield from [3,4]\nprint(list(g()))',"question":"What prints?","answer":"[1,2,3,4]","hint":"yield from concatenates all sub-iterables."},
{"title":"N — Complex Closure Counting","story":"Closures with counters track calls separately.","code":'def counter():\n count=0\n def f():\n  nonlocal count\n  count+=1\n  return count\n return f\nc=counter()\nprint(c())\nprint(c())',"question":"Second print line?","answer":"2","hint":"nonlocal allows inner function to modify outer variable."},
]

# ---------------- MAIN LOOP ---------------- #
def main():
    intro()
    while True:
        choice = get_choice()
        if choice == "break":
            continue
        if choice == 1:
            result = play(EASY)
        elif choice == 2:
            result = play(MEDIUM)
        elif choice == 3:
            result = play(HARD)
        if result == "break":
            continue
        break

if __name__ == "__main__":
    main()
