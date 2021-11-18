

def bikin_flat(l: list[list]):
    return [item for sublist in l for item in sublist]


# referensi => https://stackoverflow.com/questions/35272592/how-are-finite-automata-implemented-in-code/35279645

def accepts(transisi: dict[int, dict[str, int]], node_inisial: int, node_penerima: list[int], input_string: str):
    node = node_inisial
    print(f"Mulai tracing string '{input_string}': ")
    for idx, c in enumerate(input_string):
        print(f"=> M(q{node}, {input_string[idx:]})")
        if c not in bikin_flat([transisi[x].keys() for x in transisi.keys()]):
            return f"String '{input_string}' TIDAK DITERIMA (alasan: terminal '{c}' tidak ada dalam kamus pada DFA ini)\n"

        node = transisi[node][c]
    return f"String '{input_string}' DITERIMA\n" if node in node_penerima else f"String '{input_string}' TIDAK DITERIMA (alasan: node q{node} bukan node penerima)\n"


# soal 2
print('DFA 1')
node_awal = 0
node_penerima = [0, 1]
dfa1 = {
    0: {'a': 0, 'b': 1},
    1: {'a': 0, 'b': 2},
    2: {'a': 2, 'b': 2},
}

# abababaa
print(accepts(dfa1, node_awal, node_penerima, 'abababaa'))

# aaaabab
print(accepts(dfa1, node_awal, node_penerima, 'aaaabab'))

# aaabbaba
print(accepts(dfa1, node_awal, node_penerima, 'aaabbaba'))


# soal 3
print('DFA 2')
node_awal = 0
node_penerima = [2]
dfa2 = {
    0: {'a': 1},
    1: {'b': 2},
    2: {'a': 1}
}

# abab
print(accepts(dfa2, node_awal, node_penerima, 'abab'))

# ababa
print(accepts(dfa2, node_awal, node_penerima, 'ababa'))
