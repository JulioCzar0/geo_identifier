# !/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

# Se debe cambiar la ruta y colocar la dirección en donde se encuentran los archivos. Ejem: 'home\paradigmas\files'
os.chdir('C:\Users\JulioCzar\Documents\UCR\Paradigmas\Proyecto\geo_identifier')

# Se carga la capa de PROPIEDADES_RodrigoFacio del mapa ------ tener en consideración la ruta del archivo
property_layerFincas = QgsVectorLayer("Shapefiles_RodrigoFacio\PROPIEDADES_RodrigoFacio.shp", "Fincas", "ogr")
idFincas = property_layerFincas.id()
# Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
QgsMapLayerRegistry.instance().addMapLayer(property_layerFincas)

# Se carga la capa de ACERAS_RodrigoFacio del mapa ------ tener en consideración la ruta del archivo
property_layerAceras = QgsVectorLayer("Shapefiles_RodrigoFacio\ACERAS_RodrigoFacio.shp", "Aceras", "ogr")
idAceras = property_layerAceras.id()
# Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
QgsMapLayerRegistry.instance().addMapLayer(property_layerAceras)

# Se carga la capa de OTROS_RodrigoFacio del mapa ------ tener en consideración la ruta del archivo
property_layerOtros = QgsVectorLayer("Shapefiles_RodrigoFacio\OTROS_RodrigoFacio.shp", "Otros", "ogr")
idOtros = property_layerOtros.id()
# Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
QgsMapLayerRegistry.instance().addMapLayer(property_layerOtros)

# Se carga la capa EDIFICIOS_RodrigoFacio PROPIEDADES del mapa ------ tener en consideración la ruta del archivo
property_layerEdificios = QgsVectorLayer("Shapefiles_RodrigoFacio\EDIFICIOS_RodrigoFacio.shp", "Edificios", "ogr")
idEdificios = property_layerEdificios.id()
# Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
QgsMapLayerRegistry.instance().addMapLayer(property_layerEdificios)

# Se carga la capa de PARQUEOS_RodrigoFacio del mapa ------ tener en consideración la ruta del archivo
property_layerParqueos = QgsVectorLayer("Shapefiles_RodrigoFacio\PARQUEOS_RodrigoFacio.shp", "Parqueos", "ogr")
idParqueos = property_layerParqueos.id()
# Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
QgsMapLayerRegistry.instance().addMapLayer(property_layerParqueos)

# Se carga la capa de CALLES del mapa ------ tener en consideración la ruta del archivo
property_layerCalles = QgsVectorLayer("Shapefiles_RodrigoFacio\CALLES_RodrigoFacio.shp", "Calles", "ogr")
idCalles = property_layerCalles.id()
# Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
QgsMapLayerRegistry.instance().addMapLayer(property_layerCalles)

#caps = property_layerFincas.dataProvider().capabilities()
# Check if a particular capability is supported:
#caps & QgsVectorDataProvider.DeleteFeatures
# Print 2 if DeleteFeatures is supported

iter = property_layerParqueos.getFeatures()
'''
for feature in iter:
    # retrieve every feature with its geometry and attributes
    # fetch geometry
    geom = feature.geometry()
    if feature.id() != 1:
        res = property_layerParqueos.dataProvider().deleteFeatures([feature.id()])


# Se eliminan todas las capas 
QgsMapLayerRegistry.instance().removeMapLayer(idFincas)
QgsMapLayerRegistry.instance().removeMapLayer(idAceras)
QgsMapLayerRegistry.instance().removeMapLayer(idOtros)
QgsMapLayerRegistry.instance().removeMapLayer(idEdificios)
QgsMapLayerRegistry.instance().removeMapLayer(idParqueos)
QgsMapLayerRegistry.instance().removeMapLayer(idCalles)
'''