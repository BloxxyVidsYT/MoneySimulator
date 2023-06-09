from termcolor import colored
import time
import os

def clr_display():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(stats):
    clr_display()
    if not stats['inventory']['Mysterious Shard'] > 24:
        print(colored("You can't afford to craft any of your items!"))
        time.sleep(1.75)
        return
    
    if stats['BoosterTotal'] >= 5:
        print(colored("You've made the maximum amount of boosters in this playthrough!  Use your shards for other purposes!", "red"))
        time.sleep(1.75)
        return
    print(colored("You Can Craft a Booster!", "green"))
    time.sleep(1)

    while True:
        craftingInput = input(colored("Would you like to craft a booster? Y/N\n›› ", "yellow"))

        if craftingInput == "n":
            print(colored("Okay Then!  Come Back Soon!", "red"))
            time.sleep(1.25)
            return
        
        elif craftingInput == "y":
            stats['inventory']['Mysterious Shard'] -= 25
            stats['inventory']['Booster'] += 1
            stats['BoosterTotal'] += 1
            print(colored("You successfully crafted a booster!", "green"))
            time.sleep(1.75)
            return
        
        else:
            print(colored("Invalid Answer!"))
            time.sleep(0.5)

if __name__ == "__main__":
    print("It doesn't work like that!  Try running main.py to play Money Simulator!")