#level intermediate

print("hello python")

# in Python:
# tests go in a separate function
# print)hi -> test_print_hi_works_with_negative_numbers
# docstring looks like """description of the function"""
# snake_case (variable/function nmaes use underscores of hyphens)
# two types of numbers, int(integers) and floats(decimal numbers)
# def to define a function instead of fun
# type is just one colon instead of two
# type hints are after single colon : instead of ::
# type hints are not required by default, but they are artificiallly required by the autograder
# in python you have to say return in order to return something
# ^ in python, the last line of a function is not the automatic "result"
# get the length of something with len()
# else if is elif
# instead of end, we know where the end is just by seeing where the indentation changes
# in python, each assertion tests either that the right thing was returned or that the right thing was printed, 
# but testing prints is hard
def greet(name: str) -> None:
    """produces Hello, name!"""
    print("Hello, " + name + "!")
greet("David")
greet("Chase")
greet("Jack")
greet("Josef")
greet("Hasan")
greet("LB")
greet("Cole")
greet("Trevor")
greet("Assaf")
greet("Drew")
greet("No Mercy Morse")



def add_shipping(order_amt : int) -> int:
    """adds 4 for orders <= 10 (but non-zero), 8 for orders < 30, 12 for larger orders"""
    if order_amt == 0:
        return 0
    elif order_amt <= 10:
        return order_amt + 4
    elif order_amt < 30:
        return order_amt + 8
    else: 
        return order_amt + 12
add_shipping(25)
add_shipping(1)


numbers = list (range(1,11))
print("1.", numbers)


squares = list(map(lambda n: n ** 2, numbers))
print("2.", squares)


# 3. all_even
def all_even(nums: list) -> list:
    """Return a list of all even numbers from the input list."""
    return [n for n in nums if n % 2 == 0]


assert all_even([]) == []
assert all_even([1, 3, 5]) == []
assert all_even([1, 2, 3, 4]) == [2, 4]
assert all_even([-2, -1, 0]) == [-2, 0]
print("3.", all_even(numbers))
# [2, 4, 6, 8, 10]

