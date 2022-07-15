import os
while 1:
    cmd = input("C:\Windows\System32\\")
    if cmd == "exit":
        break
    else:
        os.system("start "+cmd)


