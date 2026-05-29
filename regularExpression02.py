import re


# print(re.split("\W+", 'Words, words , Words'))
# print(re.split("\W+", "Words's words Words"))
# print(re.split("\W+", 'On 12th Jan 2016, at 11:02 AM'))
# print(re.split("\d+", 'On 12th Jan 2016, at 11:02 AM'))



# print(re.split("\d+", 'On 12th Jan 2016, at 11:02 AM', 1))
# print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
# print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))

# print(re.sub('ub', '~*', 'Subject has Uber book already', flags=re.IGNORECASE))
# print(re.sub('ub', '~*', 'Subject has Uber book already'))
# print(re.sub('ub', '~*', 'Subject has Uber book already', flags=re.IGNORECASE, count=1))
# print(re.sub('\sAND\s', '&', 'Baked Beans And Spam', flags=re.IGNORECASE))

print(re.subn('ub', '~', 'Subject has Uber book already'))
print(re.subn('ub', '~', 'Subject has Uber book already', flags=re.IGNORECASE))






