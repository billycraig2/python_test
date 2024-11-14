import pytest
from reverse import reverse_list

def test_reverse():
    input_list = [1, 2, 3, 4, 5, 6, 7]
    expected_output = [7, 6, 5, 4, 3, 2, 1]

    # Reverse the list as done in reverse.py
    for i in range(len(input_list)//2):
        j = len(input_list) - 1 - i
        input_list[i], input_list[j] = input_list[j], input_list[i]

    assert input_list == expected_output

if __name__ == "__main__":
    pytest.main()