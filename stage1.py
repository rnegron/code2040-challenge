# Raúl Negrón

from urllib2 import Request, urlopen
from json import dumps, loads

# give is the dict I will use to receive the string
give = {'token':'e93395qR0l'}

# get contains the JSON which contains the string
get = Request('http://challenge.code2040.org/api/getstring', data=dumps(give))

# urllib2 is quite ugly!
string = loads(urlopen(get).read())['result']
#that was a mouthfull!

# Here's whats going on: first, urlopen() opens the Request object called get
# then, the read() method for Request objects returns its contents, which
# get sent to loads(). loads() deserializes arguments into Python objects
# (a dict in this case!), which can be indexed. And indeed, the variable string
# gets assigned the key 'result' 's value!
# COOL!

# Using simple string indexing
result = string[::-1]

# response contains the JSON which I will POST back
response = {'token':'e93395qR0l', 'string':result}

# go recieves the result of the POST
go = Request('http://challenge.code2040.org/api/validatestring', data=dumps(response))

# Did I win?
print loads(urlopen(go).read())
