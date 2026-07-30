import geopandas as gpd
from qgis.core import QgsProject, QgsVectorLayer


# Прямая ссылка на архив с тем самым датасетом naturalearth_lowres
url = "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"

# GeoPandas скачает, распакует и прочитает его "на лету"
gdf = gpd.read_file(url)

print(gdf.head())

# Передаем GeoDataFrame в QGIS через встроенный формат GeoJSON
layer = QgsVectorLayer(gdf.to_json(), "Страны мира (GeoPandas)", "ogr")

# Добавляем полученный слой на карту QGIS
QgsProject.instance().addMapLayer(layer)

# Добавь эту строчку в свой файл '1загрузка данных.py'
output_path = "/home/nvmaxim/Projects/dev-sandbox/api_geoservice/qgis_practice/countries.gpkg"

gdf.to_file(output_path, driver="GPKG")
print("Файл успешно сохранен!")