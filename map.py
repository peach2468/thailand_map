# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:00:42 2023

@author: penchtir
"""

import pandas as pd
import folium
import ipywidgets as widgets
from IPython.display import display
#%%
df = pd.read_excel('C:/Users/penchtir/Downloads/Retail company -  store datail.xlsx',sheet_name='Location')
df = df.iloc[:, 6:-2]
new_columns = ['LocationName', 'Latitude', 'Longitude']  # Replace with your new column names

# Assign the new column names to the DataFrame
df.columns = new_columns
for index, row in df.iterrows():
    if row['LocationName'] == 'Oversea' or row['LocationName'] == 'Large':
        df.at[index, 'LocationName'] = df.at[index - 1, 'LocationName']
thailand_map = folium.Map(location=[13.7563, 100.5018], zoom_start=6)

custom_icon = folium.CustomIcon(
    icon_image="C:/Users/penchtir/Downloads/Peach_used/map/Central.png",  # Replace with the path to your custom marker image
    icon_size=(32, 32)  # Adjust the size of the custom marker image as needed
)


x = df[['LocationName','Latitude', 'Longitude']].copy()

feature_group1 = folium.FeatureGroup(name='Central Departmentstore')
feature_group1.add_to(thailand_map)
#Central
for index, row in x.iterrows():
    custom_icon = folium.CustomIcon(
        icon_image='https://th.bing.com/th/id/OIP.vrhr4QOuGaSyKWy0XtTS0AAAAA?pid=ImgDet&rs=1',  # Replace with the actual URL
        icon_size=(25, 25)
    )
    if row['LocationName'] == 'Central Departmentstore':
        folium.Marker([row['Latitude'], row['Longitude']],icon=custom_icon,popup=row['LocationName'],).add_to(thailand_map)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
feature_group2 = folium.FeatureGroup(name='Home Pro')
feature_group2.add_to(thailand_map)
#Home Pro
for index, row in x.iterrows():
    custom_icon = folium.CustomIcon(
        icon_image='https://seeklogo.com/images/H/homepro-logo-D4C6869EFF-seeklogo.com.png',  # Replace with the actual URL
        icon_size=(43.7956204, 20)
    )
    if row['LocationName'] == 'Home Pro' or row['LocationName'] == 'Home Pro S':
        folium.Marker([row['Latitude'], row['Longitude']],icon=custom_icon,popup=row['LocationName'],).add_to(thailand_map)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
feature_group3 = folium.FeatureGroup(name='Mega Home')
feature_group3.add_to(thailand_map)
#mega home
for index, row in x.iterrows():
    custom_icon = folium.CustomIcon(
        icon_image='https://th.bing.com/th/id/R.1199aa2bc7e37d6abeb1c64b7b7ca8be?rik=3DSZX67O4L%2bUuw&riu=http%3a%2f%2fwww.floyd.co.th%2fwp-content%2fuploads%2f2013%2f08%2flogo-megahome.jpg&ehk=AQrD%2fYqNLteCizLHe57a5nNpAEM7fvTAFo9YlGrNBpQ%3d&risl=&pid=ImgRaw&r=0',  # Replace with the actual URL
        icon_size=(25, 25)
    )
    if row['LocationName'] == 'Mega Home':
        folium.Marker([row['Latitude'], row['Longitude']],icon=custom_icon,popup=row['LocationName'],).add_to(thailand_map)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
feature_group4 = folium.FeatureGroup(name='Dohome ToGo')
feature_group4.add_to(thailand_map)
#Do home
for index, row in x.iterrows():
    custom_icon = folium.CustomIcon(
        icon_image='https://th.bing.com/th/id/OIP.dqEApCYShzhRnOztVSquOwHaHa?pid=ImgDet&rs=1',  # Replace with the actual URL
        icon_size=(25, 25)
    )
    if row['LocationName'] == 'Dohome ToGo':
        folium.Marker([row['Latitude'], row['Longitude']],icon=custom_icon,popup=row['LocationName'],).add_to(thailand_map)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
feature_group5 = folium.FeatureGroup(name='Thaiwatsadu')
feature_group5.add_to(thailand_map)
#Thaiwatsadu
for index, row in x.iterrows():
    custom_icon = folium.CustomIcon(
        icon_image='https://th.bing.com/th/id/OIP.JW--ujfavoukDloJ2FqoRAHaIG?pid=ImgDet&rs=1',  # Replace with the actual URL
        icon_size=(25, 25)
    )
    if row['LocationName'] == 'Thaiwatsadu':
        folium.Marker([row['Latitude'], row['Longitude']],icon=custom_icon,popup=row['LocationName'],).add_to(thailand_map)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
feature_group6 = folium.FeatureGroup(name='Robinson')
feature_group6.add_to(thailand_map)
#Robinson
for index, row in x.iterrows():
    custom_icon = folium.CustomIcon(
        icon_image='https://logodix.com/logo/1706407.jpg',  # Replace with the actual URL
        icon_size=(25, 25)
    )
    if row['LocationName'] == 'Robinson':
        folium.Marker([row['Latitude'], row['Longitude']],icon=custom_icon,popup=row['LocationName'],).add_to(thailand_map)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
feature_group7 = folium.FeatureGroup(name='Global House')
feature_group7.add_to(thailand_map)
#Global
for index, row in x.iterrows():
    custom_icon = folium.CustomIcon(
        icon_image='https://th.bing.com/th/id/OIP.tjQ8LJU0Bfc0iKaSJocLlQHaHa?pid=ImgDet&rs=1',  # Replace with the actual URL
        icon_size=(25, 25)
    )
    if row['LocationName'] == 'Global House':
        folium.Marker([row['Latitude'], row['Longitude']],icon=custom_icon,popup=row['LocationName'],).add_to(thailand_map)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

folium.LayerControl().add_to(thailand_map)
# folium.TileLayer('openstreetmap').add_to(thailand_map)
thailand_map.save('thailand_map.html')

