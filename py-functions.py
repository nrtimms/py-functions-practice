# Funtion to find the max value in a list of values
def max_num(a,b,c):
    return max([a,b,c])

print("MAX VALUE OF PROVIDED LIST:")
print(max_num(34,49,17))


# Function to find the product of a list of values
def mult_list(num_lst):
    if len(num_lst) == 0:
        product = 0
    else:
        product = 1
        for i in num_lst:
            product = product * i
    return product

print("PRODUCT OF EMPTY LIST:")
print(mult_list([]))
print("PRODUCT OF PROVIDED LIST:")
print(mult_list([3,6,4,2]))


# Funciton to reverse stringe
def rev_string(my_string):
    new_string = my_string[::-1]
    return new_string

print("REVERSED STRING:")
print(rev_string("race car"))


# Function to determine if first number is within the range provided
def num_within(a,b,c):
    result = a in range(b,c+1)
    return result

print("IS 4 WITHIN 2-4:")
print(num_within(4,2,4))
print("IS 78 WITHIN 4-9:")
print(num_within(78,4,9))


# Function to print n number of lines of pascal triangle
def pascal(n):
    triangle = [[1],[1,1]]
    if n < 1:
        print("not a valid number of rows to print")
    elif n == 1:
        print(triangle[0])
    elif n == 2:
        for i in triangle:
            print(i)
    else:
        for i in range(2, n):
            prev_row = triangle[i-1]
            new_row = [1]
            row_len = len(prev_row)
            for i in range(0, row_len-1):
                val = prev_row[i] + prev_row[i+1]
                new_row.append(val)
                if i == row_len-2:
                    new_row.append(1)
            triangle.append(new_row)
        for i in triangle:
            print(i)

print("0 ROWS OF PASCAL TRIANGLE:")
pascal(0)
print("1 ROW OF PASCAL TRIANGLE:")
pascal(1)
print("2 ROWS OF PASCAL TRIANGLE:")
pascal(2)
print("6 ROWS OF PASCAL TRIANGLE:")
pascal(6)

