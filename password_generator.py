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
pass1 = ""
for char in range(1, nr_letters+1):
    pass1 += random.choice(letters)
for char in range(1, nr_symbols+1):
    pass1 += random.choice(symbols)
for char in range(1, nr_numbers+1):
    pass1 += random.choice(numbers)
print(f"당신의 비밀번호는 : {pass1}")
callsign1 = ""
for i in pass1:
    callsign1 += i
password1 =random.sample(letters,nr_letters) + random.sample(symbols,nr_symbols) + random.sample(numbers,nr_numbers)
print(f"당신의 비밀번호는 : {password1}")
print(f"당신의 비밀번호는 : {callsign1}")

#Hard Level
pass_list2 = []
for char in range(1, nr_letters+1):
    pass_list2.append(random.choice(letters))
for char in range(1, nr_symbols+1):
    pass_list2.append(random.choice(symbols))
for char in range(1, nr_numbers+1):
    pass_list2.append(random.choice(numbers))
random.shuffle(pass_list2)
print(f"당신의 비밀번호 (어려운버전) 은 : {pass_list2}")

password2 = random.sample(letters,nr_letters) + random.sample(symbols,nr_symbols) + random.sample(numbers,nr_numbers)
random.shuffle(password2)
print(f"당신의 비밀번호 (어려운버전) 은: {password2}")

callsign1 = ""
for i in pass_list2:
    callsign1 += i
print(f"문자열로 출력한다면 : {callsign1} 입니다.")