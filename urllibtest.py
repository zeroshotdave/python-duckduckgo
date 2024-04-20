import urllib.request
import duckduckgo

authinfo = urllib.request.HTTPBasicAuthHandler() 
authinfo.add_password(realm='PDQ Application',
                      uri='https://mahler:8092/site-updates.py', user='klem', passwd='geheim$parole')

proxy_support = urllib.request.ProxyHandler({"http" : "http://ahad-haam:3128"})

opener = urllib.request.build_opener(proxy_support, authinfo,
                                     urllib.request.CacheFTPHandler)

urllib.request.install_opener(opener)

f = urllib.request.urlopen('https://ejop.psychopen.eu/index.php/ejop/article/view/1127/1127.pdf')

# ddg_resp = duckduckgo.get_zci('foo')
# print(ddg_resp)
ddg_resp = duckduckgo.query("how do i use urllib python")
print(ddg_resp)



