# Send data to a server using urllib

# TODO: import the request and parse modules
import urllib.request
import urllib.parse


def main():
    url = "http://httpbin.org/get"

    # TODO: create some data to pass to the GET request
    args = {
        'name': 'Joe Marini',
        'is_auther': True
    }


    # TODO: the data needs to be url-encoded before passing as arguments
    data = urllib.parse.urlencode(args)


    # TODO: issue the request with the data params as part of the URL
    result = urllib.request.urlopen(url + '?' + data)

    # TODO: issue the request with a data parameter to use POST

    print("Result code: {0}".format(result.status))
    print("Returned data: ----------------------")
    print(result.read().decode("utf-8"))


if __name__ == "__main__":
    main()
