import time


def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.001)


def print_one_line_in_frame(text):
    print("+" + "-" * (len(text) + 4) + "+")
    print("|  " + text + "  |")
    print("+" + "-" * (len(text) + 4) + "+")


def print_green(text):
    print("\033[0;32m" + text + "\033[0m")


def print_red(text):
    print("\033[0;31m" + text + "\033[0m")


def print_yellow(text):
    print("\033[0;33m" + text + "\033[0m")
