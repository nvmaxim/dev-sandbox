from qgis.core import QgsProject, QgsMapLayerType, QgsWkbTypes

# Получаем текущий проект QGIS
project = QgsProject.instance()

print(f"Всего слоев в проекте: {len(project.mapLayers())}\n")

for layer_id, layer in project.mapLayers().items():
    # Проверяем, является ли слой векторным
    if layer.type() == QgsMapLayerType.VectorLayer:
        # QgsWkbTypes.displayString красиво переводит тип геометрии (Point, LineString, Polygon)
        geom_type = QgsWkbTypes.displayString(layer.wkbType())
        print(f"[Вектор] {layer.name()} | Геометрия: {geom_type}")
        
    # Проверяем, является ли слой растровым
    elif layer.type() == QgsMapLayerType.RasterLayer:
        print(f"[Растр]  {layer.name()} | Каналов: {layer.bandCount()}")
        
    else:
        print(f"[Другой] {layer.name()} | Тип слоя: {layer.type()}")