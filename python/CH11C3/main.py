def find_missing_ids(first_ids, second_ids):

    missing_ids = []
    collect_first_ids = set()
    collect_second_ids = set()
    
    for id in first_ids:
        collect_first_ids.add(id)
    
    for id in second_ids:
        collect_second_ids.add(id)
    
    for id in collect_first_ids:
        if id not in collect_second_ids:
            missing_ids.append(id)

    return missing_ids

def main():
    first_ids = [1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10]
    second_ids = [1, 2, 2, 3, 4, 5, 6, 7, 8]
    find_missing_ids(first_ids, second_ids)

main()
