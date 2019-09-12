#!/usr/bin/env python3

"""


This is going to be a web crawler app similar to the one found in the Udacity
'Intro To Computer Science' course.

Stage 1: Extract first URL from Web Page
    Variable 'page' will hold the source code.
    'start_link' holds the start position value of '<a href=' instance in page.

Stage 2:  Transform into a procedure
    Create 'get_next_target' procedure that returns the URL and it's end point.

Stage 3:    Get all the URLs in the document
    Create a while loop that loops through all of the links in the document

Stage 4:
    More to come


"""
import urllib.request

with open("index.html", "r") as myfile:
    page = myfile.read()

print(page)


def get_page(url):
    page = urllib.request.urlopen(url)
    return(str(page.read()))


def get_next_target(s):
    start_link = s.find("<a href=")
    if start_link == -1:
        return(None, 0)
    start_quote = s.find('"', start_link)
    end_quote = s.find('"', start_quote + 1)
    url = s[start_quote + 1:end_quote]
    return(url, end_quote)


def get_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break


def find_last(s, t):
    last_pos = -1
    while True:
        pos = s.find(t[last_pos + 1])
        if pos == -1:
            return(last_pos)
        last_pos = pos

get_all_links(page)
xkcd = get_page('http://www.xkcd.com/353')
get_all_links(xkcd)
