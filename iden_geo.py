# !/usr/bin/python
# -*- coding: latin-1 -*-
import os
import PyQt4
# Se debe cambiar la ruta y colocar la direcciÃ³n en donde se encuentran los archivos. Ejem: 'home\paradigmas\files'
os.chdir("/home/carlos/Desktop/")

#FunciÃ³n que carga y colorea las capas
def load_layer (path, name, data_source, color):
    #Se carga la capa al mapa
    layer = QgsVectorLayer(path, name, data_source)
    
    #Se le aplica el color a la capa
    symbol = layer.rendererV2().symbol()
    symbol.setColor(PyQt4.QtGui.QColor(color))
    
    # Se agrega la capa al mapa para manejarla y desplegarla en la GUI de QGGIS
    QgsMapLayerRegistry.instance().addMapLayer(layer)
    return layer

#FunciÃ³n que elimna todas las capas del mapa
def clear_all_layers():
    layers = iface.legendInterface().layers()    
    for layer in layers:
        QgsMapLayerRegistry.instance().removeMapLayer(layer.id())
    return 

#Función que selecciona elementos de una capa
#layer es una capa del mapa
#feature_attribute es una tupla, su primer valor es el atributo y el segundo es el valor buscado
#para crear una tupla nombre = (valor1, valor2)
def get_features(layer, feature_attribute):
    selection = []
    for feature in layer.getFeatures():
        value = feature.attribute(feature_attribute[0])
        if value == feature_attribute[1]:
           selection.append(feature)
    return selection

def get_features_array(features, feature_attribute):
    selection = [] 
    for feature in features:
        value = feature.attribute(feature_attribute[0])
        if value == feature_attribute[1]:
            selection.append(feature)
    return selection


def select_features(layer, features):
    selection = []
    for feature in features:
        selection.append(feature.id())
    layer.setSelectedFeatures(selection)
    return 
    

# Se carga la capa de PROPIEDADES_RodrigoFacio del mapa
fincas_layer = load_layer("Shapefiles_RodrigoFacio/PROPIEDADES_RodrigoFacio.shp", "Fincas", "ogr", "#58a9f0")

# Se carga la capa de ACERAS_RodrigoFacio del mapa
aceras_layer = load_layer("Shapefiles_RodrigoFacio/ACERAS_RodrigoFacio.shp", "Aceras", "ogr", "#906ee5")

# Se carga la capa de OTROS_RodrigoFacio del mapa
otros_layer = load_layer("Shapefiles_RodrigoFacio/OTROS_RodrigoFacio.shp", "Otros", "ogr", "#93c5f7")

# Se carga la capa EDIFICIOS_RodrigoFacio del mapa
edificios_layer = load_layer("Shapefiles_RodrigoFacio/EDIFICIOS_RodrigoFacio.shp", "Edificios", "ogr", "#b0f9c5")

# Se carga la capa de PARQUEOS_RodrigoFacio del mapa ------ tener en consideraciÃ³n la ruta del archivo
parqueos_layer = load_layer("Shapefiles_RodrigoFacio/PARQUEOS_RodrigoFacio.shp", "Parqueos", "ogr", "#78cdca")

# Se carga la capa de CALLES del mapa ------ tener en consideraciÃ³n la ruta del archivo
calles_layer = load_layer("Shapefiles_RodrigoFacio/CALLES_RodrigoFacio.shp", "Calles", "ogr", "#065ea1")




continue_execution = True

#while continue_execution:    
 #   response = PyQt4.QtGui.QInputDialog.getText(None, "Salir", "Presione ESC para salir.")
  #  continue_execution = response[1]

#Se eliminan todas las capas 
#clear_all_layers()
print "Bye bye!"
