'''The starting files are unrelated to the exercise.

They show examples of writing and testing
  o) a global function
  o) an instance method
Pick the style most suitable to your exercise.
'''

def fizz_buzz(num_items):
    result = [n+1 for n in range(num_items)]
    
    for i in range(num_items):
        if result[i] % 3 == 0:
            result[i] = 'Fizz'
        elif result[i] % 5 == 0:
            result[i] = 'Buzz'
    
    return result
