#input() - pozwala wprowadzić dane użytkownikowi
#int() - zmienia tekst - ciąg na liczbę
#składnia: x = polecenie(polecenie2())
print("Podaj liczbę x: ")
x = int(input())
print("Podaj liczbę y: ")
y = int(input())
 
if(x > y):
	print("x is larger than y")
else:
	print("y is either smaller or equal to x")
