import duckduckgo  

r = duckduckgo.query('DuckDuckGo')  
r.type=u'answer'  
r.results[0].text=u'Official site'  
r.results[0].url=u'http://duckduckgo.com/'  
r.abstract.url=u'http://en.wikipedia.org/wiki/Duck_Duck_Go'  
r.abstract.source=u'Wikipedia'

r = duckduckgo.query('Python')  
r.type=u'disambiguation'  
r.related[1].text=u'Python (programming language), a computer programming language'  
r.related[1].url=u'http://duckduckgo.com/Python_(programming_language)'  
r.related[7].topics[0].text # weird, but this is how the DDG API is currently organized u'Armstrong Siddeley Python, an early turboprop engine'

r = duckduckgo.query('1 + 1')  
r.type=u'nothing'  
r.answer.text=u'1 + 1 = 2'  
r.answer.type=u'calc'

print(duckduckgo.query('19301', kad='es_ES').answer.text) # 19301 es un código postal de Paoli, PA  
print(duckduckgo.query('how to spell test', html=True).answer.text) # <b>Test</b> appears to be spelled right!<br/><i>Suggestions: </i>test, testy, teat, tests, rest, yest.

print(duckduckgo.get_zci('foo'))