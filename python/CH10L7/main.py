def count_enemies(enemy_names):
    enemies = {}

    for enemy_name in enemy_names:
        enemies[enemy_name] = 0

    for enemy in enemies:
        enemies[enemy] += 1

    print(enemies)

def main():
    enemy_names = ["jackal", "kobold", "soldier"]
    count_enemies(enemy_names)

main()
