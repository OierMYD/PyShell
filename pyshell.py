from os import*
from random import*
from time import*
iostream = input("C:\Windows\System32=>")
if iostream == "mmc":
    system("start mmc")
elif iostream == "cmd":
    system("start cmd")
elif iostream == "powershell" or "PowerShell":
    system("start powershell")
elif iostream == "command" or "command.com" or "Command":
    system("start command")
elif iostream == "explorer" or "Explorer" or "EXPLORER":
    system("start explorer")
elif iostream == "python" or "Python":
    system("start python")
elif iostream == "tpm.msc":
    system("start tpm.msc")
elif iostream == "winver":
    system("start winver")
elif iostream == "ver":
    print("PyShell Running on Windows NT OS")
    print("PyShell V.1.0.0 Preview Devloper Premium Edition")
elif iostream == "edit":
    system("start edit")
elif iostream == "diskmgmt.msc":
    system("start diskmgmt.msc")
