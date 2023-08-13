import os,random,time
def version():
    print("PyShell Version 2.0BETA")
    print("---------------------------")
    print("Based On Python (3.8)\nWindows NT")
    print("\n\n\n")
    print("Warning:Don't use PyShell on Windows(R)Vista or earlier versions or other platforms")
    print("If you do that,Unknown Errors will happen.")

    print("\n\n")

def main():
    print("PyShell\nVersion 2.0.0 Beta Edition")
    print("---------------------------")
    print("For more information,visit:")
    print("https://github.com/OierMYD/PyShell")
    print("\n\n")
    print("PyShell:/")
    while True:
        op = input()
        if op == "ver":
            version()
        elif op == "exit":
            break;
        else :
            os.system("start "+op)
            
        
main()

