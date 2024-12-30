from time import time,sleep
import random as r

def mistakes(main_test,user_test):
    error=0
    for i in range(len(main_test)):
        try:
            if main_test[i]!=user_test[i]:
                error=error + 1
        except:
            error=error+1
    return error

def typing_speed(start_time,end_time,user_test):
    time_diff= end_time-start_time
    round_time=round(time_diff,2)
    '''rounding of time to 2 decimal place'''
    speed=len(user_test)/round_time
    return round(speed)

def accuracy(main_test,user_test):
    correct=len(main_test)-mistakes(main_test,user_test)
    accuracy_percentage= (correct/len(main_test))*100
    return round(accuracy_percentage,2)

while True:
    check=input("Ready To Start The Test (yes / no): ")
    if check == "yes":
        test=["In the middle of every difficulty lies opportunity.","The only way to do great work is to love what you do",
        "Abhinav Dwivedi is a Computer Science sophomore at UPES","we are in the middle of testing our speed"]

        act_test=r.choice(test)
        print("-------TYPING SPEED TEST-------")
        print("\n")
        print("Type This Phrase-")
        print(act_test)

        sleep(1)
        time_start=time()
        input_test=input("Enter Here: ")
        time_end=time()

        print("\nResults:")
        print("Typing Speed:",typing_speed(time_start,time_end,input_test),"WPM")
        print("Mistakes:",mistakes(act_test,input_test))
        print("Accuracy Percentage:",accuracy(act_test,input_test),"%")


    elif check=="no":
        print("Thank you Four Visiting. ")
        break
    else:
        print("Enter The Correct Option")
