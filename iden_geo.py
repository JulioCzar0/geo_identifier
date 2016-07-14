# !/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import time

# Se debe cambiar la ruta y colocar la dirección en donde se encuentran los archivos. Ejem: 'home\paradigmas\files'
os.chdir('C:\Users\JulioCzar\Documents\UCR\Paradigmas\Proyecto\geo_identifier\Shapefiles_RodrigoFacio')

# Se carga la capa de PROPIEDADES_RodrigoFacio del mapa ------ tener en consideración la ruta del archivo
property_layer = QgsVectorLayer("..\Shapefiles_RodrigoFacio\PROPIEDADES_RodrigoFacio.shp", "Fincas", "ogr")
idFincas = property_layer.id()
# Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
QgsMapLayerRegistry.instance().addMapLayer(property_layer)

# Se carga la capa de ACERAS_RodrigoFacio del mapa ------ tener en consideración la ruta del archivo
property_layer = QgsVectorLayer("..\Shapefiles_RodrigoFacio\ACERAS_RodrigoFacio.shp", "Aceras", "ogr")
idAceras = property_layer.id()
# Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
QgsMapLayerRegistry.instance().addMapLayer(property_layer)

# Se carga la capa de OTROS_RodrigoFacio del mapa ------ tener en consideración la ruta del archivo
property_layer = QgsVectorLayer("..\Shapefiles_RodrigoFacio\OTROS_RodrigoFacio.shp", "Otros", "ogr")
idOtros = property_layer.id()
# Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
QgsMapLayerRegistry.instance().addMapLayer(property_layer)

# Se carga la capa EDIFICIOS_RodrigoFacio PROPIEDADES del mapa ------ tener en consideración la ruta del archivo
property_layer = QgsVectorLayer("..\Shapefiles_RodrigoFacio\EDIFICIOS_RodrigoFacio.shp", "Edificios", "ogr")
idEdificios = property_layer.id()
# Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
QgsMapLayerRegistry.instance().addMapLayer(property_layer)

# Se carga la capa de PARQUEOS_RodrigoFacio del mapa ------ tener en consideración la ruta del archivo
property_layer = QgsVectorLayer("..\Shapefiles_RodrigoFacio\PARQUEOS_RodrigoFacio.shp", "Parqueos", "ogr")
idParqueos = property_layer.id()
# Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
QgsMapLayerRegistry.instance().addMapLayer(property_layer)

# Se carga la capa de CALLES del mapa ------ tener en consideración la ruta del archivo
property_layer = QgsVectorLayer("..\Shapefiles_RodrigoFacio\CALLES_RodrigoFacio.shp", "Calles", "ogr")
idCalles = property_layer.id()
# Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
QgsMapLayerRegistry.instance().addMapLayer(property_layer)

time.sleep(5) # delays for 5 seconds


# Se eliminan todas las capas 
QgsMapLayerRegistry.instance().removeMapLayer(idFincas)
QgsMapLayerRegistry.instance().removeMapLayer(idAceras)
QgsMapLayerRegistry.instance().removeMapLayer(idOtros)
QgsMapLayerRegistry.instance().removeMapLayer(idEdificios)
QgsMapLayerRegistry.instance().removeMapLayer(idParqueos)
QgsMapLayerRegistry.instance().removeMapLayer(idCalles)
