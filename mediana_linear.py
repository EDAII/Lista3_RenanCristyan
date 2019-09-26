# Cálculo da mediana real de um vetor em tempo linear

from copy import copy
from random import randint
from time import time

def swap(vetor, a, b):
    aux = vetor[a]
    vetor[a] = vetor[b]
    vetor[b] = aux

def insertion_sort(vetor):
    tam = len(vetor)
    i, j = 0, 0

    while i < tam:
        j = i

        while (j != 0) and vetor[j] < vetor[j-1]:
            swap(vetor, j, j-1)
            j -= 1
        
        i += 1

# Retorna uma vetor aleatório
# Um vetor sem valores repetidos demora muito mais para ser criado
def random_list(size, max_value=None, repeat=True):
	if max_value == None or max_value < size:
		max_value = 10*size

	lista = []

	i = 0
	while i < size:
		num = randint(0,max_value)
		
		if repeat:
			lista.append(num)
		else:
			if num not in lista:
				lista.append(num)
			
		i += 1

	return lista

# Divide um vetor em 2 e exclui pos_pivo
def partition(vetor, pos_pivo):
    
    left = vetor[:pos_pivo]
    right = vetor[pos_pivo+1:]

    return left, right

def busca_sequencial(vetor, elemento):
	n = 0
	while n < len(vetor):
		if vetor[n] == elemento:
			return n
		n += 1

	return None

# Os valores menores que o pivô vão para a esquerda, e os maiores vão para a direita
# Quase um quick sort só que de uma iteração
def almost_quick_sort(vetor, pivo=None):
	left = 0
	right = len(vetor) - 1

	swap(vetor, pivo, right)
	pivo = right
	right -= 1

	while(True):
		if vetor[left] == vetor[right] and left == 0:
			swap(vetor, pivo, left)
			pivo = left
			break

		if vetor[left] > vetor[right] and left == len(vetor)-1:
			break

		if vetor[left] < vetor[pivo]:
			left += 1
		
		if vetor[right] > vetor[pivo]:
			right -= 1

		if(vetor[left] > vetor[pivo] and vetor[right] < vetor[pivo]):
			if(left > right):
				swap(vetor, pivo, left)
				pivo = left
				break
			swap(vetor, left, right)

	return vetor

def divide_em_grupos(vetor):
	n, i = 0, 0
	tam = len(vetor)

	todos_os_grupos = []
	grupo_de_5 = []
	aux = []

	while n <= tam:
		if n != 0 and n % 5 == 0:
			aux = copy(grupo_de_5)
			todos_os_grupos.append(aux)
			grupo_de_5.clear()
			i = 0

		if n == tam:
			if i == 0:
				break
			aux = copy(grupo_de_5)
			todos_os_grupos.append(aux)
			grupo_de_5.clear()
			break

		grupo_de_5.append(vetor[n])

		i += 1
		n += 1

	return todos_os_grupos

def mediana_do_grupo(grupo):
	insertion_sort(grupo)
	m = -1
	
	if len(grupo) == 1:
		m = grupo[0]

	elif len(grupo) == 2:
		m = grupo[0]

	elif len(grupo) == 3:
		m = grupo[1]
	
	elif len(grupo) == 4:
		m = grupo[1]

	elif len(grupo) == 5:
		m = grupo[2]

	return m

# Na verdade essa função calcula a mediana das medianas do vetor (mas pode não ser a mediana real)
#  mom apenas chama ela
def calcula_medianas(todos_os_grupos):
	resultados = []
	aux, aux2 = [], []

	i = 0
	while i < len(todos_os_grupos):
		resultados.append(mediana_do_grupo(todos_os_grupos[i]))
		i += 1

	if len(resultados) > 5:
		rec = calcula_medianas(divide_em_grupos(resultados))
		return rec
	else:
		m = mediana_do_grupo(resultados)
		return m

def mom(vetor):
	aux = divide_em_grupos(vetor)
	mediana = calcula_medianas(aux)
	return mediana

def mediana_real(vetor, k):
	v = copy(vetor)

	m = mom(v)
	pos_m = busca_sequencial(v, m)
	almost_quick_sort(v, pos_m)
	pos_m = busca_sequencial(v, m)
	L, R = partition(v, pos_m)

	if len(L) == k:
		return m
	elif len(L) > k:
		return mediana_real(L, k)
	elif len(L) < k:
		return mediana_real(R, k-len(L)-1)

def teste_de_desempenho_da_mediana(size):
    w = random_list(size)

    print('Comparando o tempo de execução do cálculo da mediana em um vetor de', size, ' elementos\n')

    start = time()
    result = mediana_real(w, (len(w)//2))
    finish = time()

    print('mediana (linear) = ', result)
    print('calculada em ', finish - start, ' segundos.')

    print('-'*50)

    start = time()
    insertion_sort(w)
    finish = time()

    print('mediana (após ordenar o vetor com Insertion Sort) = ', w[len(w)//2])
    print('calculada em ', finish - start, ' segundos.')
