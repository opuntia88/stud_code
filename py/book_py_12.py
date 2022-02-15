#12.2차원 리스트와 딕셔너리
# 파이썬에서는 배열에 숫자를 넣는 것으로 제한되어있다. 그리고 대부분은 2차원의 경우 리스트가 흔하므로 
# 2차원 리스트가 훨씬 더 일반적이다.
#2차원 리스트의 코드는
grades=[[14,23,54],[32,22,45],[23,32,33]]
for i in grades:
    print(i)# 이렇게 하면 각 row에 해당되는 column이 출력됨
for i in grades[1]:#이렇게하면 row[1]에 해당되는 
    print(i)

#    for j in grades[i]:
#        print(grades[i][j])
#에러 TypeError: list indices must be integers or slices, not list -> 인덱싱은 정수나 슬라이딩 부호[:]로 하는 것

#표준 파이썬 컬럼 인덱스 번호를 사용하고싶지않을 경우 다음과 같이 딕셔너리로 사용 ->[{}]->리스트 내부에 각 요소를 딕셔너리화
grade=[{"ma":14,"en":23,"fr":54},{"ma":32,"en":22,"fr":45},{"ma":23,"en":32,"fr":33}]
print(grade[0]["en"])

#행의 인덱스도 추가가 가능하다.-> {{}} ->r과 c모두 딕셔너리화
grade={"susan":{"ma":14,"en":23,"fr":54},"peter":{"ma":32,"en":22,"fr":45},"jack":{"ma":23,"en":32,"fr":33}}
print(grade["susan"],["en"])

simple_array=[[2,5,8],[3,7,4],[1,6,9]]
print("simple_array",simple_array) #2차원어레이에있는 모든 데이터를 출력.
print("simple_array[1]",simple_array[1])
simple_array[1][2]=3
print("simple_array[1][2]",simple_array[1][2])

data_set={"a":{"x":54,"y":82,"z":91},"b":{"x":75,"y":29,"z":80}} #2차원 딕셔너리 생성
print(data_set["a"])# a행의 모든 열에 포함된 데이터를 출력.
print(data_set["a"]["z"])#b행의 z열에 포함되는 데이터를 출력
for i in data_set:
    print(data_set[i]["y"])#각 행에있는 y열의 데이터를 출력.
data_set["b"]["y"]=56
print(data_set)

clas={}#초반에 딕셔너리임을 정의해야 오류가 안생김
clas["jack"]={"math":45 ,"english":30}
print(clas)
for name in clas:
    print(("jack"),clas["jack"]["english"])#이름을 출력하고 english에 해당되는 값을 출력

del clas["jack"]["english"]#del을 사용해서 clas리스트의 jack의 english 열의 데이터를 삭제
print(clas)