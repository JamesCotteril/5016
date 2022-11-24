# functions_and_scope.py
#
# @ author: A. N. Other
# date: September 2016
 
score = 4
 
def show_new_score(param_score):
    param_score += 1
    print("You got another point...\n"
          "Your score is now {0}.\n"
          .format(param_score))
# some run code
x = input("Your score is {0} points...\n\n"
          "Hit any key to get another point. "
          .format(score))
# invoking the function
show_new_score(score)
# test case assertion
#'''
print("Test case assertion: the inital score is 4 "
    "and it should become 5!!")
 
show_new_score(score)
#'''
