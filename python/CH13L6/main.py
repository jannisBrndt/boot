def fizzbuzz(start, end):
    list = []

    for i in range(start, end):
        if i % 3 == 0 and i % 5 == 0:
            list.append("fizzbuzz")
        elif i % 5 == 0:
            list.append("buzz")
        elif i % 3 == 0:
            list.append("fizz")
        else:
            list.append(i)
    return list

def main():
    start = 5
    end = 31
    fizzbuzz(start, end)
main()
