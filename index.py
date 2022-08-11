#!/usr/bin/env python3
from os import stat
from pynput.keyboard import Key, Controller
import time

# -----------------------------------------------------------
target_user = "@Hades" # change this to the target user that would be gifted with the pokemons
start_pokemon_number = 1 # Pokemons starting from this number will be sent
end_pokemon_number = 100 # Pokemons till this number will be sent
# -----------------------------------------------------------

message_format = "p!gift pokemon {target_user} {pokemon_number}" # Message format. Change the user id to which to gift the boat

keyboard = Controller()
start_wait_time = 15 # Start delay (in seconds)
keystroke_delay = 0.05
message_delay = 2 # (in seconds)


def press_key(key):
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(keystroke_delay)

def send_message(message):
    print("Sending message ", message)
    for key in message:
        press_key(key)
    press_key(Key.enter)
    time.sleep(message_delay)

def start():
    for current_pokemon_number in range(start_pokemon_number, end_pokemon_number + 1):
        message = message_format.format(target_user = target_user, pokemon_number = current_pokemon_number)
        send_message(message)
    print("Done!")


def main():
    print("Program will start typing in ", start_wait_time, "seconds...")
    print("Hover over the discord message bar till then...")
    time.sleep(start_wait_time)
    start()


main();