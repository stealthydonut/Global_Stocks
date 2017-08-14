#Sourced from the following site https://github.com/mortada/fredapi
import pandas as pd


from fredapi import Fred
fred = Fred(api_key='4af3776273f66474d57345df390d74b6')
data = fred.get_series('TRESEGCAM052N')
