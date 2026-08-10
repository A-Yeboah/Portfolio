# This program counts the number of words used 
# by a user in a sentence

intro = 'Kindly type your sentences after pressing the enter key'
print(len(intro)*'*')
print(f'{intro}')
print(len(intro)*'*') 
sentence = input(' ')

print(f'The word count for your sentence is {len(sentence.split())}')
