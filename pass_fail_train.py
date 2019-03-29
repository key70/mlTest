#sunflower      경민이 노래

from sklearn import svm, metrics

data = [
    [20,100,'합격'],
    [18,3,'불합격'],
    [15,10,'불합격'],
    [18,80,'합격'],
    [20,100,'합격'],
    [18,0,'불합격'],
    [20,90,'합격'],
    [17,50,'불합격'],
    [19,90,'합격'],
    [14,50,'불합격']
]

#훈련데이터
train_set = data[:7]

#예측데이터
predic_set = data[7:]

# 70%만 학습에 참여시키고
# 30%를 갖고 예측하여
# 정답률을 계산하여 출력해 봅니다.

train_data = []
train_label = []

predic_data = []
predic_label = []

#훈련데이터로 부터 문제와 답을 각각 분리하기
for i in range(len(train_set)):
    row = train_set[i]
    days = row[0]
    hours = row[1]
    isPass = row[2]
    train_data.append([days,hours])
    train_label.append(isPass)

#예측을 위한 데이터를 문제와 답으로 분리
for i in range(len(predic_set)):
    row = predic_set[i]
    days = row[0]
    hours = row[1]
    isPass = row[2]
    predic_data.append([days,hours])
    predic_label.append(isPass)

clf = svm.SVC()
clf.fit(train_data, train_label)

r = clf.predict(predic_data)

print(r)
print(predic_label)

acc = metrics.accuracy_score(predic_label, r)
print(acc)




















