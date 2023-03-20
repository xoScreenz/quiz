# Created by Christopher Pulevaka
#This quiz is based on the bible. it tests your knowledge on how well you know about the bible

# This is a function called check(). It requires 2 arguments. one list and one user input. It returns correct if the user input is in the list. it returns incorrect if the user is not on the list
score = 0
def check(options, user_input):
    if user_input in options:
        return True 
    else:
        return False

options = ["39"]
question_one = input("How many books are in the old testament? Is it: \n A) 9 \n B) 33 \n C) 39 \n D) 31 ")
# print(check(options, question_one))
if check(options, question_one):
    print("Good job, you are a smart individual")
    score += 1
else:
    print("Sorry but the answer was 39")



options = ["Moses", "moses", "MOSES", "MoSeS"]
question_one = input("What man wrote the first five books of the Old Testament? Is it: \n A) Moses \n B) Jesus Christ \n C) Joseph \n D) Lebron James ")
# print(check(options, question_one))
if check(options, question_one):
    print("Correct, You have good knowledge of the bible")
    score += 1
else:
    print("Damn the answer was Moses")



options = ["A sling and a stone", "A SLING AND A STONE", "a sling and a stone", "A Sling And A Stone"]
question_one = input("What did David use to defeat Goliath? Is it: \n A) His fist and his knife \n B) Himself and his 40 \n C) A sling and a stone \n D) Some Boxing gloves? ")
# print(check(options, question_one))
if check(options, question_one):
    print("Correct")
    score += 1
else:
    print("Sorry but the answer was ")



options = ["Prevails with god", "PREVAILS WITH GOD", "Prevails With God"]
question_one = input("What does the word Israel mean? Is it: \n A) A coat of many colors \n B) Prevails with god \n C) A servant \n D) A wise man ")
# print(check(options, question_one))
if check(options, question_one):
    print("Nice one, Try get all of them correct")
    score += 1
else:
    print("Sorry but the answer was Prevails with god")



options = ["Thou shall not steal", "THOU SHALL NOT STEAL", "Thou Shall Not Steal"]
question_one = input("What is the eighth commandment? Is it: \n A) Thou shall not steal \n B) Thou shall commit adultery \n C) Thou shall honour thy father and thy mother \n D) Thou shall not kill ")
# print(check(options, question_one))
if check(options, question_one):
    print("Amazing, Now try get most of them correct")
    score += 1
else:
    print("Sorry but the answer was Thou Shall Not Steal")



options = ["Matthew, Mark, Luke, And John", "MATTHEW, MARK, LUKE, AND JOHN", "Matthew, Mark, Luke, And John", "matthew, mark, luke, and john"]
question_one = input("What are the four Gospels in the New Testament? Could it be: \n A) Jake Paul, KSI, Logan Paul, DEJI, \n B) Matthew, Mark, Luke, And John, \n C) James, Matthew, Matt, Nate, \n D) Genesis, Exodus, Leviticus, Deuteronomy? ")
# print(check(options, question_one))
if check(options, question_one):
    print("Correct")
    score += 1
else:
    print("Sorry but the answer was Matthew, Mark, Luke, And John")



options = ["Heaven", "HEAVEN", "heaven"]
question_one = input("Where did Jesus go 40 days after His resurrection? Was it: \n A) Hell \n B) His Mansion \n C) Heaven \n D) The Ground ")
# print(check(options, question_one))
if check(options, question_one):
    print("Excelent")
    score += 1
else:
    print("Sorry but the answer was Heaven")



options = ["Adam", "ADAM", "adam"]
question_one = input("Who was the first man? Was it: \n A) John Cena \n B) Eve \n C) Kay Flock \n D) Adam ")
# print(check(options, question_one))
if check(options, question_one):
    print("Good job, Well done")
    score += 1
else:
    print("Sorry but the answer was Adam")



options = ["Noah", "NOAH", "noah"]
question_one = input("Who did God tell to build an ark? Was it: \n A) Noah \n B) Mark \n C) Luke \n D) James? ")
# print(check(options, question_one))
if check(options, question_one):
    print("Correct")
    score += 1
else:
    print("Wrong answer but try and get one more correct")



options = ["39"]
question_one = input("How many days and nights did it rain when Noah was on the ark? Is it: \n A) 40 \n B) 39 \n C) 38 \n D) 37? ")
# print(check(options, question_one))
if check(options, question_one):
    print("Well Done Individual")
    score += 1
else:
    print("Imagine not getting the last one correct")

print("Congrats you got {} right! Hooray, you did a great job.".format(score))