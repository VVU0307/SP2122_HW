from colorama import init, Fore
init(autoreset = True)

#Fore
print(Fore.RED + "Hello World")
print(Fore.YELLOW + "Hi world")
print(Fore.GREEN + "Good morning world")
print(Fore.BLACK + "You can\'t read this in dark theme")
print(Fore.LIGHTWHITE_EX + "You can\'t read this in light theme")

#class
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f"{bcolors.OKGREEN}colorama is fun")
print(f"{bcolors.HEADER}{bcolors.UNDERLINE}The weather is nice")

#class + Fore
print(Fore.RED + f"{bcolors.UNDERLINE}WARNING:", f"{bcolors.BOLD} i like colorama")