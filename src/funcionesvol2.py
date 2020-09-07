import pandas as pd
import numpy as np 
import src.funcionesclean as op
import matplotlib.pyplot as plt
import seaborn as sns


def notamedia_pais_meses():
    ''' Podras ver la nota media del pais que elijas por meses'''
    hotel2 = op.read('output/hotel_clean.csv')
    x = input('Introduce el pais : ')
    hotel = hotel2[(hotel2["Hotel_Country"]== x)]
    hotel =hotel.groupby("Month").agg({"Reviewer_Score":['mean']})
    hotel.plot(figsize=(20, 5))
    plt.xlabel('Meses del año')
    plt.ylabel('Nota media')
    plt.show()

def media_paismes():
    '''Funcion para sacar la media de un pais en un mes en concreto'''
    hotel = op.read('output/hotel_clean.csv')
    x = input('Introduce el pais : ')
    y = input('Introduce el mes: ')
    hotel = hotel[(hotel["Hotel_Country"]== x)]
    hotel = hotel[(hotel["Month"]== y)]
    hotel =hotel.groupby("Month").agg({"Reviewer_Score":['mean']})
    return display(hotel)

def reviewtop10 ():
    '''Funcion para los clientes que mas se han quejado de diferentes tipos de reviews especificas'''
    hotel_esp = op.read('output/hotel_esp.csv')
    x = input('Introduce el tipo de queja: ')
    hotel_esp = hotel_esp[(hotel_esp["Negative_Review2"]== x)]
    hotel_esp =hotel_esp.groupby("Reviewer_Nationality").agg({"Reviewer_Score":"count"})
    hotel_esp = hotel_esp.sort_values(['Reviewer_Score'], ascending = False).head(10)
    return display(hotel_esp)