import time


def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)


slow_print(
    """    You arrived to a place where you supposed to find farmers house.
    Instead you see that their house is ruined and abandoned.
    The property is overgrown with thick bushes, the windows are boarded up and covered with ivy,
    making it impossible to see inside. The planks on one of the windows appear broken,
    and perhaps with a little effort you will be able to get into the house.
    If you decide to leave, you can go to The Old Farm or Plains.
    """
)
