def words_counter(text):
    return len(text.split())

def characters_counter(text):
    chars = {}
    for c in text.lower():
        if not c.isalpha(): continue

        if c not in chars: chars[c] = 1
        else: chars[c] += 1

    return chars

def dictToList(dict):
    list = []

    for k in dict:
        list.append({"char": k, "num": dict[k]})   

    return list

def sort_on(dict):
    return dict["num"]


def main():
    path = "./books/frankenstein.txt"
    contents = None
    report = ""

    with open(path) as f: contents = f.read()

    words_number = words_counter(contents)
    chars_dict = characters_counter(contents)
    list = dictToList(chars_dict)

    list.sort(reverse=True, key=sort_on)

    report = f"--- Begin report of {path} ---\n{words_number} words found in the document\n"

    for c in list:
        report += f"\nThe '{c["char"]}' character was found {c["num"]} times"


    report += "\n--- End report ---"
    print(report)

    
main()










