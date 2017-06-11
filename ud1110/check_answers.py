def check_answers(my_answers,answers):
    """
    Checks the answers provided to a multiple choice quiz and returns the results.
    """
    total = len(answers)
    count_correct = 0
    for index in range(total):
        if my_answers[index] == answers[index]:
            count_correct += 1

    if count_correct/total > 0.7:
        result = "Congratulations, you passed the test!"
    else:
        result = "Unfortunately, you did not pass."

    return result + " You scored {} out of {}.".format(count_correct, total)

print(check_answers([1,2,2,2,3,3,3],[1,2,4,2,3,4,3]))
