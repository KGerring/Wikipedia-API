# -*- coding: utf-8 -*-

import logging

import wikipediaapi

logging.basicConfig(level=logging.INFO)


wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('Python_(programming_language)')

print(f"Page - Exists: {page_py.exists()}")
print(f"Page - Id: {page_py.pageid}")
print(f"Page - Title: {page_py.title}")
print(f"Page - Summary: {page_py.summary[:60]}")


def print_sections(sections, level=0):
    for s in sections:
        print(f'{"*" * (level + 1)}: {s.title} - {s.text[:40]}')
        print_sections(s.sections, level + 1)


print("Sections:")
print_sections(page_py.sections)


def print_langlinks(page):
    langlinks = page.langlinks
    for k in sorted(langlinks.keys()):
        v = langlinks[k]
        print(f"{k}: {v.language} - {v.title}: {v.fullurl}")


print("Lang links:")
print_langlinks(page_py)


def print_links(page):
    links = page.links
    for title in sorted(links.keys()):
        print(f"{title}: {links[title]}")


print("Links:")
print_links(page_py)


def print_categories(page):
    categories = page.categories
    for title in sorted(categories.keys()):
        print(f"{title}: {categories[title]}")


print("Categories")
print_categories(page_py)

section_py = page_py.section_by_title('Features and philosophy')
if section_py is not None:
    print(f"Section - Title: {section_py.title}")
    print(f"Section - Text: {section_py.text[:60]}")
else:
    print("Section does not exist.")

wiki_html = wikipediaapi.Wikipedia(
    language='cs',
    extract_format=wikipediaapi.ExtractFormat.HTML
)

page_ostrava = wiki_html.page('Ostrava')
print(f"Page - Exists: {page_ostrava.exists()}")
print(f"Page - Id: {page_ostrava.pageid}")
print(f"Page - Title: {page_ostrava.title}")
print(f"Page - Summary: {page_ostrava.summary[:60]}")
print_sections(page_ostrava.sections)

section_ostrava = page_ostrava.section_by_title('Heraldický znak')
if section_ostrava is not None:
    print(f"Section - Title: {section_ostrava.title}")
    print(f"Section - Text: {section_ostrava.text[:60]}")
else:
    print("Section does not exists")

page_nonexisting = wiki_wiki.page('Wikipedia-API-FooBar')
print(f"Page - Exists: {page_nonexisting.exists()}")
print(f"Page - Id: {page_nonexisting.pageid}")
print(f"Page - Title: {page_nonexisting.title}")
print(f"Page - Summary: {page_nonexisting.summary[:60]}")


wiki_de = wikipediaapi.Wikipedia('de')
de_page = wiki_de.page('Deutsche Sprache')
print(f"{de_page.title}: {de_page.fullurl}")
print(de_page.summary[:60])

en_page = de_page.langlinks['en']
print(f"{en_page.title}: {en_page.fullurl}")
print(en_page.summary[:60])


def print_categorymembers(categorymembers, level=0, max_level=2):
    for c in categorymembers.values():
        print("%s %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
        if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            print_categorymembers(c.categorymembers, level + 1, max_level=max_level)


cat = wiki_wiki.page("Category:Physics")
print("Category members: Category:Physics")
print_categorymembers(cat.categorymembers, max_level=1)

wiki_hi = wikipediaapi.Wikipedia('hi')
# fetch page about Python in Hindu
# https://hi.wikipedia.org/wiki/%E0%A4%AA%E0%A4%BE%E0%A4%87%E0%A4%A5%E0%A4%A8

p_hi_python_quoted = wiki_hi.article(
    title='%E0%A4%AA%E0%A4%BE%E0%A4%87%E0%A4%A5%E0%A4%A8',
    unquote=True,
)
print(p_hi_python_quoted.title)
print(p_hi_python_quoted.summary[:60])

