#11. 숫자 배열(array)->오직 숫자를 저장하는데 사용, 배열에 저장된 데이터는 모두 동일한 타입이어야한다.
#i->정수(integer): 파이선2에서는 -32768에서 32767까지 3에서는 메모리가 허용하는 만큼의 무제한 정수, 바이트크기(2)
#ㅣ->롱(long): 파이썬2에서는 -2,147,483,648에서 2,247,483,647사이의 정수, 3에서는 메모리가 허용하는 만큼의 무제한 정수, 바이트 크기(4)
#f->부동소수점(float):약 -10^308에서 10^308까지 소수점 이하의 소수점을 포함한 최대 38개의 숫자를 허용하는 음수또는 양수값.
# ->바이트 크기(4)
#d->더블(double):-10^308에서 10^308사이의 숫자로, 소수점 이하의 자릿수를 허용, 바이트크기(8)
#배열을 생성할때 데이터타입을 정의해야함, 그리고 정의한 데이터타입은 프로그램 실행중 변경할 수 없다.

from array import * 
#파이썬이 배열 라이브러리를 사용할 수 있도록 프로그램의 첫번쨰줄에 위치해야한다.

nums= array('i',[45,235,455,567,678,788])
#array('i',[45,235,455,567,678,788]) 가능
print(nums)

for x in nums:
    print (x)
#각 항목을 하나씩 출력함.


newValue = int(input("enter number:"))
nums.append(newValue)#입력한 수를 하나씩 레이어에 추가.
print(newValue)

nums.reverse()
print("reverse:",nums)#배열의 순서를 바꾸어 출력

nums = sorted(nums) #오름차순으로 정렬
print("sort:",nums)

nums=nums.pop()#마지막 항목을 제거
print("pop:",nums)

newArray=array('i',[])#빈 어레이를 생성
more=int(input("How many items:"))
for y in range(0,more):
    newV=int(input("enter num:"))
    newArray.append(newV)
nums.extend(newArray) #nums의 배열과 newarray배열의 항목을 결합
print(nums)

getRid=int(input("enter item index:"))
nums.remove(getRid)
print(nums)

print(nums.count(45))



