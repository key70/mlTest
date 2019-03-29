from sklearn import svm

xor_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

data = []
label = []

for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p,q])
    label.append(r)

# print(data)
# print(label)

clf = svm.SVC()
clf.fit(data, label)

r = clf.predict(data)

ok = 0
total = len(label)
for i in range(len(label)):
    answer = label[i]
    p = r[i]
    if answer == p:
      ok=ok+1

# ok = 0; total = 0
# for idx, answer in enumerate(label):
#     p = r[idx]
#     if p == answer:
#         ok += 1
#     total += 1

print('정답률:',ok/total)













