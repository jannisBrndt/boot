def reverse_array(items):
    reverse_items = []
    for i in range(len(items) - 1, -1, -1):
        reverse_items.append(items[i])
    return reverse_items

def main():
    test = [1, 2, 3, 4, 5]
    reverse_array(test)

main()
