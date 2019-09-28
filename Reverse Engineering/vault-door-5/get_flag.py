import base64
import urllib



secret = str(open('base64_encoded.txt').read()).strip()


print('vault-door-5 encoded flag: ' + secret)

base64_decoded = base64.decodestring(secret)
url_decoded = urllib.unquote(base64_decoded)


print('\n\nvault-door-5 decoded flag: picoCTF{%s}' % url_decoded)
