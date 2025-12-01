from name_function import get_formatted_name

def test_first_last_name(): #1
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin') #2
    assert formatted_name == 'Janis Joplin' #3

# the name of a test file is important; it must start with test_
# when we ask pytest to run the tests we've written, it will look for any file that begins with test_, and run all of the tests it finds in that file.

# 1
# in the test file, we first import the function that we want to test: get-formatted_name().
# then we define a test function: in this case, test_first_last_name(). This is a longer function name than we've been using, for a good reason.

# 2
# we call the function we're testing. Here we call get_formatted_name() with args 'janis' and 'joplin', just like we used when we ran names.py.
# we assign the return value of this function to formatted_name.

# 3
# finally, we make an assertion. An assertion is a claim about condition. Here we're claiming that the value of formatted_name should be 'Janis Joplin'.

# to run:
# pytest
# Or,
# python3 -m pytest test_name_function.py (desktop/programming/crash_course25/pytest/2/))