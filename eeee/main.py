import time
import random
import keyboard
print("HELLO NEW USER or not...")
time.sleep(1)
exit_I = str.lower(input("do you want to run this?(Y/N): "))

if exit_I[str.find("y", exit_I)] == "y":
    print("OKAY THEN")
    time.sleep(1)
    print("RUNNING")

elif exit_I[str.find("n", exit_I)] == "n":
    print("BYE!")
    time.sleep(1)
    exit()

else:
    print("BYE!")
    time.sleep(1)
    exit()

print("alright we just need a bit of input so please answer")
time.sleep(1)

word_0_input = str.lower(input("do !dep all?(Y/N): "))
word_1_input = str.lower(input("do !bal?(Y/N): "))
word_2_input = str.lower(input("do !collect?(Y/N): "))

number_0_input = 0
if word_2_input[str.find("y", exit_I)] == "y":
    try:
        number_0_input = int(input("how many minutes per !collect?(only in minutes): "))
    except int:
        print("bro fr??")
        time.sleep(1)
        print("pls put in a valid number next time")
        time.sleep(4)
        print("BYE!")
        time.sleep(1)
        exit()

number_1_input = float(input("a delay :troll: how much seconds?(put 0 for no delay): "))


minutes_passed = 0
reset_minutes = 0

word = "!work"
word_0 = "!dep all"
word_1 = "!bal"
word_2 = "!collect"

print("!dep all = " + word_0_input)
print("!bal = " + word_1_input)
print("!collect = " + word_2_input)
print("!collect per minutes = " + str(number_0_input))
print("delay = " + str(number_1_input))
print("exit this console to stop the process")
time.sleep(10)
print("\n"*2)

while True:

    rng = random.randint(1,3)
    rng_0 = random.randint(1, 5)
    wait = 60

    print("minutes passed: " + str(minutes_passed))
    print(wait)

    for index in range(1, wait, 1):
        print(wait-index)
        time.sleep(1)
    time.sleep(number_1_input)
    minutes_passed += 1
    reset_minutes += 1

    print(minutes_passed)
    print("\n"*2)
    print("!work")

    keyboard.write(word)
    keyboard.press('enter')

    if rng == 2 and word_0_input[str.find("y", exit_I)] == "y":

        time.sleep(1.5)

        print("!dep all")

        keyboard.write(word_0)
        keyboard.press('enter')

    if rng_0 == 3 and word_1_input[str.find("y", exit_I)] == "y":

        time.sleep(1.5)

        print("!bal")

        keyboard.write(word_1)
        keyboard.press('enter')
    if reset_minutes >= number_0_input and word_2_input[str.find("y", exit_I)] == "y":
        reset_minutes = 0
        time.sleep(1.5)

        print("!collect")

        keyboard.write(word_2)
        keyboard.press('enter')
    print("\n" * 2)

