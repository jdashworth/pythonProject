import os

print("!/bin/sh")
    
num = 468341
for i in range(13):
    num = num + 1
    
    bash = "yt-dlp " + "https://coder-pour-changer-de-vie.systeme.io/course/vivreducode/lecture/" + str(num)

    print(bash) 

print("END")



