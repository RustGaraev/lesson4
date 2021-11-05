print('Калькулятор')

def summa(N):
	operation = 0
	string = ''
	for i in range(N):
		print('Введите операнд', i + 1, ':', end = ' ')
		x = float(input())
		operation += x
		if i < N - 1:
			string += str(x) + '+'
		else:
			string += str(x)
	print(string, '=', operation)

def difference(N):
	operation = float(input('Введите операнд 1: '))
	string = str(operation) + '-'
	
	for i in range(1, N):
		print('Введите операнд', i + 1, ':', end = ' ')
		x = float(input())
		operation -= x
		if i < N - 1:
			string += str(x) + '-'
		else:
			string += str(x)
	print(string, '=', operation)

def product(N):
	operation = 1
	string = ''
	for i in range(N):
		print('Введите операнд', i + 1, ':', end = ' ')
		x = float(input())
		operation *= x
		if i < N - 1:
			string += str(x) + '*'
		else:
			string += str(x)
	print(string, '=', operation)

def division(N):
	operation = float(input('Введите операнд 1: '))
	string = str(operation) + '/'
	
	for i in range(1, N):
		print('Введите операнд', i + 1, ':', end = ' ')
		x = float(input())
		operation /= x
		if i < N - 1:
			string += str(x) + '/'
		else:
			string += str(x)
	print(string, '=', operation)

print('Введите действие: \n1 - суммировать; \n2 - вычесть; \n3 - умножить; \n4 - разделить')
c = int(input())
N = int(input('Введите количество операндов: '))

if N > 0:
	if c == 1:
		summa(N)
	elif c == 2:
		difference(N)
	elif c == 3:
		product(N)
	elif c == 4:
		division(N)
	elif c == 5:
		print('Сказали же, что только 4 варианта!!!')
	else:
		print('Введено неверное действие!')	
else:
	print('Количество операндов может быть только больше нуля и целым!')

