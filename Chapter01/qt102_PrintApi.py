# -*- coding: utf-8 -*- 
'''
    【简介】
	保存PyQt5类的使用手册到本地
   
    
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage 
out = sys.stdout
sys.stdout = open(r'E:\QWebEnginePage .txt' , 'w')
help( QWebEnginePage  )
sys.stdout.close()
sys.stdout = out
