'''The starting files are unrelated to the exercise.

They show examples of writing and testing
  o) a global function
  o) an instance method
Pick the style most suitable to your exercise.
'''

def fizz_buzz(num_items):
    result = [n+1 for n in range(num_items)]
    
    result = ['Fizz' for w in result if w % 3 == 0]
    
    return result
