import pytest

def test_sort():
    # Test the bubble sort implementation
    unsorted_list = [1, 2, 3, 2, 2, 2, 3, 1, 1]
    sorted_list = [1, 1, 1, 2, 2, 2, 2, 3, 3]
    assert input == sorted_list

def test_sorted_function():
    # Test the sorted function
    unsorted_list = [1, 2, 3, 2, 2, 2, 3, 1, 1]
    sorted_list = sorted(unsorted_list)
    assert sorted_list == [1, 1, 1, 2, 2, 2, 2, 3, 3]

if __name__ == "__main__":
    pytest.main()