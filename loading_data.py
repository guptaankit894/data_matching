import pandas as pd
from sqlalchemy import create_engine # find the location of mysql (address)
import mysql.connector as mc # Passing mysql credentials and connecting to mysql
import time
import os
import subprocess

year = os.environ.get('year')
year=int(year)
orig_dir='./excellence'
proc_dir='./inputs'
files=['Excel','Lead']


def read_data(file1, file2):
	# Reading original data
	matched_pme_pt=pd.read_excel(file1)
	pme=pd.read_excel(file2)
	return matched_pme_pt, pme


# read data
matched_pme_pt, pme_excellence, pme_lead=read_data(



	os.path.join(os.getcwd(),proc_dir,'Excel',str(year)+".xlsx")


