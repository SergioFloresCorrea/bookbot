from typing import Dict

def print_report(n_words: int, chara_dict: Dict[str, int]) -> None:
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{n_words} words found in the document")

    chara_dict_sorted = {k:v for k, v in sorted(chara_dict.items(), key=lambda item: item[1], reverse=True) if not k.isspace()}
    for chara, value in chara_dict_sorted.items():
        print(f"The '{chara}' character was found {value} times")

def count_characters(text: str) -> Dict[str, int]:
    text = text.lower() # all to lowercase
    chara_dict = {}
    for character in text:
        if not character.isalpha() and not character.isspace():
            continue
        if character not in chara_dict:
            chara_dict[character] = 1
        else:
            chara_dict[character] += 1
    
    return chara_dict

def count_words(text: str) -> int:
    return len(text.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    n_words = count_words(file_contents)
    chara_dict = count_characters(file_contents)
    print_report(n_words, chara_dict)

main()