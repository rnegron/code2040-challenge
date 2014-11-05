# Raúl Negrón

from urllib2 import Request, urlopen
from json import dumps, loads

# give is the dict I will use to receive the string and the array
give = {'token':'e93395qR0l'}

# get contains the JSON which contains the string and the array
get = Request('http://challenge.code2040.org/api/prefix', data=dumps(give))

# Let's untangle that data and find our dict!
received = loads(urlopen(get).read())['result']

# Let's assign our variables from the dictionary
prefix = received['prefix']
array = received['array']

# Initialize an empty array
new_array = []

# For-in loops are very powerful!
for string in array:

    # If the prefix is not in the first len(prefix) characters
    # of string then its... not a preface to the string!
    # We can safely add string to our new array
    if not prefix in string[:len(prefix)]:
        new_array.append(string)

# response contains the JSON which I will POST back
response = {'token':'e93395qR0l', 'array':new_array}

# go recieves the result of the POST
go = Request('http://challenge.code2040.org/api/validateprefix', data=dumps(response))

# Did I win?
print loads(urlopen(go).read())
