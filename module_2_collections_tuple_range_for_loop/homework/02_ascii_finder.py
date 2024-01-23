# Write code that loops through all characters
# string and will display each character separately and
# equivalent from an ASCII array using the ord() function

import string

characters = string.ascii_lowercase

for i in characters:
    print(f"Letter: {i}, ASCII: {ord(i)}")
