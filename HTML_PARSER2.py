# https://docs.python.org/3/library/html.parser.html 

# https://www.hackerrank.com/challenges/html-parser-part-2/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
from html.parser import HTMLParser

class MyHtmlClass(HTMLParser):
    def handle_comment(self, comment_data):
        no_of_lines = len(comment_data.split('\n'))
        if no_of_lines > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        if comment_data.strip():
            print(comment_data)
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

parser = MyHtmlClass()

html_string = ''
for i in range(int(input())):
    html_string += input().rstrip() + "\n"
#print(html_string)
parser.feed(html_string)
parser.close()

#Another method 
'''
class MyHTMLParser(HTMLParser):
        def handle_comment(self, data):
                if "\n" in data:
                        print(">>> Multi-line Comment  ", data, sep="\n")
                else:
                        print(">>> Single-line Comment  ", data, sep="\n")
        def handle_data(self, data):
                if data != "\n":
                        print(">>> Data", data, sep="\n") '''