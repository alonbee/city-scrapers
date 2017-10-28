import os
import urllib3
from scrapy.http import HtmlResponse, Request, TextResponse


def file_response(file_name, url=None):
    """
    Create a Scrapy fake HTTP response from a HTML file
    @param file_name: The relative filename from the tests directory,
                      but absolute paths are also accepted.
    @param url: The URL of the response.
    returns: A scrapy HTTP response which can be used for unittesting.

    Based on https://stackoverflow.com/a/12741030, a nice bit of hacking.
    """
    if not url:
        url = 'http://www.example.com'

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    request = Request(url=url)
    file_content = read_test_file_content(file_name)

    if file_name[-5:] == '.json':
        body = file_content
        return TextResponse(url=url, body=body, encoding='utf-8')

    body = str.encode(file_content)
    return HtmlResponse(url=url, request=request, body=body)


def read_test_file_content(file_name):
    if not file_name[0] == '/':
        tests_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(tests_dir, file_name)
    else:
        file_path = file_name

    return open(file_path, 'r').read()


def test_item():
    return {
        '_type': 'event',
        'name': 'Committee on Pedestrian Safety',
        'description': 'A longer description',
        'classification': 'committee-meeting',
        'start_time': '2017-08-30T17:30:00Z',
        'end_time': None,
        'timezone': 'America/Chicago',
        'all_day': False,
        'status': 'tentative',

        'location': {
            'url': '',
            'name': '121 N. Lasalle, Chicago, IL',
            'coordinates': {
                'latitude': '41.883868',
                'longitude': '-87.631936'
            }
        },

        'sources': [
            {
                'url': '',
                'note': ''
            }
        ]
    }
