import re
import pyperclip

phoneExtracted = re.compile(r"""
(
((\d\d\d) | (\(\d\d\d\)))? # can be 0 or 1 time
(\s|-)
\d\d\d
-
\d\d\d\d
)  # the whole group will give a definate output
          #,whereas other way will give each individual mapping a tuple
""", re.VERBOSE)

emailExtracted = re.compile(r"""
(
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+   # one or more times
)  # the whole group will give a definate output
          #,whereas other way will give each individual mapping a tuple
""", re.VERBOSE)
in_from_clipboard = pyperclip.paste()
numbers = phoneExtracted.findall(in_from_clipboard)
mails = emailExtracted.findall(in_from_clipboard)
#print(numbers)
extracted_phone=[]
for phoneNumbers in numbers:
    extracted_phone.append(phoneNumbers[0])

result = '\n'.join(extracted_phone)+'\n'+'\n'.join(mails)
#pyperclip.copy(result)
print(mails)
print(result)
'''
479-205-4874678-560-3485724-900-2986242-391-3183604-720-6426651-807-8065209-754-9111641-433-6698
7@an@m0@g6@hy@m7@is@c1@o
'''
'''
479-205-4874678-560-3485724-900-2986242-391-3183604-720-6426651-807-8065209-754-9111641-433-6698
7@anm0@g6hy@m7is@c1
'''
