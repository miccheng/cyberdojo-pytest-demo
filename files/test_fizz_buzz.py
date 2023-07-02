from fizz_buzz import fizz_buzz

def test_empty_list():
    assert fizz_buzz(0) == []

def test_one_item():
    assert fizz_buzz(1) == [1]