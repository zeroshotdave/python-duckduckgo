==================
python-duckduckgo
==================

A Python library for querying the DuckDuckGo API.

Copyright Michael Stephens <me@mikej.st>, released under a BSD-style license.

Source: http://github.com/crazedpsyc/python-duckduckgo
Original source: http://github.com/mikejs/python-duckduckgo (outdated)

This version has been forked from the original to handle some new features of the API, and switch from XML to JSON.

Installation
============

To install run

    ``python setup.py install``

Usage
=====

    >>> import duckduckgo
    >>> r = duckduckgo.query('DuckDuckGo')
    >>> r.type
    'answer'
    >>> r.results[0].text
    'Official site'
    >>> r.results[0].url
    'http://duckduckgo.com/'
    >>> r.abstract.url
    'http://en.wikipedia.org/wiki/Duck_Duck_Go'
    >>> r.abstract.source
    'Wikipedia'
    
    >>> r = duckduckgo.query('Python')
    >>> r.type
    'disambiguation'
    >>> r.related[6].text
    'Python (programming language), a computer programming language'
    >>> r.related[6].url
    'http://duckduckgo.com/Python_(programming_language)'

    >>> r = duckduckgo.query('1 + 1')
    >>> r.type
    'nothing'
    >>> r.answer.text
    '1 + 1 = 2'
    >>> r.answer.type
    'calc'

    # query() takes some special arguments, and passes the rest directly to the API.
    >>> print duckduckgo.query('19301', kad='es_ES').answer.text
    19301 es un código postal de Paoli, PA
    >>> print duckduckgo.query('how to spell test', html=True).answer.text
    <b>Test</b> appears to be spelled right!<br/><i>Suggestions: </i>test, testy, teat, tests, rest, yest.

    # Special keyword args:
    #   useragent   - string, The useragent used to make API calls. This is somewhat irrelevant, as they are not logged or used on DuckDuckGo, but it is retained for backwards compatibility.
    #   safesearch  - boolean, enable or disable safesearch.
    #   html        - boolean, Allow HTML in responses?

