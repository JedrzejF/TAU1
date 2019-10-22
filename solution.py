test = open('test-A/in.tsv', 'r', encoding='utf-8')
dev = open('dev-0/in.tsv', 'r', encoding='utf-8')

dictionary = []
with open('basic dictionary.txt') as dict:
    for x in dict.readlines():
        x = x.replace("\n","")
        dictionary.append(x.split(';'))

with open('test-A/out.tsv', 'w', encoding='utf-8') as out_test:
    for x in test.readlines():
        x = x.lower()
        for b, a in dictionary:
            x = x.replace(a, b)
        out_test.write(x)

with open('dev-0/out.tsv', 'w', encoding='utf-8') as out_dev:
    for x in test.readlines():
        x = x.lower()
        for b, a in dictionary:
            x = x.replace(a, b)
        out_dev.write(x)