from src.database_module import DataBase
from src.plot_module import plt_plot as pl


## Porque es una clase con self debo crear primero el objeto con parametros si es el caso
data_module=DataBase()
data=data_module.get_data(n_data=10000)

## Como pl es estatico no debo crear el objeto
pl.plot(data=data,ciudad="MEDELLIN",departamento="ANTIOQUIA")





