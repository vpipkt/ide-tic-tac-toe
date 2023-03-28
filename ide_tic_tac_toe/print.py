
art = """
   A B C
1  {}|{}|{}
  --------
2  {}|{}|{}
  --------
3  {}|{}|{}
"""


def print_board(xs, os):
    marks = []
    for row in [1, 2, 3]:
        for col in ["a", "b", "c"]:
            space = f"{col}{row}"
            if space in xs:
                marks.append("X")
            elif space in os:
                marks.append("O")
            else:
                marks.append(" ")
    print(art.format(*marks))
