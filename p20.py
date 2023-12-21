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
    outputs = outputs.split(", ")
    for o in outputs:
        counter[o] += 1
        inverse[o].append(module.lstrip("%&"))
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


def push_button(state):
    low_pulses = high_pulses = 0
    initial_pulse = ("button", "low", "broadcaster")
    queue: Deque[tuple[str, Literal["low"] | Literal["high"], str]] = deque(
        [initial_pulse]
    )
    while queue:
        input, pulse, output = queue.popleft()
        if output == "rx" and pulse == "low":
            print("hi")
            sys.exit()
        if pulse == "high":
            high_pulses += 1
        else:
            low_pulses += 1
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
        if next_pulse is None:
            assert False
        for o in next_outputs:
            queue.append((output, next_pulse, o))
    return (state, low_pulses, high_pulses)


n = 1000
low_pulse_total = high_pulse_total = 0
cur_state = copy.deepcopy(state)
for i in range(1, n + 1):
    cur_state, low_pulses, high_pulses = push_button(cur_state)
    low_pulse_total += low_pulses
    high_pulse_total += high_pulses

print(low_pulse_total * high_pulse_total)
