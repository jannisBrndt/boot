def validate_path(expected_path, character_path):
    name = character_path[0]
    percentage = 0.0

    for i in range(0, (len(expected_path))):
        for j in range(1, len(character_path)):
            if expected_path[i] == character_path[j]:
                percentage += 1
                break

    percentage = (percentage/len(expected_path)) * 100
    return name, percentage

def main():
    expected_path = ["A", "B", "C", "D", "E"]
    character_path = ["Hero123", "A", "B", "C", "D", "E"]
    validate_path(expected_path, character_path)

main()
