def merge(dict1, dict2):
    merged = {}

    for i in dict1:
        merged[i] = dict1[i]
    for i in dict2:
        merged[i] = dict2[i]
    return merged

def total_score(score_dict):
    total_score = 0
    for i in score_dict:
        total_score += score_dict[i]
    return total_score


def main():
    dict1 = {"first quarter": 2, "second quarter": 3}
    dict2 = {"third quarter": 6, "fourth": 10}
    merge(dict1, dict2)

main()
