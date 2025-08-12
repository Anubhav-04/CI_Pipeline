# Application to verify wheather the voter is eligible to caste their vote or not

def eligibleToVote(name,Age):
    if Age >= 18:
        print(f"Hi {name} Yes you are eligible to vote.")
    else:
        print(f"Hi {name} You are not eligible to vote.")

name = input("Enter your name:- ")    
age = int(input("Hi, Please enter your age:- "))
eligibleToVote(name,age)