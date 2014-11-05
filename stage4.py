# Raúl Negrón

import datetime
from urllib2 import Request, urlopen
from json import dumps, loads

# give is the dict I will use to receive the string and the int
give = {'token':'e93395qR0l'}

# get contains the JSON which contains the string and the int
get = Request('http://challenge.code2040.org/api/time', data=dumps(give))

# Let's untangle that data and find our dict!
received = loads(urlopen(get).read())['result']

# Let's assign our variables from the dictionary
datestamp = received['datestamp']
interval = received['interval']

# Manual parsing time!
# We can do this because the datestamp is standardized by ISO 8601
year = int(datestamp[:4])
month = int(datestamp[5:7])
day = int(datestamp[8:10])
hour = int(datestamp[11:13])
minute = int(datestamp[14:16])
second = int(datestamp[17:19])
micro = int(datestamp[20:23])

# Let's now change the datestamp into a datetime object
datestamp = datetime.datetime(year, month, day, hour, minute, second, micro)

# With timedelta, we can safely calculate the time change
interval_delta = datestamp + datetime.timedelta(seconds=interval)

# We now convert that datetime object into its ISO 8601 representation
final_time = interval_delta.isoformat()

# Debugging !
#print 'Interval:', interval
#print 'Current time:', datestamp
#print 'Time after interval:', interval_delta
#print 'Time after interval in ISO 8601:', final_time

# response contains the JSON I will POST back
response = {'token':'e93395qR0l', 'datestamp':final_time}

# go recieves the result of the POST
go = Request('http://challenge.code2040.org/api/validatetime', data=dumps(response))

# Did I win?
print loads(urlopen(go).read())
