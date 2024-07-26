import sidrapy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#https://apisidra.ibge.gov.br/values/t/1621/n1/all/v/all/p/all/c11255/90707,93406/d/v584%201
df_cnt = sidrapy.get_table(
    table_code='1621',
    territorial_level = "1",
    ibge_territorial_code = "all",
    variable="584",
    period = "all",
    classifications= {'11255':'90707,93406'},
    header='n')

println(1)