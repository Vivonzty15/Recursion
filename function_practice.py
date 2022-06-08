from math import factorial
#1

nums = [4, 8, 2, 15, 40, 10]
def max_num(*args):
    return max(*args)

print(max_num(nums))

#2

def mult_list(list):
    result = 1
    for num in list:
        result = result * num
    return result

print(mult_list(nums))

#3

def rev_string(string):
    return string[::-1]

print(rev_string('Hello'))

#4

def num_within(x, beg, end):
    nums = range(beg, end)
    bool = []
    for num in nums:
        if num == x:
            bool.append(True)
        else:
            bool.append(False)
    print(any(bool))

num_within(7, 2, 10)

#5

def pascal(n):
    layer = 1  
    values = [1]  
    while layer <= n:  
        new_values = [1]  
        index = 0  
        while index < len(values): 
            print('%d' % values[index], end=' ')  
            if (index < layer - 1):
                new_values.append(values[index] + values[index + 1])
            index += 1
        new_values.append(1)
        values = new_values 
        print("")
        layer += 1

pascal(10)