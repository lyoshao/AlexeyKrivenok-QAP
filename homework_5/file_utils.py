from typing import List, Dict

def read_lines(filename: str) -> List[str]:
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]

def write_lines(filename: str, lines: List[str]) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(f"{line}\n")

def count_words(filename: str) -> Dict[str, int]:
    word_counts: Dict[str, int] = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.lower().split()
            for word in words:
                clean_word = word.strip('.,!?;:"()')
                if clean_word:
                    word_counts[clean_word] = word_counts.get(clean_word, 0) + 1
    return word_counts
