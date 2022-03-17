#13.텍스트 파일의 읽기와 쓰기
#파일내의 정보가 휘발되지않도록 외부에 저장할 필요가 있다
#그러므로 우리는 외부의 파일을 읽고 쓰기위해 텍스트로 연습해볼 필요가 있다.
#w->쓰기모드:새로운 파일을 생성하기위해 사용. 동일한 파일이 있을 경우, 그파일은 삭제되고 새파일이 생성됨
#r->읽기모드:기존의 파일에 쓰지않고 오직 읽기만 함
#a->추가하기모드:파일 끝에 새로운 데이터를 추가할떄 사용된다.
#이미 생성된 파일의 일부를 변경하기를 원한다면 csv파일이나 sql데이터베이스를 이용하는것이 더 좋다.

file = open("Countries.txt","w")#다음 이름의 파일을 생성, 있을경우 빈파일로 덮어씌움
file.write("Italy\n")#\n은 강제 개행을 시킴 
file.write("Germany\n")
file.write("Spain\n")
file.close()#파일의 닫아 텍스트 파일에 저장되도록 한다.

file = open("Countries.txt","r")#해당파일을 읽기모드로 열고 파일 전체를 출력한다
print(file.read())

file = open("Countries.txt","a")#파일을 추가하기로 열고 한줄을 추가한 뒤 닫음
file.write("France\n")
file.close

file = open("Countries.txt","r")#해당파일을 읽기모드로 열고 파일 전체를 출력한다
print(file.read())



