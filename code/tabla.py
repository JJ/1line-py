#!/usr/bin/env python

"""Define una tabla y filtra por algún valor"""
cabecera = ["Lugar","Tipo","Asistencia"]
tabla=[cabecera]
tabla.append( ["La Nave","Taller",10] )
tabla.append( ["Universidad", "Mesa redonda", 70])
solo_tabla = tabla[1:]
suma=0
for fila in solo_tabla:
    suma=suma+fila[2]
print(suma)
