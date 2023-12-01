import os
import pathlib

def get_input_file(day):
    return (pathlib.Path(__file__).parent / 'inputs' / str(day)).resolve()

def get_input(day):
    path = get_input_file(day)
    if not os.path.isfile(path):
        raise FileNotFoundError(f'https://adventofcode.com/2023/day/{day}/input')
    return path

