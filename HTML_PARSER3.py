# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
from html.parser import HTMLParser
class MyHtmlClass(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])

parser = MyHtmlClass()
html_string = ''
for i in range(int(input())):
    html_string += input().rstrip() + '\n'
parser.feed(html_string)
parser.close()
