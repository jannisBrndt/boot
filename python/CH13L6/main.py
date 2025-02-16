def fizzbuzz(start, end):
    list = []

    for i in range(start, end + 1):
        if i % 3 == 0:
            list.append("fizz")
        if i % 3 == 0 and i % 5 == 0:
            list.append("fizzbuzz")
        else:
            list.append(i)
    return list

def main():
    start = 0
    end = 10
    fizzbuzz(start, end)

main()
