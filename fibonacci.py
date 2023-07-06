# The purpose is to show recurssive functions utilizing memoization to 
# help with Time complexity. Normally the fibonacci sequence which adds 
# the last two numbers of the sequence to make the new number, would run at O(2^n)
# which is about as bad as it gets. Utilizing memoization we can store calculated numbers into
# an array and as we go through the sequence we will use the stored results to
# calculate the number rather than repeate it many times over and over.

# Memoization is the concept of storing function results to utilize so the function does
#  not need to be repeated.

# # The Fibonacci sequence is the following algorithm:
#       fib(n) = if n>=3 fib(n-1) + fib(n-2)
#                else fib(2)=1 and fib(1)=1
#         All real positive integers

#The method for calculating the Fibonacci sequence
def fib(n, memo):
    '''
    The function will return the last number in the fibonacci sequence.
    '''
    #check if memo contains value and return it if it does.
    if  memo[n] is not None:
        return memo[n]
    elif n >= 3:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]
    else:
        memo[1] = 1
        memo[2] = 1
        return memo[n]


# Gather input of desired n value to return Fibonacci number. 
# Loop until only given positive integer.
n = 0
while n <= 0:
  n = input("Please enter a positive whole number: ")
  if n.isdigit():
    n = int(n)
  else:
    n = 0
print(n)

# Initialize the memoization array for the amount of n values needed.
# Add 1 so that we can store the value in the n index location rather
# than counting from zero
memo = [None] * (n + 1)

fib(n, memo)
print("The sequence is")
print(str(memo[1:n + 1]))