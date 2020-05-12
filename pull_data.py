#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tabula import read_pdf

import csv, sys



test_file_name='./reports/ABQ_MMI_2020-01.pdf'

base_file_name = './reports/ABQ_MMI_'
file_end_name = '.pdf'

out=dict()

Date = []
New_Listings = dict()
Pending_Sales = dict()
Closed_Sales =dict()
Days_On_Market= dict()
Median_Sales_Price = dict()
Average_Sales_Price = dict()
Percent_Of_List_Price_Received =dict()
Housing_Affordability_Index = dict()
Inventory_Of_Homes_For_Sale =dict()
Absorbtion_Rate = dict()

expected_labels = ['New Listings', 'Pending Sales', 'Closed Sales', 'Days on Market Until Sale', 'Median Sales Price', 'Average Sales Price', 'Percent of List Price Received', 'Housing Affordability Index', 'Inventory of Homes for Sale', 'Absorption Rate']




def string_to_float(x):
    return float(x.replace(',','').replace('$','').replace("%",''))


def date_to_index(s):
    return (int(s.split("-")[0])-1) + (int(s.split("-")[1])-2016)*12



for year in range(2017,2021):
    for month in range(1,13):
        try:
            pdf=read_pdf(base_file_name+str(year) +"-"+"{:02d}".format(month)+file_end_name, pages=2)[0]
            
            label = pdf.loc[:,'Unnamed: 0'].values.tolist()
            previous_value = pdf.loc[:, 'Unnamed: 4'].values.tolist()
            value = pdf.loc[:, 'Unnamed: 5'].values.tolist()
            
            reduced_label = label[slice(1,-1,2)]
            assert(reduced_label == expected_labels)
            
            
            date = date_to_index(value[0])
            previous_date = date_to_index(previous_value[0])
            
            reduced =  list(map( string_to_float , value[slice(1, -1, 2)]))
            previous_reduced = list(map( string_to_float , previous_value[slice(1, -1, 2)]))
            
            
            out[date] = reduced
            out[previous_date] = previous_reduced
            
        except Exception as e:
            print(e)
            print(sys.exc_info()[0])
            print(year, "-", month)

print(out)

with open('GAAR_Reports.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date_Indexed"]+expected_labels)
    for i in range(0,60):
        try:
            writer.writerow([i]+out[i])
        except Exception as e:
            print(e)
            print(sys.exc_info()[0])  





    




reduced_label = ["Date"].append(reduced_label)








