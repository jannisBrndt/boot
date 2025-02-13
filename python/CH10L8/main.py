def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    name_of_max = ""
    if bool(enemies_dict) == False:
        return
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            max_so_far = enemies_dict[enemy]
            name_of_max = enemy
        elif enemies_dict[enemy] == max_so_far:
            break
            
    return name_of_max

def main():
    enemies_dict = {
        "jackal": 4,
        "kobold": 3,
        "soldier": 10,
        "gremlin": 5
    }
    get_most_common_enemy(enemies_dict)

main()
