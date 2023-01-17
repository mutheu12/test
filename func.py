# EXAMPLE SOLUTION


def is_even(x):
    return x % 2 == 0


def is_within_range(x, _min, _max):
    return _min <= x <= _max


def red_or_blue(x):
    if not is_even(x) or (is_even(x) and is_within_range(x, 6, 20)):
        return "Red"

    if (is_even(x) and x > 20) or x in [2, 4]:
        return "Blue"

# new func
def average_exam_score(student_marks):
    denominator = len(student_marks)
    marks = []

    for result in student_marks:
        try:
            mark = int(result['mark'])
        except KeyError:
            mark = 5

        if not 10 > mark > 1:
            raise ValueError("Mark is not in the valid range")

        marks.append(mark)

    return sum(marks) / denominator