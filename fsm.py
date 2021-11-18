

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


def bikin_flat(l: list[list]):
    return [item for sublist in l for item in sublist]


def accepts(transisi: dict[int, dict[str, int]], node_inisial: int, node_penerima: list[int], input_string: str):
    node = node_inisial
    for c in input_string:
        if c not in bikin_flat([transisi[x].keys() for x in transisi.keys()]):
            return f"Tidak diterima (alasan: terminal '{c}' tidak ada dalam kamus pada DFA ini)"

        node = transisi[node][c]
    return "Diterima" if node in node_penerima else f"Tidak diterima (alasan: node q{node} bukan node penerima)"


print(accepts(dfa1, 0, [0, 1], 'aaabbaba'))
