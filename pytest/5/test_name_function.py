from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name("janis", "joplin")
    assert formatted_name == "Janis Joplin"


def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")  # 1
    assert formatted_name == "Wolfgang Amadeus Mozart"  # 2


# We name this new function test_first_last_middle_name().
# The function name must start with test_ so the function runs automatically when we run pytest.
# We name the function to make it clear which behavior of get_formatted_name() we’re testing.
# As a result, if the test fails, we’ll know right away what kinds of names are affected.
# To test the function, we call get_formatted_name() with a first, last, and middle name ❶, and then we make an assertion ❷ that the returned full name matches the full name (first, middle, and last) that we expect.
# When we run pytest again, both tests pass:

# test_name_function.py ..                                         [100%]
# ========================== 2 passed in 0.01s ==========================

# The two dots above indicate that two tests passed, which is also clear from the last line of output. This is great! We now know that the function still works for names like Janis Joplin, and we can be confident that it will work for names like Wolfgang Amadeus Mozart as well.
