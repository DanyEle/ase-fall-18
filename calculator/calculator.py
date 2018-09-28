#calculator.py module ASE 28/09/2018

def sum(m,n):
    result = m
    iterator = 0
    increment = 1

    if n < 0 :
        increment = -1
        n = -n

    while iterator < n : # for i in range(n)
        result = result + increment
        iterator = iterator + 1

    return result


def divide(m,n):
    result = 0
    sign = 1

    if n == 0:
        raise Exception("Not allowed to divide by 0!!")

    if n < 0:
        sign = -sign
        n = -n

    if m < 0:
        sign = -sign
        m = -m

    while (m -n) >= 0 :
        m = m - n
        result = result + 1

    return sign * result



def main():
    print(sum(-3,-3))
    print(divide(0,-3))


if __name__ == "__main__":
    main()