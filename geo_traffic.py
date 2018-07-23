#coding=utf-8
import json

import geopandas
import matplotlib.pyplot as plt
import requests
from shapely.geometry import LineString
import time
from locaDiv import LocaDiv



BASE_URL = 'https://restapi.amap.com/v3/traffic/status/rectangle?rectangle={loc}&key=你的KEY&extensions=all'



def request_amap():
    loc = LocaDiv('108.781305,34.166266,109.118206,34.375328')
    locs = loc.ls_row()
    Lines = []
    Names = []
    Speeds = []
    Status = []
    Lenghts = []
    for i in locs:
        url = BASE_URL.format(loc=i)
        res = requests.get(url)
        datas = res.json()
        if datas['status'] == '1':
            for road in datas['trafficinfo']['roads']:
                polyline = road['polyline']
                polylines = [(float(y[0]),float(y[1])) for y in [x.split(',') for x in [i for i in polyline.split(';')]]]
                line = LineString(polylines)
                Lines.append(line)
                Names.append(road['name'])
                if 'speed' in road: Speeds.append(int(road['speed']))
                else: Speeds.append(100)
                Status.append(road['status'])
                Lenghts.append(line.length)
    return {'name':Names,"speed":Speeds,"geometry":Lines,'status':Status,'lenght':Lenghts}
                        
def plot_show(pds_dict):
    xian = geopandas.GeoDataFrame(pds_dict)
    print xian
    xian.plot(column='speed',cmap='RdYlGn',legend=True)
    #xian.to_file(time.strftime("%Y%m%d%H%M", time.localtime())+'_xian_traffic')
    plt.show()

def read_json():
    #xian = geopandas.GeoDataFrame.from_file('items.json')
    Lines = []
    Names = []
    Speeds = []
    with open('/home/vowers/workspaces/爬虫/amap_traffic/items.json') as f:
        for line in f.readlines():
            line = eval(line)
            polyline = line['polyline']
            polylines = [(float(y[0]),float(y[1])) for y in [x.split(',') for x in [i for i in polyline.split(';')]]]
            Names.append(line['name'])
            Speeds.append(int(line['speed']))
            Lines.append(LineString(polylines))

    return {'name':Names,"speed":Speeds,"geometry":Lines}
    
if __name__ == '__main__':
    plot_show(request_amap())
