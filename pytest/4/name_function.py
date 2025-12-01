# Responding to a Failed Test

# a passing test means the function is behaving correctly and a failing test means there's an error in the new code you wrote. 
# When a test fails, don't change the test, fix the code that's causing the test to fail. 

# In this case, get_formatted_name() used to require only two parameters: a first name and a last name. 
# Now it requires a first name, middle name, and last name. 
# The addition of that mandatory middle name parameter broke the original behavior of get_formatted_name(). 
# The best option here is to make the middle name optional. Once we do, our test for names like Janis Joplin should pass again, and we should be able to accept middle names as well. # Let’s modify get_formatted_name() so middle names are optional and then run the test case again. If it passes, we’ll move on to making sure the function handles middle names properly.
# To make middle names optional, we move the parameter middle to the end of the parameter list in the function definition and give it an empty default value. 
# We also add an if test that builds the full name properly, depending on whether a middle name is provided:

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

# In this new version of get_formatted_name(), the middle name is optional. 
# If a middle name is passed to the function, the full name will contain a first, middle, and last name. Otherwise, the full name will consist of just a first and last name. 
# Now the function should work for both kinds of names. 
# To find out if the function still works for names like Janis Joplin, let’s run the test again:



