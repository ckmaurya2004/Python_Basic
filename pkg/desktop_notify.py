from plyer import  notification
import time 

if __name__ == '__main__':
    while True:
        notification.notify(title = 'Take Rest', message = 'Rest is very important for us and our health ',app_icon = '/home/kiran/img.ico',timeout = 5)
        time.sleep(4)