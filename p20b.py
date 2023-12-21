import math
import itertools
import copy
import sys
from typing import Deque, Literal
from collections import Counter, defaultdict, deque

file = open(sys.argv[1]).read().strip()
lines = [line for line in file.split("\n")]

conjs = []
state = {}
inverse = defaultdict(list)
counter = Counter()
for line in lines:
    module, outputs = line.split(" -> ")
    module_name = module.lstrip("%&")
    outputs = outputs.split(", ")
    for o in outputs:
        counter[o] += 1
        inverse[o].append(module_name)
    if module == "broadcaster":
        state["broadcaster"] = {"type": "broadcaster", "outputs": outputs}
    elif module.startswith("%"):
        state[module[1:]] = {"type": "flip-flop", "on": False, "outputs": outputs}
    elif module.startswith("&"):
        state[module[1:]] = {"type": "conj", "inputs": None, "outputs": outputs}
        conjs.append(module[1:])
    else:
        assert False
for conj in conjs:
    state[conj]["inputs"] = {k: "low" for k in inverse[conj]}


def push_button(state, input_awaited):
    initial_pulse = ("button", "low", "broadcaster")
    queue: Deque[tuple[str, Literal["low"] | Literal["high"], str]] = deque(
        [initial_pulse]
    )
    while queue:
        input, pulse, output = queue.popleft()
        if input == input_awaited and pulse == "low":
            return (state, True)
        next_pulse = None
        try:
            next_outputs = state[output]["outputs"]
        except KeyError:
            continue
        if output == "broadcaster":
            next_pulse = pulse
        elif state[output]["type"] == "flip-flop":
            if pulse == "high":
                continue
            if state[output]["on"]:
                next_pulse = "low"
            else:
                next_pulse = "high"
            state[output]["on"] = not state[output]["on"]
        elif state[output]["type"] == "conj":
            state[output]["inputs"][input] = pulse
            if all(input == "high" for input in state[output]["inputs"].values()):
                next_pulse = "low"
            else:
                next_pulse = "high"
        else:
            assert False, (output, state)
        for o in next_outputs:
            queue.append((output, next_pulse, o))
    return (state, False)


cycles = []
# how long it takes each conjunction module associated with its 12 flip-flops to go low
for input in ["jv", "pr", "qs", "jm"]:
    cur_state = copy.deepcopy(state)
    for button_press in itertools.count(1):
        cur_state, done = push_button(cur_state, input)
        if done:
            cycles.append(button_press)
            break
print(math.lcm(*cycles))

# the structure of the graph is roughly
#
#                                       broadcaster
#             /                   /                    \              \
#  12 (chained) flip-flops   12 flip-flops      12 flip-flops    12 flip-flops
#            |                    |                    |                |
#           conj                conj                  conj             conj          <- conj layer 1
#            |                    |                    |                |
#           conj                conj                  conj             conj          <- conj layer 2
#             \                    \                   /               /
#                                           conj                                     <- final conj
#                                             |
#                                            rx
#
# the broadcaster pulse toggles 4 flip-flops (aka bits), each of which is chained with 11 other flip-flops
# to create a 12 bit number. each pulse effectively increments this number. some bits of this number feed
# into a conjunction module (NAND) (conj layer 1 above), which will only send low if its inputs are all high.
# so it must have last received high pulses from these bits. this first happens when those bits are set to 1.
# the bits not feeding into the NAND conveniently receive a pulse from this NAND, so each time the 12-bit number
# is achieved, these remaining bits are set high, so that the number has all bits set. then on the next
# broadcaster pulse, the number is reset to 0.
#
# once we get to an iteration where all of conj layer 1 is set high, then conj layer 2 will be set low, and the
# final conj will be set high, sending a low pulse to rx
#
# this is achieved in the code by identifying the four conjunction modules of conj layer 1, finding when they send
# a low pulse, and taking an LCM of those numbers
