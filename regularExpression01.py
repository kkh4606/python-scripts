import re


# string = """Hello my Number is 123456789 and
#             my friend's number is 987654321"""

# match = re.findall('\d+', string)

# print(match)


# pattern = re.compile("[a-e]")

# print(pattern.findall("Aye, said Mr. Gibenson Stark"))

# pattern = re.compile('\d')
# print(pattern.findall("I went to him at 11 A.M. on 4th July 1886"))

# pattern = re.compile('\d+')
# print(pattern.findall("I went to him at 11 A.M. on 4th July 1886"))

pattern = re.compile("\w")

print(pattern.findall("He said * in some_lang."))

pattern = re.compile("\w+")
print(pattern.findall("I went to him at 11 A.M., he \
said *** in some_language."))

print(pattern)


pattern = re.compile("\W")
print(pattern.findall("he said *** in some_language."))


pattern = re.compile("ab")

print(pattern.findall("abbabaabbbababbacb"))












