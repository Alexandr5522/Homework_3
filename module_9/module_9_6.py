def all_variants(text):
    for l in range(len(text)):
        for j in range(len(text) - l):
            yield text[j:j + l + 1]

res = all_variants('ABC')
for i in res:
    print(i)

