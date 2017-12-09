example_str = '''
\n\n이상한 띄워쓰기 \t\t                      읽기
힘들지요 \t\n\t\t
'''

cleaned_str_list = " ".join(example_str.split())

print(cleaned_str_list)
