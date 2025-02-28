import matplotlib.pyplot as plt

class plt_plot():
    # Clase estatica
    @staticmethod
    def plot(data,ciudad, departamento):

        datos=data[(data.nombre_departamento==departamento)&
            (data.nombre_municipio==ciudad)&
            (data.nombre_de_la_clase.isin(["AUTOMOVIL","CAMPERO"]))]
        datos=datos.groupby("fecha_de_registro")["cantidad"].sum().reset_index()
        plt.plot(datos["fecha_de_registro"],datos["cantidad"])
        plt.show()