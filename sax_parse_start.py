# parse XML data using the SAX parser

import requests
import xml.sax

# TODO: define the ContentHandler subclass for our content
class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slideCount = 0
        self.itemCount = 0
        self.isInTitle = False

    #TODO: Handle startElement
    def startElement(self, tagName, attrs):
        if tagName == 'slideshow':
            print('Slideshow title: ' + attrs['title'])
        elif tagName == 'slides':
            self.slideCount += 1
        elif tagName == 'item':
            self.itemCount += 1
        elif tagName == 'Title':
            self.isInTitle = True

    #TODO: Handle endElement
    def endElement(self, tagName):
        if tagName == 'title':
            self.isInTitle = False

    #TODO: Handle text data
    def charachters(self, chars):
        if self.isInTitle:
            print('Title: ' + chars)

    #TODO: Handle startDocument
    def startDocument(self):
        print('About to start!')

    #TODO: Handle endDocument
    def endDocument(self):
        print('Finishing up!')


def main():
    # create a new content handler for the SAX parser
    handler = MyContentHandler()

    # use the Requests lib to get XML data from the server
    # remember that Requests auto-decodes our content
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    print(result.text)

    # TODO: call the parseString method on the XML text content received
    xml.sax.parseString(result.text, handler)


    # when we're done, print out some interesting results
    print("There were {0} slide elements".format(handler.slideCount))
    print("There were {0} item elements".format(handler.itemCount))


if __name__ == "__main__":
    main()
