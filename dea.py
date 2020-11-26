import graphviz


class DEA:

    def __init__(self, sigma, states, delta, initial_state, final_states):
        self.sigma = sigma
        self.states = states
        self._delta = {(q_from, label): q_to for q_from, label, q_to in delta}
        self.initial_state = initial_state
        self.final_states = final_states

    @property
    def delta(self):
        return {(q_from, label, q_to) for (q_from, label), q_to in self._delta.items()}

    def transition(self, q_from, label):
        try:
            return self._delta[(q_from, label)]
        except KeyError:
            return None

    def accepts(self, word):
        q = self.initial_state
        for char in word:
            q = self.transition(q, char)
            if q is None:
                return False
        return q in self.final_states


def draw_automaton(aut):

    g = graphviz.Digraph('Automaton')

    for state in aut.states:
        if state in aut.final_states:
            g.attr('node', style='bold')
        if state == aut.initial_state:
            g.node(str(state), label="-> " + str(state))
        else:
            g.node(str(state))
        g.attr('node', style='solid')

    for x, label, z in aut.delta:
        g.edge(str(x), str(z), label=" " + label + " ")

    return g


def main():
    # construction data
    sigma = {"a", "b"}
    states = {1, 2, 3, 4, 5}
    delta = {
        (1, "a", 1), (1, "b", 2),
        (2, "a", 3), (2, "b", 2),
        (3, "a", 5), (3, "b", 4),
        (4, "a", 1), (4, "b", 5),
        (5, "a", 5), (5, "b", 5)
    }
    initial_state = 1
    final_states = {4}

    aut = DEA(sigma, states, delta, initial_state, final_states)

    # tests
    test_data = [
        ("", False),
        ("abc", False),
        ("aab", False),
        ("bbab", True),
        ("baab", False),
        ("abababab", True)
    ]

    for word, should_accept in test_data:
        if aut.accepts(word) != should_accept:
            print(f"""'{word}' was accepted: {not should_accept}
                  Expected was: {should_accept}.""")

    g = draw_automaton(aut)
    g.render('graphviz/aut.gv', view=True)


if __name__ == "__main__":
    main()
