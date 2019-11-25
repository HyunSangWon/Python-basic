# key, value 구조 for 문
jsonData = {1 : 'moon', 2 : 'sangwon', 3 : 'dahan'}
for i,v in jsonData.items():
    print(i, '번 단어는',v,' 입니다!')
# key 만 출력
var_dict = {"a": 50, "b":30}
for i in var_dict:
    print('key ===> ',i)

# 범위 지정 for문 0부터 3까지
for i in range(0,4):
    print(i)

# 배열 for 문
var_list = [1, 3, 5, 7]
for i in var_list:
    print('result ==> ',i)

# for문과 if 같이 사용
arr = [5,15,23,5,6,9]
for i in arr :
    print('데이터:',i)
    if i == 15 :
        print(i,'를 찾았습니다.')
        break;
    else :
        print('fuck!')