import pandas as pd
import numpy as np
import re


def read(x):
    ''' Con esta función, podremos importar archivos csv y crear DataFrames'''
    return pd.read_csv(x , encoding = 'latin1')


def espacios(x) :
    ''' Quitará los espacios iniciales y finales de un string'''
    return x.strip()


def pais(x):
    ''' utilizamos esta funcion para cambiar el nombre del pais'''
    if x == "Kingdom":
        return 'United Kingdom'
    else:
        return x


#lam = lambda x : 'United Kingdom' if x == 'Kingdom' else x

def mes(x):
    ''' Funcion para sacar el mes en str'''
    arr_year = (["None","01Enero","02Febrero", "03Marzo","04Abril","05Mayo","06Junio",
    "07Julio", "08Agosto","09Septiembre","10Octubre", "11Noviembre", "12Diciembre"])
    return arr_year[int(x)]



airconditionair = ["(.*)?air(.*)?", "(.*)?condition(.*)?"]
utilities = ["(.*)?pool(.*)?", "(.*)?gym(.*)?", "(.*)?spa(.*)?" ,
             "(.*)?elevat(.*)?" , "(.*)?stair(.*)?" , "(.*)?lift(.*)?" ,
             "(.*)?stairs(.*)?"]
eldery = ["(.*)?building(.*)?" , "(.*)?renovat(.*)?" ,
          "(.*)?eldery(.*)?" , "(.*)?old(.*)?"]
suciedad = ["(.*)?clean(.*)?" , "(.*)?dirty(.*)?"]
comidas = ["(.*)?lunch(.*)?" , "(.*)?breakf(.*)?" , "(.*)?dinner(.*)?"]
rooms = ["(.*)?roo(.*)?", "(.*)?windo(.*)?" , "(.*)?phon(.*)?",
        "(.*)?bed(.*)?" , "(.*)?sheet(.*)?"]
positive = ["(.*)?no negative(.*)?" , "(.*)?excellent(.*)?"]

def neg(x):
    '''
    Con esta funcion vamos a poder agrupar los comentarios negativos segun lo que ponga en la columna
    '''
    aire = 'Aire Acondicionado'
    utility = 'Utilities'
    eldery2 = 'Antiguedad'
    sucio = 'Suciedad'
    comida = 'Comidas'
    room = 'Habitaciones'
    positive = 'Comentario positivo'
    x = x.lower()
    for a in airconditionair:
        if re.search (a,x):
            x = aire
            return x
    for u in utilities :
        if re.search (u,x):
            x = utility
            return x
    for e in eldery:
        if re.search (e,x):
            x = eldery2
            return x
    for s in suciedad:
        if re.search (s,x):
            x = sucio
            return x
    for r in rooms:
        if re.search (r,x):
            x = room
            return x
    for c in comidas:
        if re.search (c,x):
            x = comida
            return x
    for p in positive:
        if re.search (p,x):
            x = positive
            return x
    return "Other"


def top10():
    ''' Sacamos con esta funcion los 10 paises que peores notas ponen en España'''
    hotel_esp= op.read('output/hotel_esp.csv')
    hotel_esp2 =hotel_esp.groupby("Reviewer_Nationality").agg({
    "Reviewer_Score":"mean"})
    hotel_esp2 = hotel_esp2.sort_values(['Reviewer_Score'], ascending = True).head(10)
    return hotel_esp2.plot.barh();

def top10():
    hotel_esp = op.read('output/hotel_esp.csv')
    hotel_esp2 =hotel_esp.groupby("Reviewer_Nationality").agg({"Reviewer_Score":"mean"})
    hotel_esp2 = hotel_esp2.sort_values(['Reviewer_Score'], ascending = True).head(10)
    return hotel_esp2.plot.barh();
