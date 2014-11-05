# Raúl Negrón

from urllib2 import Request, urlopen
from json import dumps, loads

# give is the dict I will use to receive the string and the array
give = {'token':'e93395qR0l'}

# get contains the JSON which contains the string and the array
get = Request('http://challenge.code2040.org/api/haystack', data=dumps(give))

# Let's untangle that data and find our dict!
received = loads(urlopen(get).read())['result']

# Let's assign our variables from the dictionary
needle = received['needle']
haystack = received['haystack']

# Using array methods
position = haystack.index(needle)

# response contains the JSON which I will POST back
response = {'token':'e93395qR0l', 'needle':position}

# go recieves the result of the POST
go = Request('http://challenge.code2040.org/api/validateneedle', data=dumps(response))

# Did I win?
print loads(urlopen(go).read())
