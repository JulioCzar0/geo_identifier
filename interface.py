#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import os
import random
from PyQt4.QtGui import *
from PyQt4.QtCore import * 
#Ventana para envío de mensajes
prompt = QWidget() 
path = QInputDialog.getText(prompt, "Primero lo primero", "Ingrese el path su directorio actual")


#Se debe cambiar la ruta del computador
os.chdir(path[0])

#Se define el texto de las ventanas del programa
window_title = 'Identificador goegrafico'
start_message = "Baia...baia estas perdido. Te gustaria saber donde estas?"


#Lista que almacena preguntas generales
general_questions = []
general_questions_options = ["Aceras", "Calles", "Edificios", "Parqueos", "Otros", "Zona Verde"]

#Lista que almacena las preguntas especificas por capa
specific_questions = []


with open('preguntas_generales.csv', 'rb') as file:
    reader = csv.reader(file)
    general_questions = map(tuple, reader)
    
with open('/home/carlos/Desktop/preguntas_especificas.csv', 'rb') as file:
    reader = csv.reader(file)
    specific_questions = map(tuple, reader)    





def ask_general_question():    
    question = general_questions.pop(random.randrange(0,(len(general_questions))))
    
    #Selecciona el tipo de InputDialog dependiendo del tipo de pregunta
    if question[0] == 'Selection':
        answer = QInputDialog.getItem(prompt, question[1], question[2],  general_questions_options, 0, False)    
    return answer

def ask_specific_question():
    question = specific_questions.pop(random.randrange(0,(len(specific_questions))))
        
    if question[1] == 'Yes/No':
        answer = QMessageBox.question(prompt, question[2], question[3], QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if question[1] == 'Number':
        answer = QInputDialog.getInt(prompt, question[2], question[3],0)
    return answer    

#---------- Inicio de ejecución del programa ----------

#Se pregunta al usuario si desea continuar
user_answer = QMessageBox.question(prompt, window_title, start_message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

continue_execution = False
if user_answer == QMessageBox.Yes:
    continue_execution = True


while continue_execution:    
    #Escoge una pregunta del pool de preguntas generales
    if general_questions: 
        user_answer = ask_general_question()
        continue_execution = user_answer[1]
    elif specific_questions:
        user_answer = ask_specific_question()
    else:
        continue_execution = False
            
print "Baia baia"
    
    

    
