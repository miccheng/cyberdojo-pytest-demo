'''The starting files are unrelated to the exercise.

They show examples of writing and testing
  o) a global function
  o) an instance method
Pick the style most suitable to your exercise.
'''

def fizz_buzz(num_items):
    result = [__value_of(n+1) for n in range(num_items)]
    
    return result

def __value_of(num):
    result = ''
    
    if num % 3 == 0:
        result += 'Fizz'
    
    if num % 5 == 0:
        result += 'Buzz'

    if len(result) == 0:
        result = num
    
    return result