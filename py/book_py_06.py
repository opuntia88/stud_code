#while루프
#조건을 충족할때까지 계속해서 반복하는 루프 -> 조건이 충족되지않으면 루프를 완전히 건너뛸수있다
#루프를 실행할 조건이 올바른지 확인!

total = 0
while total < 100: #100미만일 경우
    num =int(input("enter the number: ")) 
    total = total + num # #입력된 값을 총 더한 값
    print("the total is", total)
    #100이상의 경우에는 루프를 종료.

#비교연산자
#'==': ~와 같다. '!='~와 같지않다. '>=','<=','<','>'
#논리연산자
#and,or

