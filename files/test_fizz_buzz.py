from fizz_buzz import fizz_buzz

def test_empty_list():
    assert fizz_buzz(0) == []

def test_one_item():
    assert fizz_buzz(1) == [1]

def test_first_multiple_of_3():
    assert fizz_buzz(3) == [1, 2, 'Fizz']