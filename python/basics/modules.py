"""In this exercise, you will need to print an alphabetically sorted list of
all functions in the re module, which contain the word find."""

import re

find_members = []
for member in dir(re):
    if member.find('find') > -1:
        find_members.append(member)

print(sorted(find_members))
