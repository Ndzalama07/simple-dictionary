import json
from pathlib import Path
import difflib

read_data = Path("data.json").read_text()
data = json.loads(read_data)


def search(query):
    if query in data:
        return data[query]
    else:
        return None


def main():
    while True:
        user_search = input("Search for a word (type 'e' or 'q' to quit): ").lower()
        if user_search in ["e", "q"]:
            break
        matches = difflib.get_close_matches(user_search, data.keys())
        result = search(user_search)
        if result is not None:
            print(f"Definitions for word {user_search}")
            for definition in result:
                print(f"-{definition}")
        else:
            print(f"Word {user_search} not found. Did you mean {matches}?")


if __name__ == "__main__":
    main()
