def AgeInDays(age_in_yrs: int) -> int:
    """
    Return the age in days.

    :param age: Age in years
    :return: age in days
    """
    return f"{365 * age_in_yrs} Days"

print(AgeInDays(20))
