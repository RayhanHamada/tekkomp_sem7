

dfa1 = {
    0: {'a': 0, 'b': 1},
    1: {'a': 0, 'b': 2},
    2: {'a': 2, 'b': 2},
}

dfa2 = {
    0: {'a': 1},
    1: {'b': 2},
    2: {'a': 1}
}


def accepts(transitions: dict[int, dict[str, int]], initial: int, accepting: list[int], s: str):
    state = initial
    for c in s:
        state = transitions[state][c]
    return "Diterima" if state in accepting else "Tidak diterima"


print(accepts(dfa1, 0, [0, 1], 'aaaabab'))
