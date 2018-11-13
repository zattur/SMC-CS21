# A program to help you calculate your final grade in case the teacher doesn't
# show it on moodle.
def get_grade():
    tot_percent = 0
    points = 0
    score_obtained = 0
    loop = "y"
    while tot_percent < 1 or loop == "y":
        
        grade_test = float(input("Tell me the percentage grade you received in decimals: "))
        grade_percent = float(input("Tell me the percentage of the final grade in decimals: "))
        grade_percent = 100 * grade_percent
        tot_percent += grade_percent
        score_obtained += (grade_test * grade_percent)
        loop = eval(input("type y if you have more grade to evaluate: "))
    grade = s
    return score_obtained
