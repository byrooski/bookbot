path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        file = f.read()
        return file
def main(path):
    print(get_book_text(path))


main(path)