def comparison_points(student_a_scores: list, student_b_scores: list) -> list:
    """
    Determine the comparison points between two students.

    :param a: First list
    :param b: Second list
    :return: List containing assigned points.
    """
    try:
        assert isinstance(student_a_scores, list) and isinstance(student_b_scores, list)
        assert len(student_a_scores) == len(student_b_scores)
        
        student_a_points = 0
        student_b_points = 0
        for i in range(len(student_a_scores)):
            if student_a_scores[i] > student_b_scores[i]:
                student_a_points += 1
            elif student_a_scores[i] < student_b_scores[i]:
                student_b_points += 1
                
        return [student_a_points, student_b_points]
                
    except (AssertionError, TypeError):
        print("Error!!!\n1. Argument(s) not a list.\n2. Contains an unsupported data type.\n3. a and b are not equal in length")
    

print(comparison_points([1, 2.5, 3], [3, 2, 1]) )
    