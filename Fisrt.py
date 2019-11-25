def sum(a,b):
    result = a + b
    return result

for i in range(1,3):
    print("%d : Hi? :)" %i)

jsonData = {1 : 'moon', 2 : 'sangwon', 3 : 'dahan'}
for i,v in jsonData.items():
    print(i, '번 단어는',v,' 입니다!')


arr = [5,15,23,5,6,9]
for i in arr :
    print('데이터:',i)
    if i == 15 :
        print(i,'를 찾았습니다.')
        break;
    else :
        print('fuck!')