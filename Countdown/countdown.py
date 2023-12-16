import time

def countdown(t):
    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end= "\r")
        time.sleep(1)
        print(t)
        t -= 1

    print('Timer Done!')

user_time = input("Enter time in seconds: ")
countdown(int(user_time))