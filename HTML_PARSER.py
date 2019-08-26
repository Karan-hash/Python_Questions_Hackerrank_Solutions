# Link - https://docs.python.org/2/library/htmlparser.html#HTMLParser.HTMLParser
'''
HTML 
Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.

Parsing 
Parsing is the process of syntactic analysis of a string of symbols. It involves resolving a string 
into its component parts and describing their syntactic roles.

HTMLParser 
An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, 
comments, and other markup elements are encountered.
'''
from html.parser import HTMLParser
# Create a subclass and overriding the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Found a starting tag :", tag)
    def handle_endtag(self, tag):
        print("Found an ending tag :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Found an empty tag :", tag)
parser = MyHTMLParser() #Instantiate the parser and feed it some html 
parser.feed("<html><head><title>HTML Parser - I</title></head>"
            +"<body><h1>HackerRank</h1><br /></body></html>")
