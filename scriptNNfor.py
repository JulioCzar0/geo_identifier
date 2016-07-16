# !/usr/bin/python
# -*- coding: latin-1 -*-
indexP = QgsSpatialIndex()
for feat in parqueos_layer.getFeatures():
  indexP.insertFeature(feat)

indexO = QgsSpatialIndex()
for feat in otros_layer.getFeatures():
  indexO.insertFeature(feat)

indexC = QgsSpatialIndex()
for feat in calles_layer.getFeatures():
  indexC.insertFeature(feat)

indexA = QgsSpatialIndex()
for feat in aceras_layer.getFeatures():
  indexA.insertFeature(feat)

indexE = QgsSpatialIndex()
for feat in edificios_layer.getFeatures():
  indexE.insertFeature(feat)

indexF = QgsSpatialIndex()
for feat in fincas_layer.getFeatures():
  indexF.insertFeature(feat)

for id in range(0, 246):

  #if id != 242 :

    feature_id =id
    iterator = edificios_layer.getFeatures(QgsFeatureRequest().setFilterFid(feature_id))
    feature = next(iterator)
    attrs=feature.attributes()
    print id
    print attrs[4]
    geom = feature.geometry()
    #x = geom.asPolygon()
    #print x[0][1]
    #for campo in range (0, len(x[0])):
    #for campo in range (0, 2):
    #pt = QgsPoint(x[0][0])
    pt = geom.asPoint()

    nearestP = indexP.nearestNeighbor(pt, 2)
    print nearestP

    nearestO = indexO.nearestNeighbor(pt, 2)
    print nearestO

    nearestC = indexC.nearestNeighbor(pt, 2)
    print nearestC

    nearestA = indexA.nearestNeighbor(pt, 2)
    print nearestA

    nearestE = indexE.nearestNeighbor(pt, 2)
    print nearestE

    nearestF = indexF.nearestNeighbor(pt, 2)
    print nearestF