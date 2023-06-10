import wikipediaapi
import string


def check_letter_count():
    title_generator = read_titles("small.txt")
    for e in title_generator:
        d = dict.fromkeys(string.ascii_lowercase, 0)
        title = e
        art = get_article(title)
        all_letters = 0
        for i in art:
            if i.lower().isalpha():
                d[i.lower()] = d.get(i.lower(), 0) + 1
                all_letters = all_letters + 1
        avg = {}
        all = 0
        for i in d:
            if d[i] == 0:
                avg[i] = 0
            else:
                avg[i] = d[i] / all_letters
                all = all + avg[i]
        yield avg


def get_article(title):
    w_api = wikipediaapi.Wikipedia('en')
    page = w_api.page(title)
    if page.exists():
        return page.text
    else:
        return ""


def read_titles(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


letter_count_gen = check_letter_count()

for e in letter_count_gen:
    print(e)