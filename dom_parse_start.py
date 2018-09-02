# Use the XML DOM to parse a document in memory

import xml.dom.minidom
import requests


def main():
    # retrieve the XML data using the requests library
    url = "http://httpbin.org/xml"
    result = requests.get(url)

    # TODO: parse the returned content into a DOM structure
    domtree = xml.dom.minidom.parseString(result.text)
    rootnode = domtree.documentElement

    # TODO: display some information about the content
    print('The root element is {0}'.format(rootnode.nodeName))
    print('Title: {0}'.format(rootnode.getAttribute('title')))

    items = domtree.getElementsByTagName('item')
    print('There are {0} item tags'.format(items.length))

    # manipulate the XML content in memory
    # TODO: create a new item tag
    newItem = domtree.createElement('item')

    # TODO: add some text to the item
    newItem.appendChild(domtree.createTextNode('This is some text'))

    # TODO: now add the item to the first slide
    firstSlide = domtree.getElementsByTagName('slide')[0]
    firstSlide.appendChild(newItem)

    # TODO: Now count the item tags again
    items = domtree.getElementsByTagName('item')
    print('There are {0} item tags'.format(items.length))


if __name__ == "__main__":
    main()
