#12.2차원 리스트와 딕셔너리
# 파이썬에서는 배열에 숫자를 넣는 것으로 제한되어있다. 그리고 대부분은 2차원의 경우 리스트가 흔하므로 
# 2차원 리스트가 훨씬 더 일반적이다.
#2차원 리스트의 코드는
grades=[[14,23,54],[32,22,45],[23,32,33]]
#for i in grades:
#    for j in grades[i]:
#        print(grades[i][j])
#에러 TypeError: list indices must be integers or slices, not list -> 인덱싱은 정수나 슬라이딩 부호[:]로 하는 것
#표준 파이썬 컬럼 인덱스 번호를 사용하고싶지않을 경우 다음과 같이 딕셔너리로 사용
grade=[{"ma":14,"en":23,"fr":54},{"ma":32,"en":22,"fr":45},{"ma":23,"en":32,"fr":33}]
print(grade[0]["en"])