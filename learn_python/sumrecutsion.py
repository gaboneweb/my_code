def sum_normal(n):
    sum_ = 0
    for i in range(1,n + 1):
        sum_ += i

    return sum_

def sum_recursion(n):
    if n <= 1:
        return n
    else:
        return n + sum_recursion(n - 1)


if __name__ == "__main__":

    #print(sum_normal(int(input("Enter big number:"))))



    print(sum_recursion(int(input("Enter big number:"))))
"""
 Recursion limit for python is set to 1000. So summing numbers greater than 998 will raise a:
 *************RecursionError: maximum recursion depth exceeded in comparison****************
    """
