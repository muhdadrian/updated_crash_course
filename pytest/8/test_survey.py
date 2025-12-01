from survey import AnonymousSurvey


def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    assert "English" in language_survey.responses


def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ["English", "Spanish", "Mandarin"]  # 1
    for response in responses:
        language_survey.store_response(response)

    for response in responses:  # 2
        assert response in language_survey.responses


# We call the new function test_store_three_responses(). We create a survey object just like we did in test_store_single_response(). We define a list containing three different responses ❶, and then we call store_response() for each of these responses. Once the responses have been stored, we write another loop and assert that each response is now in language_survey.responses ❷.
# When we run the test file again, both tests (for a single response and for three responses) pass:
# $ pytest test_survey.py
# ========================= test session starts =========================
# --snip--
# test_survey.py ..                                                [100%]
# ========================== 2 passed in 0.01s ==========================


# This works perfectly. However, these tests are a bit repetitive, so we’ll use another feature of pytest to make them more efficient.

# In test_survey.py, we created a new instance of AnonymousSurvey in each test function. This is fine in the short example we’re working with, but in a real-world project with tens or hundreds of tests, this would be problematic.

# In testing, a fixture helps set up a test environment. Often, this means creating a resource that’s used by more than one test. We create a fixture in pytest by writing a function with the decorator @pytest.fixture. A decorator is a directive placed just before a function definition; Python applies this directive to the function before it runs, to alter how the function code behaves. Don’t worry if this sounds complicated; you can start to use decorators from third-party packages before learning to write them yourself.

# Let’s use a fixture to create a single survey instance that can be used in both test functions in test_survey.py at 9
