# -*- coding: utf-8 -*-
import urllib2
import pandas as pd
import numpy as np
import time
from spyre import server
from matplotlib import pyplot as plt

changing_index = {
    1: 22,
    2: 24,
    3: 23,
    4: 25,
    5: 3,
    6: 4,
    7: 8,
    8: 19,
    9: 20,
    10: 21,
    11: 9,
    12: 0,
    13: 10,
    14: 11,
    15: 12,
    16: 13,
    17: 14,
    18: 15,
    19: 16,
    20: 0,
    21: 17,
    22: 18,
    23: 6,
    24: 1,
    25: 2,
    26: 7,
    27: 5
}

rename_columns = {
    "VCI": "Vegetation Condition Index",
    "VHI": "Vegetation Health Index",
    "TCI": "Temperature Condition Index",
    "%Area_VHI_LESS_15": "Percentage of an area, where VHI less than 15%",
    "%Area_VHI_LESS_35": "Percentage of an area, where VHI less than 35%"
}

def DownloadFile(index):
    # changing index in accordance with task
    index = changing_index[index]
    """
        filename - number of the file on website
        because files are numerating like (01, 02, ..., 09, 10, ...)
    """
    filename = ""
    if index <= 0 or index > 27:
        return False
    elif index < 10:
        filename += "0" + str(index)
    else:
        filename += str(index)
    # opening url
    url = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R%s.txt" % filename
    url_file = urllib2.urlopen(url)
    current_time = str(time.strftime("%d.%m.%Y_%H-%M-%S"))
    out = open("Files/vhi_id_%s_%s.csv" % (filename, current_time), "w")
    print ("Downloading file vhi_id_%s" % filename)
    out.write(url_file.read())
    out.close()
    return "Files/vhi_id_%s_%s.csv" % (filename, current_time)

def ReversedChangeIndex(index):
    index = int(index)
    if index < 1 or index > 25:
        return 0
    for i in range(1, len(changing_index)):
        if int(changing_index[i]) == index:
            return int(i)
    return 0


class WebApp(server.App):
    title = "Lab 2"
    inputs = [{"input_type": "dropdown",
               "label": "Дані",
               "options": [{"label": "VHI", "value": "VHI"},
                           {"label": "TCI", "value": "TCI"},
                           {"label": "VCI", "value": "VCI"}],
               "variable_name": "column_name",
               "action_id": "update_data"},
              {"input_type": "dropdown",
               "label": "Область",
               "options": [{"label": "Вінницька", "value": 1},
                           {"label": "Волинська", "value": 2},
                           {"label": "Дніпропетровська", "value": 3},
                           {"label": "Донецька", "value": 4},
                           {"label": "Житомирська", "value": 5},
                           {"label": "Закарпатська", "value": 6},
                           {"label": "Запорізька", "value": 7},
                           {"label": "Івано-франківська", "value": 8},
                           {"label": "Київська", "value": 9},
                           {"label": "Кіровоградська", "value": 10},
                           {"label": "Луганська", "value": 11},
                           {"label": "Львівська", "value": 13},
                           {"label": "Миколайвська", "value": 14},
                           {"label": "Одеська", "value": 15},
                           {"label": "Полтавська", "value": 16},
                           {"label": "Рівненська", "value": 17},
                           {"label": "Сумська", "value": 18},
                           {"label": "Тернопільська", "value": 19},
                           {"label": "Харківська", "value": 21},
                           {"label": "Херсонська", "value": 22},
                           {"label": "Хмельницька", "value": 23},
                           {"label": "Черкаська", "value": 24},
                           {"label": "Чернівецька", "value": 25},
                           {"label": "Чернігівська", "value": 26},
                           {"label": "Республіка Крим", "value": 27}],
               "variable_name": "region_index",
               "action_id": "update_data"},
              {"input_type": "slider",
               "label": "Рік",
               "min": 1981,
               "max": 2016,
               "variable_name": "year",
               "action_id": "update_data"}]

    tabs = [ "Plot", "Table"]
    outputs = [ { "output_type": "plot",
                   "output_id": "plot",
                   "control_id": "update_data",
                   "tab": "Plot",
                   "on_page_load": True},
                 {"output_type": "table",
                  "output_id": "table_id",
                  "control_id": "update_data",
                  "tab": "Table",
                  "on_page_load": True} ]
    controls = [{"control_type": "hidden",
                 "label": "Update",
                 "control_id": "update_data"}]

    def __init__(self):
        self.dframe = []
        for index in range(1, 28):
            if index == 12 or index == 20:
                self.dframe.append(pd.DataFrame())
                continue
            path = DownloadFile(index)
            if path == False:
                print ("Failed to download file!")
                return
            else:
                self.dframe.append(pd.read_csv(path, index_col=False, header=1))

    def getData(self, params):
        df = self.dframe[int(params['region_index']) - 1]
        df.rename(columns=rename_columns, inplace=True)
        return pd.DataFrame(df[df['year'] == params['year']], columns=['year', 'week', rename_columns[params['column_name']]])

    def getPlot(self, params):
        df = self.getData(params)
        x = df['week']
        y = df[rename_columns[params['column_name']]]
        plt.plot(x, y)
        plt.title(("%s for %s") % (params['column_name'], int(params['year'])))
        plt.xlim(1, 52)
        plt.xlabel("Weeks")
        plt.ylabel(rename_columns[params['column_name']])
        return plt.gcf()


app = WebApp()
app.launch()
#main();