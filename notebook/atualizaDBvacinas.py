from selenium import webdriver
import requests
import time
import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns; sns.set()
from datetime import datetime
import camelot
import folium
from folium import plugins
import pathlib


path_download19 = Path(parent,"bases/{}/vacinas.csv".format(cidade))
