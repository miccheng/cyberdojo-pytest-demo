from fizz_buzz import fizz_buzz


@pytest.mark.parametrize(
    "test_input,expected", 
    [
        (0, []),
        (1, [1]), 
        (3, [1, 2, 'Fizz']),
        (5, [1, 2, 'Fizz', 4, 'Buzz']),
        (15, [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'])
    ]
)
def test_fizz_buzz(test_input, expected):
    assert fizz_buzz(test_input) == expected
    

'''
def test_empty_list():
    assert fizz_buzz(0) == []

def test_one_item():
    assert fizz_buzz(1) == [1]

def test_first_multiple_of_3():
    assert fizz_buzz(3) == [1, 2, 'Fizz']
    
def test_first_multiple_of_5():
    assert fizz_buzz(5) == [1, 2, 'Fizz', 4, 'Buzz']
    
def test_first_multiple_of_3_and_5():
    assert fizz_buzz(15) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
'''