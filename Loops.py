#example input
n=3

#solution
if __name__ == '__main__':
    n = int(input())
    #lets create a range of values 0<=i<n
    for i in range(n):
        #square the values in this list
        result = i**2
        #print each square
        print(result)
