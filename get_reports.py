# -*- coding: utf-8 -*-

import wget
import time
import os.path

out_dir = './reports/'
base_url = 'http://www.gaar.com/images/uploads/statistics/'

for year in range(2017,2021):
    for month in range(1,13):
        name = "ABQ_MMI_"+str(year) +"-"+"{:02d}".format(month)+'.pdf'
        print(base_url+name)
        try:
            if not os.path.isfile(out_dir+name):
                wget.download(base_url+name,out_dir+name)
            time.sleep(1.3)
        except:
            pass


