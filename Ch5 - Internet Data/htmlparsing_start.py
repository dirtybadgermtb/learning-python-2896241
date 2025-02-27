# 
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
#
from html.parser import HTMLParser
import os

paragraphs = 0
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered a comment:", data)
        pos = self.getpos()
        print("At line:", pos[0], "position", pos[1])

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        pos = self.getpos()
        print("At line:", pos[0], "position", pos[1])
        
        global paragraphs
        if tag == "p":
            paragraphs += 1

    def handle_data(self, data):
        print("Encountered text data:", data)
        if data.isspace():
            return
        pos = self.getpos()
        print("At line:", pos[0], "position", pos[1])

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    
    # Get the absolute path to the HTML file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(current_dir, "samplehtml.html")
    
    try:
        with open(html_file, "r") as f:
            contents = f.read()
            parser.feed(contents)
            print("Paragraph tags:", paragraphs)
    except FileNotFoundError:
        print(f"Error: Could not find file at {html_file}")

if __name__ == "__main__":
    main()
