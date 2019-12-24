import random

choose = input('Какую программу вы хотите запустить?\nНажмите 1 если вы хотите запустить калькулятор\nНажмите 2 чтобы запустить игру "больше меньше"\nНажмите 3 чтобы запустить программу для вычисления случайных цифр\n')

first_symbol = ''
first_number = ''
second_number = ''

def calculator(first_symbol, first_number, second_number):
	print('Вы выбрали программу "Калькулятор"')

	first_symbol = input('Введите знак: ')
	first_number = input('Введите цифру: ')
	second_number = input('Введите вторую цифру: ')

	if first_symbol == "+":
		print(int(first_number) + int(second_number))

	elif first_symbol == "-":
		print(int(first_number) - int(second_number))

	elif first_symbol == "*":
		print(int(first_number) * int(second_number))

	elif first_symbol == "/":
		try:
			print(int(first_number) / int(second_number))
		except:
			print('На ноль делить невозможно')
	else:
		print('Вы ввели неправильный символ')

first_text = ''
second_text = ''

def upper_lower(first_text, second_text):
	first_text = input('Введите первое слово или цифру: ')
	second_text = input('Введите второе слово или цифру: ')

	if first_text >= second_text:
		print(first_text + ' больше')
	else:
		print(second_text + ' больше')

how_numbers = ''

def random_number(how_numbers):
	while how_numbers == '':
		how_numbers = input('Сколько рандомных чисел вам нужно?: ')
	for i in range(int(how_numbers)):
		print( random.randint(1, 100) )

if choose == "1":
	calculator(first_symbol, first_number, second_number)

if choose == "2":
	upper_lower(first_text, second_text)

if choose == "3":
	random_number(how_numbers)
