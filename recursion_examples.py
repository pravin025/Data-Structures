# Find sum of digits of a integer number


def sum_digits(num):
    if num == 0 and int(num) == num:
        return 0
    else:
        return int(num % 10) + sum_digits(int(num / 10))


print("--------------------  sum_digits-------------------------")
print(sum_digits(10011))


# Find power of some number.
def power_of_num(num, power):
    if power == 1:
        return num
    if power == 0:
        return 1
    else:
        power -= 1
        return num * power_of_num(num, power)


print("--------------------  Power of num-------------------------")
print("-------------------------num=22, power=0--------------------")
print(power_of_num(22, 0))
print("---------------------- num=11, power=1-------------------------")
print(power_of_num(11, 1))
print("---------------------- num=4, power=3-------------------------")
print(power_of_num(4, 3))


# Find GCD of two numbers

def gcd(num1, num2):
    if num1 > num2:
        # print(f"{num1} is greater than {num2}")
        # print(num1 / num2)
        if int(num1 / num2) == num1 / num2:
            # print(f"{num1} is divisible by {num2}")
            return num1 / num2
        num1 = num1 - num2
        # print(f"num1={num1}, num2={num2}")
        return gcd(num1, num2)
    else:
        # print(f"{num2} is greater than {num1}")
        if int(num2 / num1) == num2 / num1:
            # print(f"{num2} is divisible by {num1}")
            return num2 / num1
        num2 = num2 - num1
        # print(f"num1={num1}, num2={num2}")
        return gcd(num1, num2)


print("-------------------------- Greatest common factor------------------------")
print("-------------------------num1 = 98, num2 = 56----------------------------")
print(gcd(98, 56))

print("-------------------------num1 = 4, num2 = 16----------------------------")
print(gcd(4, 16))

print("-------------------------num1 = 28, num2 = 4----------------------------")
print(gcd(28, 4))


def decimal_to_binary(num):
    if num <= 1:
        return num
    binary = num % 2
    num = num // 2
    return str(decimal_to_binary(num)) + str(binary)


print("---------------------- decimal to binary ----------------------------------")
print("----------------------- num =7 --------------------------------------------")
print(decimal_to_binary(52))


def reverse_string(string):
    if not len(string):
        return string
    else:
        return reverse_string(string[1:]) + string[0]


print("------------------------ reverse_string -----------------------------------------")
print(reverse_string("pravin"))


def palindrome(string):
    if len(string) < 1:
        return True
    else:
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
        else:
            return False


print("------------------------------- palindrome -----------------------------------------------")
print(palindrome("abcdcba"))
print(palindrome("abcd"))


# Count pairs with given sum

def sum_pairs(num):
    pairs_count = 1
