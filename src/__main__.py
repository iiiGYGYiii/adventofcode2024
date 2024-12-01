from importlib import import_module
from importlib.util import find_spec
from os import path

from typing import Optional

DAY_TEMPLATE = "day%(day_number)d"
def log_all_solutions():
    day_number = 1
    current_module = DAY_TEMPLATE % dict(day_number=day_number)

    while find_spec(current_module):
        log_solution(current_module, day_number)
        day_number += 1
        current_module = DAY_TEMPLATE % dict(day_number=day_number)

def log_solution(module_name, day_number: int) -> None:
    module = import_module(module_name)
    module_path = path.dirname(path.realpath(module.__file__))
    filepath = path.join(module_path, "input.txt")
    solution = module.Solution(filepath)

    print(f"""
    SOLUTION DAY {day_number}:

    PART 1:
            {solution.part1()}

    PART 2:
            {solution.part2()}
    """)

def get_cli_args() -> Optional[int]:
    import sys
    try:
        _, args = sys.argv
        if len(args) > 1:
            return None
        day_number = int(args[0])
    except ValueError:
        return None
    return day_number

day_number = get_cli_args()
if day_number:
    current_module = DAY_TEMPLATE % dict(day_number=day_number)
    if find_spec(current_module):
        log_solution(current_module, day_number)
    else:
        print(f"NOT FOUND FOR DAY {day_number}")
else:
    log_all_solutions()
