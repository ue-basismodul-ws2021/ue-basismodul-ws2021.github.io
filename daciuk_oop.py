from collections import OrderedDict


class MinDict:
    def __init__(self, ...):
        self.initial_state = State()
    pass

    # ...
    # last_child = state.last_child
    # state.last_child = new_child


class State:
    def __init__(self):
        self.is_final = False
        self.tr = OrderedDict[str, State] = OrderedDict()

    def __eq__(self, other):
        if self.is_final is other.final \
                and self.tr == other.tr:
            return True
        return False

    @property
    def last_child(self):
        return self.tr[next(reversed(self.tr))]

    @last_child.setter
    def last_child(self, new_child):
        self.tr[next(reversed(self.tr))] = new_child
