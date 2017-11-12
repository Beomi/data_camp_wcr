import re

example_str = '''
901211-1123111
621003-2115633
'''

pattern = re.compile('\d{6}-\d{7}')
result = pattern.findall(example_str)

print(result)
