
def getInput():
    
    return list(map(int, input().split()))


def makeReverse(numbers):
    
    rvrList = []
    
    while numbers:
        rvrList.append(numbers.pop())
        
    return rvrList


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
