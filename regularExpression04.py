import re
s = 'geeks.forgeeks'

# match = re.search(r'.', s)
# print(match)


# match = re.search(r'\.', s)
# print(match)


# string = "aThe quick brown fox jumps over the lazy dog"
# pattern = "[a-m]"
# result = re.findall(pattern, string)
# print(result)



# string = '10234'
# pattern = '[0,4]'
# print(re.search(pattern, string))



# regex = r'^The'
# strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']


# for string in strings:
#     if re.match(regex, string):
#         print(f'Matched: {string}')
#     else:
#         print(f'Not matched: {string}')




# string = "Hello World!"
# regex = r'World!$'
# 
# match = re.search(regex, string)
# 
# if match:
#     print("Match found!")
# else:
#     print("Match not found")




string = "The quick brown fox jumps over the lazy dog."
pattern = r"brown...fox"

match = re.search(pattern, string)
if match:
    print(match)
else:
    print("Match not found")

























