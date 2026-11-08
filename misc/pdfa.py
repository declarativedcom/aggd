#!/usr/bin/env python3

import sys
sys.path.append("/home/henrique/anaceo/aggd/misc/pypdf")
from pypdf import PdfReader


def main():
    a_pdf_text(sys.argv[1:])


def a_pdf_text(files):
    res = [
        (name, pdf_text(name))
        for name in files
    ]
    if len(files) <= 1:
        _, one = res[0]
        text = swift(one)
        print(text)
        return [(one, text)]
    these = []
    for name, cont in res:
        print(f"---- [{name}] ----")
        text = swift(cont)
        print(text, end="\n\n")
        these.append((name, text))
    return these

def swift(lst):
    res = '----\n'.join(lst) + '\n'
    return res

def pdf_text(filename):
    reader = PdfReader(filename)
    res = []
    for page_num, page in enumerate(reader.pages, start=1):
        #print(f"----- PAGE {page_num} -----")
        text = page.extract_text()
        res.append(text)
    return res


if __name__ == "__main__":
    main()
