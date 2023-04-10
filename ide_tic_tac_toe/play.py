import sys
import printer


spaces = {
    3: {f"{l}{n}" for l in ["a", "b", "c"] for n in [1, 2, 3]},
}

print("spaces  " + str(sorted(spaces[3])))

computer = []
player = []

while True:

    m = input('Your turn: ')

    if m.lower() == "q":
        sys.exit(0)

    # do something
    m = m[:2].lower()
    if len(m) < 2 or not m[0] in ["a", "b", "c"] or not m[1] in ["1", "2", "3"]:
        print("Hmm I didn't understand")
        continue

    if m in computer or m in player:
        print("That space is already taken!")
        continue

    player.append(m)

    # Now computer plays...
    # TODO 

    # Print the board
    printer.print_board(
        xs=player,
        os=computer,
    )
