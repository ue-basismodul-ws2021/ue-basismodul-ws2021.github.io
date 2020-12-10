from itertools import count
from collections import OrderedDict


class MinDict:
    def __init__(self, words):
        self.final_states: set[int] = set()
        self.register: set[int] = set()
        self.temp_states: set[int] = set()  # optional
        self.curr_id = count() # next_id = next(curr_id)
        self.tr: dict[int, OrderedDict[str, int]] = dict()
        # ....
        self.compile(words)

    def compile(self, words):
        for word in words:
            pass
            # ...
            # state = 5
            # s_tr = self.tr[state]
            # last_label = next(reversed(s_tr))
            # last_child = str[last_label]

    def add_suffix(self, suffix, state):
        for c in suffix:
            next_state = next(self.curr_id)
            self.tr[state][c] = next_state
            state = next_state
        self.final_states.add(state)
