# Nome: Renan Cristyan A. Pinheiro
# Matrícula: 17/0044386
# Disciplina: Estruturas de Dados 2 - 2019/2
# Professor: Maurício Serrano

# Algorítmos de Ordenação O(n*log(n))

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

# Implementação recursiva do merge sort
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

x = [6, 5, 3, 1, 8, 7, 2, 4]
print(merge_sort(x))
