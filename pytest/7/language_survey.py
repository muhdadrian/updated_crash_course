from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()

# This program defines a question ("What language did you first learn to speak?") and creates an AnonymousSurvey object with that question. The program calls show_question() to display the question and then prompts for responses. Each response is stored as it is received. When all responses have been entered (the user inputs q to quit), show_results() prints the survey results:

# What language did you first learn to speak?
# Enter 'q' at any time to quit.

# Language: English
# Language: Spanish
# Language: English
# Language: Mandarin
# Language: q

# Thank you to everyone who participated in the survey!
# Survey results:
# - English
# - Spanish
# - English
# - Mandarin

# This class works for a simple anonymous survey, but say we want to improve AnonymousSurvey and the module it’s in, survey. We could allow each user to enter more than one response, we could write a method to list only unique responses and to report how many times each response was given, or we could even write another class to manage non-anonymous surveys.

# Implementing such changes would risk affecting the current behavior of the class AnonymousSurvey. For example, it’s possible that while trying to allow each user to enter multiple responses, we could accidentally change how single responses are handled. To ensure we don’t break existing behavior as we develop this module, we can write tests for the class.
