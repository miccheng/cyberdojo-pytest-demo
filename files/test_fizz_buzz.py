import pytest
from fizz_buzz import fizz_buzz

@pytest.mark.parametrize(
    "num, expected",
    [
        (0, []),
        (1, [1]),
        (3, [1, 2, 'Fizz']),
        (5, [1, 2, 'Fizz', 4, 'Buzz']),
        (15, [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'])
    ]
)
def test_fizz_buzz(num, expected):
    print('Expecting input of {} will result in {}'.format(num, expected))
    assert fizz_buzz(num) == expected
