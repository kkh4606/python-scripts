import re



# print(re.escape('This is Awsome even 1 AM'))
# print(re.escape('I asked what is this [a-9], he said \t Wow'))


regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, 'I was born  June 24')

if match:
    print("Match at index %s, %s" % (match.start(), match.end()))
    print("full match: ", match.group())
    print("month: ", match.group(1))
    print("day: ", match.group(2))
else:
    print('The regex pattern does not match')