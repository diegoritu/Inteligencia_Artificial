'''
Condiciones
~~~~~~~~~~~
1. Hay 5 casas.
2. El Matematico vive en la casa roja.
3. El hacker programa en Python.
4. El Brackets es utilizado en la casa verde.
5. El analista usa Atom.
6. La casa verde esta a la derecha de la casa blanca.
7. La persona que usa Redis programa en Java
8. Cassandra es utilizado en la casa amarilla
9. Notepad++ es usado en la casa del medio.
10. El Desarrollador vive en la primer casa.
11. La persona que usa HBase vive al lado de la que programa en JavaScript.
12. La persona que usa Cassandra es vecina de la que programa en C#.
13. La persona que usa Neo4J usa Sublime Text.
14. El Ingeniero usa MongoDB.
15. EL desarrollador vive en la casa azul.

Quien usa vim?


Resumen:
Colores = Rojo, Azul, Verde, Blanco, Amarillo
Profesiones = Matematico, Hacker, Ingeniero, Analista, Desarrollador
Lenguaje = Python, C#, JAVA, C++, JavaScript
BD = Cassandra, MongoDB, Neo4j, Redis, HBase
editor = Brackets, Sublime Text, Atom, Notepad++, Vim
'''

import random
import time

from scipy.sparse import data


colors =      {'001' : 'red',          '010' : 'blue',          '011' : 'green',    '100' : 'white',    '101' : 'yellow'}
profession =  {'001' : 'Mathematician','010' : 'Hacker',        '011' : 'Engineer', '100' : 'Analyst',  '101' : 'Developer'}
languaje =    {'001' : 'Python',       '010' : 'C#',            '011' : 'Java',     '100' : 'C++',      '101' : 'JavaScript'}
database =    {'001' : 'Cassandra',    '010' : 'MongoDB',       '011' : 'HBase',    '100' : 'Neo4j',    '101' : 'Redis'}
editor =      {'001' : 'Brackets',     '010' : 'Sublime Text',  '011' : 'Vim',      '100' : 'Atom',     '101' : 'Notepad++'}

#Se agregan constantes que definen la posición de cada característica del individuo
COLOR = 0
PROFESION = 1
LENGUAJE = 2
BASEDEDATOS = 3
EDITORDETEXTO = 4

SIZE_POBLACION = 2000

class Phenotype:

    def __init__(self):
        # crear un individuo
        self.chromosome = self.crearInvididuos()
        #print(self.chromosome)
        self.score = 0
        self.score = self.fitness_function()

    #AGREGADO PARA EL PUNTO 1.
    def crearInvididuos(self):
            h = 5
            datosIndividuo = [[] for y in range(h)]

            individuos = []

            #Por cada característica
            for i in range(0,5):

                #Por cada individuo
                for j in range(0,5):
                    #Se selecciona un valor al azar.
                    randomValue = random.randint(0,4)

                    #INVESTIGAR QUE HACE ESTO         
                    while datosIndividuo[i].count(randomValue) > 0:
                        randomValue = random.randint(0,4)
                    #FIN INVESTIGAR QUE HACE ESTO


                    datosIndividuo[i].append(randomValue)

            #Se agregan los datos a la lista de individuos
            for i in range(0,5):
                for j in range(0,5):
                    if i==COLOR:
                        individuos.append(list(colors.keys())[datosIndividuo[j][i]])
                    elif i==PROFESION:
                        individuos.append(list(profession.keys())[datosIndividuo[j][i]])
                    elif i==LENGUAJE:
                        individuos.append(list(languaje.keys())[datosIndividuo[j][i]])
                    elif i==BASEDEDATOS:
                        individuos.append(list(database.keys())[datosIndividuo[j][i]])
                    else:
                        #i==EDITORDETEXTO
                        individuos.append(list(editor.keys())[datosIndividuo[j][i]])
                                
            return individuos
    #FIN AGREGADO PARA EL PUNTO 1

    def decode(self):
        ''' traduce 0's y 1's (conjunto de genes: 3) en valores segun un diccionario '''
        return [[colors[self.chromosome[i*5+0]], 
                 profession[self.chromosome[i*5+1]],
                 languaje[self.chromosome[i*5+2]],
                 database[self.chromosome[i*5+3]],
                 editor[self.chromosome[i*5+4]]] for i in range(5)]
        

    def encode(self):
        pass


    def mutate(self):
        ''' muta un fenotipo, optimizado'''
        print("programame")
        pass

    def fitness_function(self):
        ''' calcula el valor de fitness del cromosoma segun el problema en particular '''

        score = 0
        ok_score = 1
        fail_score = -1
        #punish_score = -1 
        
        chromosome = self.decode()
        #print("Datos del cromosoma:")
        #print(chromosome)

        #ARRANCA AGREGADO

        matrizKeyValues = [[0 for x in range(5)] for x in range(5)] 
                
        
        #Se llena matriz de key values para poder posteriormente ejecutar todas las condiciones del modelo.
        for i in range(0, 5):
            for j in range(0, 5):
                matrizKeyValues[i][j] = self.chromosome[j*5+i]
        
        #Se empiezan a evaluar la condiciones del modelo

        #Condición 2: El Matematico vive en la casa roja.
        #Se busca el individuo con profesión "Matemático"
        i = matrizKeyValues[PROFESION].index(list(profession.keys())[0])
        if matrizKeyValues[COLOR][i] == 0:
            #Si el color de la casa del matemático es rojo
            score += ok_score
        else:
            #Si no lo es, penaliza
            score += fail_score

        #Condición 3: El hacker programa en Python.
        #Se busca al individuo con profesión "Hacker"
        i = matrizKeyValues[PROFESION].index(list(profession.keys())[1])
        if matrizKeyValues[LENGUAJE][i] == 0:
            #Si el lenguaje de programación es Python
            score += ok_score
        else:
            #Si no lo es, penaliza
            score += fail_score
    
        # Condición 4: El Brackets es utilizado en la casa verde.
        #Se busca al individuo que utiliza el editor de texto "Brackets"
        i = matrizKeyValues[EDITORDETEXTO].index(list(editor.keys())[0])
        if matrizKeyValues[COLOR][i] == 2:
            #Si la casa es verde
            score += ok_score
        else:
            #Si no lo es, penaliza
            score += fail_score

        # Condición 5: El analista usa Atom.
        #Se busca al individuo que tiene la profesión "Analista"
        i = matrizKeyValues[PROFESION].index(list(profession.keys())[3])
        if matrizKeyValues[EDITORDETEXTO][i] == 3:
            #Si el editor de texto es atom
            score += ok_score
        else:
            #Si no lo es, penaliza
            score += fail_score
        
        #Condición 6: La casa verde esta a la derecha de la casa blanca.
        #Se busca al individuo que tiene la casa verde
        i = matrizKeyValues[COLOR].index(list(colors.keys())[3])
        if i != 0 and matrizKeyValues[COLOR][i-1] == 4:
            #Si hay una casa a la derecha, y la casa es blanco
            score += ok_score
        else:
            #Si no se cumple lo anterior, penaliza
            score += fail_score
    
        #Condición 7: La persona que usa Redis programa en Java
        #Se busca al individuo que usa Redis
        i = matrizKeyValues[BASEDEDATOS].index(list(database.keys())[4])
        if matrizKeyValues[LENGUAJE][i] == 2:
            #Si el individuo usa Java
            score += ok_score
        else:
            #De lo contrario, penaliza
            score += fail_score
        
        #Condición 8: Cassandra es utilizado en la casa amarilla
        #Se busca al individuo que usa Cassandra
        i = matrizKeyValues[BASEDEDATOS].index(list(database.keys())[0])
        if matrizKeyValues[COLOR][i] == 4:
            #Si la casa del individuo es amarilla
            score += ok_score
        else:
            #De lo contrario, penaliza
            score += fail_score
        
        #Condición 9: Notepad++ es usado en la casa del medio
        #Se busca a quien utiliza el editor Notepad++
        i = matrizKeyValues[EDITORDETEXTO].index(list(editor.keys())[4])
        if i == 2:
            #Si se usa en la casa 2 (la del medio)
            score += ok_score
        else:
            #De lo contrario, penaliza
            score += fail_score

        #Condición 10: El Desarrollador vive en la primer casa.
        #Si la profesión del individuo es desarrollador
        i = matrizKeyValues[PROFESION].index(list(profession.keys())[4])
        if i == 0:
            #Si vive en la primer casa
            score += ok_score
        else:
            #De lo contrario, penaliza
            score += fail_score

        #Condición 11: La persona que usa HBase vive al lado de la que programa en JavaScript.
        #Si el individuo usa HBase
        i = matrizKeyValues[BASEDEDATOS].index(list(database.keys())[2])
        if (i != 4 and matrizKeyValues[LENGUAJE][i+1] == 4) or (i != 0 and matrizKeyValues[LENGUAJE][i-1] == 4):
            #Si a su izquierda o a su derecha vive quien programa en Javascript
            score += ok_score
        else:
            #De lo contrario, penaliza
            score += fail_score

        #Condición 12: La persona que usa Cassandra es vecina de la que programa en C#.
        #Si el individuo usa Cassandra
        i = matrizKeyValues[BASEDEDATOS].index(list(database.keys())[0])
        if (i != 4 and matrizKeyValues[LENGUAJE][i+1] == 1) or (i != 0 and matrizKeyValues[LENGUAJE][i-1] == 1):
            #Si a su izquierda o derecha vive quien programa en C#
            score += ok_score
        else:
            #De lo contrario, penaliza
            score += fail_score
        
        #Condición 13: La persona que usa Neo4J usa Sublime Text.
        #Si el individuo usa Neo4J
        i = matrizKeyValues[BASEDEDATOS].index(list(database.keys())[3])
        if matrizKeyValues[EDITORDETEXTO][i] == 1:
            #Si el individuo usa el editor Sublime Text
            score += ok_score
        else:
            #De lo contrario, penaliza
            score += fail_score
    
        #Condición 14: El Ingeniero usa MongoDB.       
        #Si el individuo es ingeniero
        i = matrizKeyValues[PROFESION].index(list(profession.keys())[2])
        if matrizKeyValues[BASEDEDATOS][i] == 1:
            #Si el individuo usa MongoDB
            score += ok_score
        else:
            #De lo contrario, penaliza
            score += fail_score

        #Condición 15: El desarrollador vive en la casa azul.
        #Si el individuo tiene como profesión "Desarrollador"
        i = matrizKeyValues[PROFESION].index(list(profession.keys())[4])
        if matrizKeyValues[COLOR][i] == 1:
            #Si vive en la casa azul
            score += ok_score
        else:
            score += fail_score

        return score

class Riddle:

    def __init__(self):
        self.start_time = time.time()
        self.population = []


    '''
    proceso general
    '''
    def solve(self, n_population):
        
        self.generate(n_population)
        print(f"Población creada con {len(self.population)} individuos")

        ''' descomentame '''
        print(self.population[0].chromosome)
        print(self.population[0].decode())

        print("Inicio del proceso iterativo")
        fit, indi = self.iterar()

        print(f"Fin del proceso, mejor resultado \n - Fitness: {fit} \n - Individuo {indi.chromosome} \n - Individuo {indi.decode()}")
        

    def iterar(self):

        counter = 0
        break_condition = False

        crossover_prop = 0.80
        
        while not(break_condition):
            
            if counter % 100 == 0:
                print("--------------------------------")
                print(counter)
                print(self.population[0].decode())
            
            
            # seleccion
            for i, x in enumerate(self.population):                
                #Si cumple con todas las reglas
                if(x.score >= 14):
                    break_condition = True
                    return x
                pass

            
            # crossover
            for s in range(0, SIZE_POBLACION, 2):
                #print(s)
                #Mando a 2 de los hijos para el cruzamiento (SIN TERMINAR, SEGUIR DESDE ACÁ)
                hijo1, hijo2 = self.crossOver(self, self.population[s], self.population[s+1], limit)

                pass
            
           
            # mutate
            print("programame")
            pass

            # condicion de corte
            if counter > N2 :
                print("programame")
                pass
                break_condition = True


            #IMPORTANTE: SE AGREGA ESTA LÍNEA TEMPORALMENTE HASTA TERMINAR TODOS LOS MÉTODOS Y PASOS DE ARRIBA. SI NO, ES PROBABLE QUE SE FORME UN LOOP INFINITO
            #break_condition = True
            
            counter += 1
            
        return self.population[0].score, self.population[0]

    '''
    operacion: generar individuos y agregarlos a la poblacion
    '''
    def generate(self, i):
        for x in range(0,i):
            newbie = Phenotype()
            self.population.append(newbie)

    '''
    operacion: mutación. Cambiar la configuración fenotipica de un individuo
    '''
    def mutate(self, crossed, prob=0.5):
        print("programame")
        pass


    '''
    operacion: cruazamiento. Intercambio de razos fenotipicos entre individuos
    '''
    def crossOver(self, progenitor_1, progenitor_2, limit):
        print("programame")
        pass

start = time.time()

rid = Riddle()
rid.solve(n_population = SIZE_POBLACION)

end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Tiempo transcurrido {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))