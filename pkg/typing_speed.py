from time import *
import random as r


def mistake(paratext,usertext):
    error =0
    for i in range(len(paratext)):
        try:
           if paratext[i]!= usertext[i]:
            error += 1
        except:
            error = error+1
    return error

def speed_time(time_s,time_e,usertext):
   time_delay = time_e - time_s
   time_r = round(time_delay,2)
   speed = len(usertext)/time_r
   return round(speed)


if __name__ == '__main__':
    while True:
        ch = input("ready to test : y/n  ")
        if ch == 'y':
            test = ["kiran is a good girl","kiran is a intelligent girl","kiran is a pretty girls"]
            test1 = r.choice(test)
            print(" **** testing start ****")
            print(test1)
            print()
            print()
            time_1 = time()
            userinput = input("Enter: ")
            time_2 = time()

            print("error :", mistake(test1, userinput),"w/sec")
            print("speed :", speed_time(time_1,time_2, userinput),"sec")

        elif ch == 'n':
           print('thank you ')
           break

        else:
           print("Sorry")
           break
           






