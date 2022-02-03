def main():
    num = int(input('Insert number: ')) #takes an integer as input
    output = sumOfMultiples(num) 
    print(output)


def sumOfMultiples(param):
    j = 0
    i = 0
    for i in range(i, param):
        if (i % 3 ==0) or (i % 5 == 0) and (i % 15 != 0):
            j = j + i
    return j

if __name__ == '__main__':
    main()
