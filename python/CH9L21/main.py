heroes = [
        "Glorfindel",
        2093,
        True,
        "Gandalf",
        1054,
        False,
        "Gimli",
        389,
        False,
        "Aragorn",
        87,
        False,
]

def get_heroes(heroes):
    # iterate over the list from beginning to end in 3 steps
    # steps
    n = 3
    for i in range(0, len(heroes), n):
        heroes[i] = heroes[i:n]
        n += 3
    return heroes

def main():

    get_heroes(heroes)

main()
