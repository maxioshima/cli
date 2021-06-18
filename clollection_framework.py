import argparse
from functools import lru_cache


def create_parser():
    parser = argparse.ArgumentParser(description="Find unique characters in string")
    parser.add_argument("--string", help='This argument for any simple string')
    parser.add_argument("--file", help='This argument for count string from any file',
                        type=argparse.FileType("r", encoding="utf-8"))
    args = parser.parse_args()
    return args


@lru_cache(maxsize=None)
def unique_characters_counter(data):
    unique_characters = []
    [unique_characters.append(data[a]) for a in range(0, len(data)) if
     (data.count(data[a])) == 1]
    [unique_characters.remove(a) for a in unique_characters if a == ' ']
    return len(unique_characters)


if __name__ == '__main__':
    if create_parser().file:
        data = create_parser().file.readlines()
        print(unique_characters_counter(data[0]))
    elif create_parser().string:
        data = create_parser().string
        print(unique_characters_counter(data))
