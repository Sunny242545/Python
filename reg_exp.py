import re

pattern1 = re.compile(r'\d{3}[.-]\d{3}[-.]\d{4}')
pattern2 = re.compile(r'[89]00[.-]\d{3}[-.]\d{4}')

with open('regex_data.txt' ,'r') as f:
    data = f.read()
    matched_data1 = pattern1.finditer(data)
    matched_data2 = pattern2.finditer(data)


    for match in matched_data1:
        print(match.group())

    for match in matched_data2:
        print(f'1-{match.group()}')
