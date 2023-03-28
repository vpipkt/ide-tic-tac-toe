import sys



spaces = {
    3: {f"{l}{n}" for l in ["a", "b", "c"] for n in [1, 2, 3]},
}

print("spaces  " + str(sorted(spaces[3])))

played = []
while True:

    m = input('Your turn: ')

    if m.lower() == "q":
        sys.exit(0)

    # do something
    m = m[:2].lower()
    if len(m) < 2 or not m[0] in ["a", "b", "c"] or not m[1] in ["1", "2", "3"]:
        print("Hmm I didn't understand")
        continue

    if m in played:
        print("That space is already taken!")
        continue

    played.append(m)

    # instead of just saying what we said, tell us what the board looks like now
    print(f"Board #: {played}")
