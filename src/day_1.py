def add_values(array: list) -> int|float:
    """
    A function that adds the elements of an array.
    If item in the array is not an integer or float, it skips this item and proceeds.

    :param array: an array whose elements are to be added.
    :return: result
    """
    try:
        assert type(array) == list
        assert len(array) != 0
        
        total_sum = 0
        for value in array:
            if isinstance(value, int) or isinstance(value, float):
                total_sum += value
        return total_sum
    
    except AssertionError:
        print("Not an array or array is empty.")

if __name__ == "__main__":
    print(add_values([1, 2, "check", 2, 2.5]))
