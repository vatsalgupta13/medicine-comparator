import pandas as pd
data = pd.read_csv('medicine_information+description.csv',
                   encoding='unicode_escape', engine='python')
# print(data.head())
l = []
flagged = []
last = 0
temp = data['Generic(Salt) name'][0]
print(temp)
for i, j in enumerate(data['Generic(Salt) name']):
    j = j.split()[0]
    if j not in flagged:
        flagged.append(j)
        last = i
    k = last
    alternatives = []
    while (data['Generic(Salt) name'][k].split()[0] == j and k < len(data['Generic(Salt) name'])-1):
        if data['Medicine(Brand) name'][k] != data['Medicine(Brand) name'][i]:
            if data['Medicine(Brand) name'][k] not in alternatives:
                alternatives.append(data['Medicine(Brand) name'][k])
            m = ','.join(alternatives)
        k += 1
    l.append(m)
    if i % 1000 == 0:
        print(i)
    if i == 33219:
        break
while len(l) < len(data['Generic(Salt) name']):
    l.append([])
data.insert(2, column="Alternatives", value=l)
print(data.tail()['Medicine(Brand) name'], data.tail()['Alternatives'])
data.to_csv('file2.csv')