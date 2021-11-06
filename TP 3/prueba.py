import random
import copy
import time

n_poblacion = 2000
n_sobreviven_cruzamiento = 100
probabilidad_sobrevivir_cruzamiento = 70
n_mutantes = 100
puntos_por_fallar = 0.5
puntos_castigo = 1

colores = ["roja", "verde", "negra", "amarilla", "azul"]
profesiones = ["matematico", "hacker",
               "analista", "desarrollador", "ingeniero"]
lenguajes = ["python", "java", "javascript", "c#", "c++"]
ide = ["vscode", "atom", "notepad++", "sublime", "vim"]
nosql = ["cassandra", "redis", "hadoop", "neo4j", "mongo"]

matrizProto = [colores, profesiones, lenguajes, ide, nosql]


class matriz:

    def __init__(self):
        self.matriz = [[0 for x in range(5)] for x in range(5)]
        self.puntos = 20
        self.restriccionesCumplidas = 0
        self.noCumplidas = []

    def getmatriz(self, x, y):
        return self.matriz[x][y]

    def llenarMatrizRandom(self):
        for x in range(0, 5):
            for y in range(0, 5):
                self.matriz[x][y] = random.sample(matrizProto[x], 1)[0]
                pass
            pass

    def mutar(self):
        variablesY = [0, 1, 2, 3, 4]
        x = random.randint(0, 4)
        y1 = random.choice(variablesY)
        variablesY.remove(y1)
        y2 = random.choice(variablesY)
        temp = self.matriz[x][y1]
        self.matriz[x][y1] = self.matriz[x][y2]
        self.matriz[x][y2] = temp

    def prueba(self):
        # El matemático vive en la casa roja
        try:
            i = self.matriz[1].index('matematico')
            if self.matriz[0][i] == 'roja':
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append("El matematico vive en la casa roja")
        except:
            self.puntos -= puntos_castigo

        # El hacker programa en python
        try:
            i = self.matriz[1].index('hacker')
            if self.matriz[2][i] == 'python':
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append("El hacker programa en python")
        except:
            self.puntos -= puntos_castigo

        # El que vive en la casa verde codea en vscode
        try:
            i = self.matriz[0].index('verde')
            if self.matriz[3][i] == 'vscode':
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append(
                    "El que vive en la casa verde codea en vscode")
        except:
            self.puntos -= puntos_castigo

        # El analista usa Atom
        try:
            i = self.matriz[1].index('analista')
            if self.matriz[3][i] == 'atom':
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append("El analista usa Atom")
        except:
            self.puntos -= puntos_castigo

        # El que vive en la casa verde está a la derecha del de la casa negra
        try:
            i = self.matriz[0].index('verde')
            if self.matriz[0][i-1] == 'negra' and i != 0:
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append(
                    "El que vive en la casa verde esta a la derecha del de la casa negra")
        except:
            self.puntos -= puntos_castigo

        # El que usa Redis codea en java
        try:
            i = self.matriz[4].index('redis')
            if self.matriz[2][i] == 'java':
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append("El que usa Redis codea en java")
        except:
            self.puntos -= puntos_castigo

        # El que usa Cassandra vive en la casa amarilla
        try:
            i = self.matriz[4].index('cassandra')
            if self.matriz[0][i] == 'amarilla':
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append(
                    "El que usa Cassandra vive en la casa amarilla")
        except:
            self.puntos -= puntos_castigo

        # El que usa notepad++ vive en la casa del medio
        try:
            if self.matriz[3][2] == 'notepad++':
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append(
                    "El que usa notepad++ vive en la casa del medio")
        except:
            self.puntos -= puntos_castigo

        # El desarrollador vive en la primera casa
        try:
            if self.matriz[1][0] == 'desarrollador':
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append(
                    "El desarrollador vive en la primera casa")
        except:
            self.puntos -= puntos_castigo

        # El que usa hadoop vive al lado del que codea javascript
        try:
            i = self.matriz[4].index('hadoop')
            if (self.matriz[2][i-1] == 'javascript' and i != 0) or (self.matriz[2][i+1] == 'javascript' and i != 4):
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append(
                    "El que usa hadoop vive al lado del de js")
        except:
            self.puntos -= puntos_castigo

        # El que programa en c# vive al lado del que usa cassandra
        try:
            i = self.matriz[2].index('c#')
            if (self.matriz[4][i+1] == 'cassandra' and i != 4) or (self.matriz[4][i-1] == 'cassandra' and i != 0):
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append(
                    "El que programa en c# vive al lado del que usa cassandra")
        except:
            self.puntos -= puntos_castigo

        # El que usa Neo4J usa sublime
        try:
            i = self.matriz[4].index('neo4j')
            if self.matriz[3][i] == 'sublime':
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append("El que usa Neo4J usa sublime")
        except:
            self.puntos -= puntos_castigo

        # El ingeniero usa mongo
        try:
            i = self.matriz[1].index('ingeniero')
            if self.matriz[4][i] == 'mongo':
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append("El ingeniero usa mongodb")
        except:
            self.puntos -= puntos_castigo

        # El desarrollador vive al lado del de la casa azul
        try:
            i = self.matriz[0].index('azul')
            if (self.matriz[1][i+1] == 'desarrollador' and i != 4) or (self.matriz[1][i-1] == 'desarrollador' and i != 0):
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append(
                    "El desarrollador vive al lado del de la casa azul")
        except:
            self.puntos -= puntos_castigo

        # El programador de c++ lo hace en vim
        try:
            i = self.matriz[2].index('c++')
            if self.matriz[3][i] == 'vim':
                self.puntos += 1
                self.restriccionesCumplidas += 1
            else:
                self.puntos -= puntos_por_fallar
                self.noCumplidas.append("El programador de c++ lo hace en vim")
        except:
            self.puntos -= puntos_castigo


class AcertijoEinstein:

    def __init__(self):
        self.poblacion = []

    def resolucion(self):
        self.generacion(n_poblacion)
        x = 0
        while True:
            x += 1
            print('Iteracion numero:  %d' % x)
            self.prueba()
            restriccionesCumplidas = self.poblacion[0].restriccionesCumplidas
            if restriccionesCumplidas >= 15:
                break
            self.cruzamiento(n_sobreviven_cruzamiento, n_poblacion)
            self.mutar()
            pass
        self.prueba()
        print(self.poblacion[0].matriz)
        print(self.poblacion[0].restriccionesCumplidas)

    def mutar(self):
        for x in range(0, n_mutantes):
            y = random.randint(0, len(self.poblacion)-1)
            self.poblacion[y].mutar()
            pass

    def generacion(self, i):
        for x in range(0, i):
            nuevo_individuo = matriz()
            nuevo_individuo.llenarMatrizRandom()
            self.poblacion.append(nuevo_individuo)
            pass

    def cruzamiento(self, i, limit):
        goodpoblacion = []
        i = 0
        while len(goodpoblacion) < n_sobreviven_cruzamiento:
            if random.randint(0, 100) < probabilidad_sobrevivir_cruzamiento:
                goodpoblacion.append(self.poblacion[i])
            i += 1
            i %= len(self.poblacion)
        nuevaGeneracion = []
        while len(nuevaGeneracion) <= limit:
            primero = goodpoblacion[random.randint(0, len(goodpoblacion)-1)]
            segundo = goodpoblacion[random.randint(0, len(goodpoblacion)-1)]
            tercero = goodpoblacion[random.randint(0, len(goodpoblacion)-1)]
            nuevo_individuo = self.cruza(primero, segundo, tercero)
            nuevaGeneracion.append(nuevo_individuo)
        self.poblacion = nuevaGeneracion

    def cruza(self, primero, segundo, tercero):
        nuevo_individuo = matriz()
        for x in range(0, 5):
            for y in range(0, 5):
                i = random.randint(0, 2)
                if i == 0:
                    nuevo_individuo.matriz[x][y] = primero.getmatriz(x, y)
                elif i == 1:
                    nuevo_individuo.matriz[x][y] = segundo.getmatriz(x, y)
                else:
                    nuevo_individuo.matriz[x][y] = tercero.getmatriz(x, y)
                pass
            pass
        return nuevo_individuo

    def prueba(self):
        for x in range(0, len(self.poblacion)):
            self.poblacion[x].prueba()
            pass
        self.poblacion.sort(key=lambda x: x.puntos, reverse=True)
        print(self.poblacion[0].restriccionesCumplidas)
        print(self.poblacion[0].matriz)
        print(self.poblacion[0].noCumplidas)


puz = AcertijoEinstein()
puz.resolucion()
