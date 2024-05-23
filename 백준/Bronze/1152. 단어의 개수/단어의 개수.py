# 대소문자와 공백으로 이뤄진 문자열. 문자열에는 몇 개의 단어가 있는가?
# 리스트로 받고, 공백 카운트 +1 한 값 출력

sentence = list(input())
count = 1
for i in range(len(sentence)):
    if sentence[i] == ' ':
        count += 1
if sentence[0] == ' ':
        count -= 1
if sentence[-1] == ' ':
        count -= 1
print(count)