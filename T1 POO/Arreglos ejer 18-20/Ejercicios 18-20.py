# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 00:21:33 2021

@author: maril
"""

class Arreglos:    
    def __init__(self):
        pass

#EJERCICIO 18
#ARREGLOS DE UNA DIMENSIÓN        
    def calificaciones(self):                  
        cal = []
        for i in range(10):
            NDato = int( input( "Dime el dato numero {}: ".format(i)))
            cal.append(NDato)
        print("Las calificaciones son: {}".format(cal))

#EJERCICIO 19
#ARREGLOS EN UNA DIMENSIÓN
    def vectores(self):            
        N = []
        B=[]
        A= []
        print(N)
        for j in range(0,20):
            num = int(input("Ingrese un número: "))
            N.append(num)
        for j in N:
            if j >= 0:
                B.append(j)
            else:
                A.append(j)
        print("Los números positivos son: {}".format(B))
        print("Los números negativos son: {}".format(A))

#EJERCICIO 20
#ARREGLOS EN DOS DIMENSIONES
    def datos(self):            
        NotList = []
        AlumList = []
        Alum = 30
        CNotas = 6
        PromExam = []

        for alumno in range(1, 31):
            """Lectura de los 30 alumnos."""
            alum_temporal = input('Nombre del alumno {}: '.format(alumno))
            AlumList.append(alum_temporal)
            for nota in range(1, 7):
                print('Escriba la calificación del alumno "{}" en el exámen "{}"'.format(alum_temporal, nota))
                """Lectura de las 6 calificaciones de los 30 alumnos."""
                NTemp = round(float(input('Nota #{}: '.format(nota))), 2)
                if nota == 1:
                    NotList.append([NTemp])
                else:
                    NotList[alumno-1].append(NTemp)
            print('')

        """Calculo promedio de calificaciones de cada uno de los exámenes."""
        for NumExam in range(6):
            SumNotas = 0
            for nota in NotList:
                SumNotas += nota[NumExam]
            Prom = round((SumNotas/Alum ), 2)
            print('Promedio de exámen {}: {}'.format(NumExam+1, Prom))

        """Cálculo del promedio de cada alumno."""
        print('')
        for num, alum in enumerate(AlumList):
            SNotas = sum(NotList[num])
            Prom = round((SNotas/CNotas), 2)
            print('{} su promedio es: {}'.format(alum, Prom))

        """Cálculo del tipo de exámen que tuvo mayor promedio de calificación."""
        PromMayor = 0
        for NumExam in range(6):
            SNotas = 0
            for nota in NotList:
                SNotas += nota[NumExam]
            promedio = round((SNotas/Alum ), 2)
            if PromMayor < promedio:
                PromMayor = promedio
            PromExam.append(promedio)
        print('')
        print('El exámen', PromExam.index(PromMayor)+1,'obtuvo el mayor promedio:', PromMayor)

class1= Arreglos()
class1.calificciones() 
class1.vectores()
class1.datos()
