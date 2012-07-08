import urllib
import urllib2
import json as j

__version__ = 0.2


def query(query, useragent='python-duckduckgo '+str(__version__), safesearch=True, html=False, **kwargs):
    """
    Query DuckDuckGo, returning a Results object.

    Here's a query that's unlikely to change:

    >>> result = query('1 + 1')
    >>> result.type
    'nothing'
    >>> result.answer.text
    '1 + 1 = 2'
    >>> result.answer.type
    'calc'

    Keword arguments:
    useragent: UserAgent to use while querying. Default: "python-duckduckgo %d" (str)
    safesearch: True for on, False for off. Default: True (bool)
    html: True to allow HTML in output. Default: False (bool)
    Any other keyword arguments are passed directly to DuckDuckGo as URL params.
    """ % __version__

    safesearch = '1' if safesearch else '-1'
    html = '0' if html else '1'
    params = {
        'q': query,
        'o': 'json',
        'kp': safesearch,
        'no_redirect': '1',
        'no_html': html,
        }
    params.update(kwargs)
    encparams = urllib.urlencode(params)
    url = 'http://duckduckgo.com/?' + encparams

    request = urllib2.Request(url, headers={'User-Agent': useragent})
    response = urllib2.urlopen(request)
    json = j.loads(response.read())
    response.close()

    return Results(json)


class Results(object):

    def __init__(self, json):
        self.type = {'A': 'answer', 'D': 'disambiguation',
                     'C': 'category', 'N': 'name',
                     'E': 'exclusive', '': 'nothing'}[json.get('Type','')]

        self.api_version = None # compat

        self.heading = json.get('Heading', '')

        self.results = [Result(elem) for elem in json.get('Results',[])]
        self.related = [Result(elem) for elem in
                        json.get('RelatedTopics',[])]

        self.abstract = Abstract(json)
        self.redirect = Redirect(json)
        self.definition = Definition(json)
        self.answer = Answer(json)

        self.image = Image({'Result':json.get('Image','')})


class Abstract(object):

    def __init__(self, json):
        self.html = json.get('Abstract', '')
        self.text = json.get('AbstractText', '')
        self.url = json.get('AbstractURL', '')
        self.source = json.get('AbstractSource')

class Redirect(object):

    def __init__(self, json):
        self.url = json.get('Redirect', '')

class Result(object):

    def __init__(self, json):
        self.html = json.get('Result')
        self.text = json.get('Text')
        self.url = json.get('FirstURL')

        icon_json = json.get('Icon')
        if icon_json is not None:
            self.icon = Image(icon_json)
        else:
            self.icon = None


class Image(object):

    def __init__(self, json):
        self.url = json.get('Result')
        self.height = json.get('Height', None)
        self.width = json.get('Width', None)


class Answer(object):

    def __init__(self, json):
        self.text = json.get('Answer')
        self.type = json.get('AnswerType', '')

class Definition(object):
    def __init__(self, json):
        self.text = json.get('Definition','')
        self.url = json.get('DefinitionURL')
        self.source = json.get('DefinitionSource')
