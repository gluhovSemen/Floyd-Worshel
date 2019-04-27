import numpy as np
import math

def show_graph(matrix):
    edge_list = []
    for vertex in matrix:
        for sub_vertex in vertex:
            if not(sub_vertex == 0) and not(sub_vertex == math.inf):
                edge_list.add()

def init_graph():
    adjacency_matrix = [[math.inf]]
    return adjacency_matrix



def add_vertex(adjacency_matrix):
    for item in adjacency_matrix:
        item.append(math.inf)
    new_line = [math.inf for i in range(len(adjacency_matrix[0]) - 1)] + [math.inf]
    adjacency_matrix.append(new_line)
    return adjacency_matrix




#Считаем, что граф неНАПРАВЛЕННЫЙ#
def add_edge(vertex1, vertex2, weight, matrix):
    matrix[vertex1][vertex2] = matrix[vertex2][vertex1] = weight




def fill_matrix(inp, size):
    
    matrix = init_graph()
    for i in range(size - 1):
        add_vertex(matrix)
        
    adges = inp.split(', ')
    for i in adges:
        num = ''
        j = len(i) - 1
        while j > 0:
            if i[j].isnumeric():
                num = i[j] + num
            else:
                break
            j -= 1
        #print('added adge ({}; {}), weight = {}'.format(int(i[3]) - 1, int(i[6]) - 1, int(num) ))
        matrix[int(i[3]) - 1][int(i[6]) -1] = matrix[int(i[6]) -1][int(i[3]) - 1] = int(num)
        
        
    return matrix


def floyd(matrix):
    next_v = [ [math.inf for i in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != math.inf: 
                next_v[i][j] = j
                next_v[j][i] = i
            
    d = matrix
    #print(d)
    n = len(matrix) 
    for k in range (0 , n):
        for i in range (0 , n):
            for j in range (0 , n):
               # print(' {} <> {}'.format( d[k][j], (d[k][i] + d[i][j]) ))
                #print(' {}; {} vs ({}; {}) + ({}; {}) '.format(k, j, k, i, i, j))
                if k != j and k != i and i != j:
                    if d[k][j] > d[k][i] + d[i][j]:

                        next_v[k][j] = i
                        next_v[j][k] = i
                    d[k][j] = d[j][k] = min(d[k][j], (d[k][i] + d[i][j]))
                
    return d, next_v
            


def getShortestPath(u, v, next_v, d):
    u -= 1
    v -= 1
    print('len = ', d[u][v])
    if d[u][v] == math.inf:
        print( "No path found")                 
    c = u
   
    while c != v:
        print (c, end = ' -> ')
        c = next_v[c][v]
    print (v)
    

def inp_func():
	print('Количество ребер :')
	n = int(input())

	print('Количество вершин :')
	v = int(input())


	print('ребра в формате:   w(v1,v5) = 12 - ребро из 1 вершины в 5 длинной 12 ')
	inp = ''
	for i in range(n):
		s = input()
		inp += s + ', '
		
		num = ''
		j = len(s) - 1
		while j > 0:
			if s[j].isnumeric():
				num = s[j] + num
			else:
				break
			j -= 1

		print('added adge ({}; {}), weight = {}'.format(int(s[3]) , int(s[6]) , int(num) ))


	print('Введите вершины, между которыми нужно найти расстояние: ( два числа через пробел)')
	x, y = [int(i) for i in input().split()]
	
	return v, inp[:-2], x, y 
	# FLOYD-WORSHEL
n, inp, x, y = inp_func()

print(inp)
#inp = 'w(v1,v3) = 16, w(v1,v5)=12, w(v1,v6)=6, w(v1,v8)=13, w(v2,v3)=18, w(v2,v4)=23, w(v2,v6)=17, w(v3,v5)=29, w(v3,v6)=31, w(v4,v6)=27, w(v4,v7)=3, w(v5,v6)=24, w(v6,v7)=2, w(v6,v8)=1' 
matrix = fill_matrix(inp, n)
print ('Матрица смежности : ')
for i in matrix:
    print (i)
print()


print('Матрица кратчайших путей')
dist, next_v = (floyd(matrix))
for i in dist:
    print(i)
print()


print('Расстояние между вершинами')
getShortestPath(x, y, next_v, dist)




