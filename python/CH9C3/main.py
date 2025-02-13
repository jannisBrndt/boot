# function to check the percentage of available ingredients and recipe, and ingredients that are not there
def check_ingredient_match(recipe, ingredients):
    count = 0
    missing = []
    for recip in recipe:
        
        if recip in ingredients:
            count += 1
        else:
            missing.append(recip)

    total = (count/len(recipe)) * 100

    print(f"{total}0", missing)


def main():
    recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
    ingredients = ["Dragon Scale", "Goblin Ear", "Phoenix Feather", "Troll Tusk"]

    check_ingredient_match(recipe, ingredients)

main()
