# Application to verify wheather is eligible to caste their vote or not

def eligibleToVote(Age):
    if Age >= 18:
        print("Yes you are eligible to vote.")
    else:
        print("You are not eligible to vote.")
    
age = int(input("Hi, Please enter your age:- "))
eligibleToVote(age)