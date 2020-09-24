from collections import Counter

phones = ['iphone', 'samsung', 'lg', 'iphone', 'lg']

count = Counter(phones)
print(count['lg'])

text = 'Ехал грека через реку'\
    .lower().replace(' ', "")
count = Counter(text)
print(count)