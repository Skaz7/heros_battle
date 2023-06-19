import time


def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.001)


def print_one_line_in_frame(text):
    print("+" + "-" * (len(text) + 4) + "+")
    print("|  " + text + "  |")
    print("+" + "-" * (len(text) + 4) + "+")
