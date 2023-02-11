
import pandas as pd

from sklearn import preprocessing

from sklearn.neighbors import KNeighborsClassifier

import numpy as np

import PySimpleGUI as sg
excel = pd.read_excel('Crop_recommendation.xlsx', header=0)
print(excel)
print(excel.shape)
le = preprocessing.LabelEncoder()
crop = le.fit_transform(list(excel["label"]))

NITROGEN = list(excel["N"])
PHOSPHORUS = list(excel["P"])
POTASSIUM = list(excel["K"])
TEMPERATURE = list(excel["temperature"])
HUMIDITY = list(excel["humidity"])
PH = list(excel["ph"])
RAINFALL = list(excel["rainfall"])

features = list(zip(NITROGEN, PHOSPHORUS, POTASSIUM,
                TEMPERATURE, HUMIDITY, PH, RAINFALL))
features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM,
                    TEMPERATURE, HUMIDITY, PH, RAINFALL])
features = features.transpose()
print(features.shape)
print(crop.shape)

model = KNeighborsClassifier(n_neighbors=4)
model.fit(features, crop)

nitrogen_content = 16
phosphorus_content = 27
potassium_content = 37
temperature_content = 22
humidity_content = 94
ph_content = 7.2
rainfall = 104
predict1 = np.array([nitrogen_content, phosphorus_content, potassium_content,
                    temperature_content, humidity_content, ph_content, rainfall], dtype=float)
print(predict1)
predict1 = predict1.reshape(1, -1)
print(predict1)
predict1 = model.predict(predict1)
print(predict1)
crop_name = str()
if predict1 == 0:
    crop_name = 'Apple(सेब)'
elif predict1 == 1:
    crop_name = 'Banana(केला)'
elif predict1 == 2:
    crop_name = 'Blackgram(काला चना)'
elif predict1 == 3:
    crop_name = 'Chickpea(काबुली चना)'
elif predict1 == 4:
    crop_name = 'Coconut(नारियल)'
elif predict1 == 5:
    crop_name = 'Coffee(कॉफ़ी)'
elif predict1 == 6:
    crop_name = 'Cotton(कपास)'
elif predict1 == 7:
    crop_name = 'Grapes(अंगूर)'
elif predict1 == 8:
    crop_name = 'Jute(जूट)'
elif predict1 == 9:
    crop_name = 'Kidneybeans(राज़में)'
elif predict1 == 10:
    crop_name = 'Lentil(मसूर की दाल)'
elif predict1 == 11:
    crop_name = 'Maize(मक्का)'
elif predict1 == 12:
    crop_name = 'Mango(आम)'
elif predict1 == 13:
    crop_name = 'Mothbeans(मोठबीन)'
elif predict1 == 14:
    crop_name = 'Mungbeans(मूंग)'
elif predict1 == 15:
    crop_name = 'Muskmelon(खरबूजा)'
elif predict1 == 16:
    crop_name = 'Orange(संतरा)'
elif predict1 == 17:
    crop_name = 'Papaya(पपीता)'
elif predict1 == 18:
    crop_name = 'Pigeonpeas(कबूतर के मटर)'
elif predict1 == 19:
    crop_name = 'Pomegranate(अनार)'
elif predict1 == 20:
    crop_name = 'Rice(चावल)'
elif predict1 == 21:
    crop_name = 'Watermelon(तरबूज)'

if int(humidity_content) >= 1 and int(humidity_content) <= 33:
    humidity_level = 'low humid'
elif int(humidity_content) >= 34 and int(humidity_content) <= 66:
    humidity_level = 'medium humid'
else:
    humidity_level = 'high humid'
if int(temperature_content) >= 0 and int(temperature_content) <= 6:
    temperature_level = 'cool'
elif int(temperature_content) >= 7 and int(temperature_content) <= 25:
    temperature_level = 'warm'
else:
    temperature_level = 'hot'
if int(rainfall) >= 1 and int(rainfall) <= 100:
    rainfall_level = 'less'
elif int(rainfall) >= 101 and int(rainfall) <= 200:
    rainfall_level = 'moderate'
elif int(rainfall) >= 201:
    rainfall_level = 'heavy rain'

if int(nitrogen_content) >= 1 and int(nitrogen_content) <= 50:
    nitrogen_level = 'less'
elif int(nitrogen_content) >= 51 and int(nitrogen_content) <= 100:
    nitrogen_level = 'not to less but also not to high'
elif int(nitrogen_content) >= 101:
    nitrogen_level = 'high'
if int(phosphorus_content) >= 1 and int(phosphorus_content) <= 50:
    phosphorus_level = 'less'
elif int(phosphorus_content) >= 51 and int(phosphorus_content) <= 100:
    phosphorus_level = 'not to less but also not to high'
elif int(phosphorus_content) >= 101:
    phosphorus_level = 'high'
if int(potassium_content) >= 1 and int(potassium_content) <= 50:
    potassium_level = 'less'
elif int(potassium_content) >= 51 and int(potassium_content) <= 100:
    potassium_level = 'not to less but also not to high'
elif int(potassium_content) >= 101:
    potassium_level = 'high'

if float(ph_content) >= 0 and float(ph_content) <= 5:
    phlevel = 'acidic'
elif float(ph_content) >= 6 and float(ph_content) <= 8:
    phlevel = 'neutral'
elif float(ph_content) >= 9 and float(ph_content) <= 14:
    phlevel = 'alkaline'

print(crop_name)
print(humidity_level)
print(temperature_level)
print(rainfall_level)
print(nitrogen_level)
print(phosphorus_level)
print(potassium_level)
print(phlevel)
