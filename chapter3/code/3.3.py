from __future__ import print_function
import pandas as pd
import numpy as np


dish_profit = '../data/catering_dish_profit.xls'
data = pd.read_excel(dish_profit,index_col=u'菜品名')
data = data[u'盈利'].copy()