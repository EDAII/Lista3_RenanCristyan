# Nome: Renan Cristyan A. Pinheiro
# Matrícula: 17/0044386
# Disciplina: Estruturas de Dados 2 - 2019/2
# Professor: Maurício Serrano

# Algorítmos de Ordenação O(n*log(n))

from random import randint
from mediana_linear import *

# O principal gargalo de desempenho é criar uma lista de valores aleatórios não repetidos
# Por enquanto a mediana linear só funciona com valores não repetidos

# Função que recebe dois vetores a e b, realiza o merge (mesclagem)
#  e retorna um vetor m
def merge(a,b):
    i, j = 0, 0 # Variáveis que percorrem os vetores a e b, respectivamente
    tam_a, tam_b = len(a), len(b) # Variáveis que guardam os tamanhos dos vetores a e b
    m = [] # Vetor (ou lista) que será retornado no final

    out = 0 # Variável auxiliar para sair do loop principal
    while True:
        if i == tam_a: # Se o contador i chegou no fim do vetor a
                       #  copia todo o vetor b
            while j < tam_b:
                m.append(b[j])
                j += 1
            out = 1
            break

        elif j == tam_b: # Se o contador j chegou no fim do vetor b
                         #  copia todo o vetor a
            while i < tam_a:
                m.append(a[i])
                i += 1
            out = 1
            break

        if out == 1: # Se um dos vetores já foi todo percorrido, 
                     #  copia o restante do outro e termina
            break

        if a[i] < b[j]:    # Se o valor atual do vetor a for menor que o valor atual do vetor b,
                           #  copia esse valor para o vetor m
            m.append(a[i])
            i += 1
            continue
        elif a[i] >= b[j]: # Se não, copia o valor atual do vetor b para o vetor m
            m.append(b[j])
            j += 1
            continue

    return m

# Implementação recursiva do Merge Sort
def merge_sort(vetor):
    if len(vetor) == 1: # Se o tamanho do vetor for 1, retorna ele mesmo
        return vetor

    s = len(vetor) # Variável que guarda o tamanho do vetor
    l = vetor[:s//2]   # "lado esquerdo" do vetor 
    r = vetor[(s//2):] # "lado direito" do vetor

    # Chama recursivamente para a esquerda e para a direita
    a = merge_sort(l)
    b = merge_sort(r)
    
    if a != None and b != None:
        return merge(a,b) # Se os vetores a e b tiverem tamanho diferentes de 1
                          #  chama a função merge()

# Como o nome da função abaixo sugere, esta não é a implementação original do Quick Sort.
# Estava tendo problemas com a recursividade, os valores estavam incorretos, então
#  resolvi tentar uma abordagem diferente para retornar os valores corretos

# O funcionamento do algorítmo é o seguinte:
#  Ele começa parecido com o Quick Sort original, escolhendo um pivô (agora o pivô é a mediana do vetor calculada em tempo linear)
#  e separando os valores menores que o pivô para a esquerda e os maiores para direita, garantindo que o pivô
#  já está na posição correta. Porém, após particionar o vetor entre esquerda e direita, o algoritmo insere
#  o pivô em um vetor auxiliar 'bvec' e chama o Insertion Sort para garantir que a cada inserção o vetor 
#  bvec já estará ordenado. Então o algoritmo se chama recursivamente para a esquerda e para a direita passando como
#  parâmetros o vetor atual e bvec, repetindo o raciocínio até que o tamanho de bvec seja igual ao tamanho do vetor
#  original

# Escolhi o Insertion Sort como algorítmo auxliar porque ele tem um desempenho muito bom com vetores quase ordenados,
#  sendo linear nesse caso, dessa forma não afeta drasticamente o desempenho do algorítmo principal

# A desvantagem desse algorítmo é que ele consome mais memória já que cria um vetor auxiliar.
# Isso pode ser problemático se o vetor a ser ordenado for muito grande

def quick_insertion_sort(vetor, bvec=[]): # Na primeira chamada bvec não pode ser alterado ou o algorítmo não funcionará corretamente
    left = 0
    right = len(vetor) - 1

    p = mediana_real(vetor, len(vetor)//2)
    pivo = busca_sequencial(vetor, p)

    if len(vetor) == 1:
        bvec.append(vetor[0])
        insertion_sort(bvec)
        return vetor

    swap(vetor, pivo, right)
    pivo = right
    right -= 1

    while(True):
        if vetor[left] == vetor[right] and left == 0:
            if vetor[pivo] < vetor[left]:
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

    L, R = my_partition(vetor, pivo)
    bvec.append(vetor[pivo])
    insertion_sort(bvec)

    if len(L) != 0:
        quick_insertion_sort(L, bvec)
    if len(R) != 0:
        quick_insertion_sort(R, bvec)

    if len(bvec) == len(vetor):
        return bvec

# As duas funções abaixo foram extraídas de https://wiki.python.org.br/QuickSort

# Função auxiliar de sort()
def partition(array, begin, end, cmp):
    while begin < end:
         while begin < end:
            if cmp(array[begin], array[end]):
                (array[begin], array[end]) = (array[end], array[begin])
                break
            end -= 1
         while begin < end:
            if cmp(array[begin], array[end]):
                (array[begin], array[end]) = (array[end], array[begin])
                break
            begin += 1
    return begin

# Implementação do Quick sort
def sort(array, cmp=lambda x, y: x > y, begin=None, end=None):
    if begin is None: begin = 0
    if end   is None: end   = len(array)
    if begin < end:
        i = partition(array, begin, end-1, cmp)
        sort(array, cmp, begin, i)
        sort(array, cmp, i+1, end)
