#비밀번호 생성기 제작 프로젝트
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("비밀번호 생성기 프로그램에 오신걸 환영합니다!")
nr_letters= int(input("몇개의 문자를 비밀번호에 사용하시겠습니까?\n"))
nr_symbols = int(input(f"몇개의 심볼을 사용하시겠습니까?\n"))
nr_numbers = int(input(f"몇개의 숫자를 사용하시겠습니까?\n"))

#Eazy Level - 출력 예시는:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass1 = "" #빈문자열 초기화
#char 를 1부터 입력받은 횟수 까지 반복
for char in range(1, nr_letters+1):
    #빈문자열에 랜덤함수의 초이스를 이용하여 문자열 에서 하나 랜덤으로 입력 및 반복
    pass1 += random.choice(letters)
for char in range(1, nr_symbols+1):
    #위의 문자열에 랜덤함수에 초이스를 이용하여 심볼에서 하나 랜덤으로 입력 및 반복
    pass1 += random.choice(symbols)
for char in range(1, nr_numbers+1):
    pass1 += random.choice(numbers)
#print(f"당신의 비밀번호는 : {pass1}")
callsign1 = "" #빈 문자열 선언 : 랜덤으로 추출된 문자열을 넣어줘서 깔끔하게 출력하기 위함
#i를 pass1 에 저장된 문자를 하니싹 입력
#i는 아이템 : 증가할 값 pass1 ; iterable 반복가능한 객체를 의미함
for i in pass1:
    callsign1 += i
#함수만을 사용하여 출력시 문자열이 합쳐지지 않은채로 나옴
password1 =random.sample(letters,nr_letters) + random.sample(symbols,nr_symbols) + random.sample(numbers,nr_numbers)
print(f"당신의 비밀번호는 : {password1}")
print(f"당신의 비밀번호는 : {callsign1}")

#Hard Level
pass_list2 = [] #리스트로 선언
for char in range(1, nr_letters+1):
    #리스트에 추가 += 써도 append를 사용하여도 무방함
    pass_list2.append(random.choice(letters))
for char in range(1, nr_symbols+1):
    pass_list2.append(random.choice(symbols))
for char in range(1, nr_numbers+1):
    pass_list2.append(random.choice(numbers))
#랜덤의 셔플함수는 랜덤으로 값을 섞어줌
random.shuffle(pass_list2)
print(f"당신의 비밀번호 (어려운버전) 은 : {pass_list2}")
#랜덤의 샘플은 중복을 허용하지 않고 랜덤으로 값을 추출
password2 = random.sample(letters,nr_letters) + random.sample(symbols,nr_symbols) + random.sample(numbers,nr_numbers)
random.shuffle(password2)
#print(f"당신의 비밀번호 (어려운버전) 은: {password2}")


callsign1 = ""
for i in pass_list2:
    callsign1 += i
print(f"문자열로 출력한다면 : {callsign1} 입니다.")
#^^ 위의 코드는 리스트로 출력이 된다면 가독성이 불편하기에 가독성을 위하여 빈 문자열을 선언후 i 변수에 pass_list2 리스트(iterable)의 값을 반복하며
#하나하나씩 주입함 A ,B ,C ,D  가 있다면 ABCD로 주입이 되게 됨