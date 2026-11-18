"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""

#Basic if-statement test
#Since the input value (number) is 15, it gets rejected by the first condition (number < 0),
# ... the second condition (number == 0),
# ... and the third condition (number < 1).
#Then the flow reaches the else statement, and since none of the previous conditions were met,
# ... the flow executes the code in the else statement.
def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'

    print(conclusion)

#Nested conditions if-statement test
#Let's start with the outer if-statment,
# ... which checks whether or not the bool variable is_weekend is true.
#It is true, so the first condition is met and the flow never reaches the outer else statement
#The nested if-statement in the initial if-condition
# ... checks whether or not the bool variable is_raining is true.
#Since it is true, the first nested if-condition passes and its code is executed.
def test_nested_conditions():
    """Nested if statements check multiple conditions in sequence."""

    is_weekend = True
    is_raining = True
    plan = ''

    if is_weekend:
        if is_raining:
            plan = 'Stay indoors'
        else:
            plan = 'Go hiking'
    else:
        plan = 'Go to work'

    assert plan == 'Stay indoors'

    print(plan)

#Multiple else-if branches if-statement test
#The first condition checks if the score is greater than or equal to 90.
#Since score is not, that condition's code is skipped and the next one is checked.
#The first else-if branch (the second condition) checkes
# ... whether score is greater than or equal to 80.
# Since score is greater than 80, the condition is true and that branch's code is executed
def test_multiple_elif_branches():
    """Multiple elif branches can handle several ordered outcomes."""

    score = 82
    grade = ''

    if score >= 95:
        grade = 'A'
    elif score >= 85:
        grade = 'B'
    elif score >= 75:
        grade = 'C'
    else:
        grade = 'F'

    assert grade == 'B'

    print(grade)


test_if_statement()
test_nested_conditions()
test_multiple_elif_branches()
