import time
from time import sleep
from tqdm import tqdm
from plyer import notification

count = 0 
print("The pomodoro timer has started, start working!")

if __name__ == "__main__":
    for i in tqdm(range(100)):
        sleep(18)
    while True:
        time.sleep(1800)
        count += 1800
        notification.notify(
            title = "Good work!",
            message = "Take a 10 minute break! You have completed"
        )


        time.sleep(600)
        notification.notify(
            title = "Back to work!",
            message = "Try and doing another pomodoro...",
        )

