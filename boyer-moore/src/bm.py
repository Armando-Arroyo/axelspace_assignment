from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    for value, char in enumerate(pattern):
        table[char] = value
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        c_idx = self.table[c]
        if c_idx < len(self.text):
            slide = len(self.pattern)-self.table[c]
        return slide
        # return self.table[c]

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
        slide = 0
        while slide <= t_len-p_len:
            j = p_len - 1
            while j >= 0 and pattern[j] == text[slide+j]:
                j -= 1
            if j < 0:
                pos = slide
                positions.append(pos)
                try:
                    slide += self.decide_slide_width(text[slide+p_len])
                except Exception:
                    slide = 1
            else:
                slide += max(j-km_table[text[slide+j]], 1)
        return positions[0] if positions else -1
