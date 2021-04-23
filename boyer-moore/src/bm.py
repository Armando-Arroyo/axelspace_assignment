from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    for value, char in enumerate(pattern):
        table.update({f'{char}': value})
    # raise Exception("TODO")
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        return self.table[c]

    def search(self) -> int:
        pattern = self.pattern
        text = self.text
        p_len = len(pattern)
        t_len = len(text)
        km_table = self.table
        positions = []
        for i in range(t_len):
            if text[i] not in km_table:
                km_table[text[i]] = -1
        shift = 0
        while shift <= t_len-p_len:
            j = p_len - 1
            while j >= 0 and pattern[j] == text[shift+j]:
                j -= 1
            if j < 0:
                pos = shift
                positions.append(pos)
                shift += (p_len-self.decide_slide_width(text[shift+p_len]) if shift+p_len < t_len else 1)
            else:
                shift += max(1, j-self.decide_slide_width(text[shift+j]))
        return positions[0] if positions else -1
