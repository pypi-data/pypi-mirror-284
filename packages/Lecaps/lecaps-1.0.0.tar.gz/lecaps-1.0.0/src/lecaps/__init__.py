from matplotlib import pyplot as plt
import numpy as np 

from datetime import datetime, timedelta
import pandas as pd

def get_start_date():
    current_time = datetime.now()
    target_time = current_time.replace(hour=18, minute=30, second=0, microsecond=0)
    today_label = current_time.strftime('%A').lower()

    if today_label in ["monday", "tuesday", "wednesday", "thursday"]:
        if current_time > target_time:
            start_date = current_time.date() + timedelta(days=1)
        else:
            start_date = current_time.date()
    elif today_label == "friday":
        if current_time > target_time:
            start_date = current_time.date() + timedelta(days=3)
        else:
            start_date = current_time.date()
    elif today_label == "saturday":
        start_date = current_time.date() + timedelta(days=2)
    else:  # sunday
        start_date = current_time.date() + timedelta(days=1)

    return start_date

def days360(end_date, today = None, method=False):
    
    if today == None: 
        start_date = pd.to_datetime(get_start_date())
    else: 
        start_date = pd.to_datetime(today)
    
    end_date = pd.to_datetime(end_date)

    start_day = start_date.day
    start_month = start_date.month
    start_year = start_date.year

    end_day = end_date.day
    end_month = end_date.month
    end_year = end_date.year

    if not method:  # US method
        if start_day == 31:
            start_day = 30
        if end_day == 31 and start_day == 30:
            end_day = 30
    else:  # European method
        if start_day == 31:
            start_day = 30
        if end_day == 31:
            end_day = 30

    days_difference = 360 * (end_year - start_year) + 30 * (end_month - start_month) + (end_day - start_day)

    return days_difference

class Lecaps:
    def __init__(self, nombre: str, vencimiento: str, amortizacion: float) -> None:
        """
        Inicializa una instancia de Lecaps.

        Args:
            nombre (str): El nombre de la Lecaps.
            vencimiento (str): La fecha de vencimiento.
            amortiza (float): El monto de la amortización.
        """
        self.nombre = nombre
        self.vencimiento = vencimiento
        self.amortizacion = amortizacion

    def info(self) -> str:
        """
        Devuelve la información de vencimiento y amortización en un formato legible.

        Returns:
            str: La información formateada de vencimiento y amortización.
        """
        diferencia = pd.to_datetime(self.vencimiento) - pd.to_datetime(get_start_date())
        return f"Lecap: {self.nombre} \nVencimiento: {self.vencimiento} ({diferencia.days} dias) \nAmortiza: {self.amortizacion}"
    
    def Tasas(self, Precio: float, Precio_Final = None, end_date = None) -> dict: 
    
        start_date = get_start_date()

        if end_date is None:
            end_date = self.vencimiento
        
        if Precio_Final is None: 
            Precio_Final = self.amortizacion

        difference_in_days = (pd.to_datetime(end_date) - pd.to_datetime(start_date)).days
        difference_in_days_360 = (days360(end_date)) / 30
        difference_in_360 = days360(end_date)

        REN = round((Precio_Final / Precio - 1), 4) * 100
        TNA = round((Precio_Final / Precio - 1) * (360 / difference_in_360), 4) * 100
        TEA = round((Precio_Final / Precio) ** (360 / difference_in_360) - 1, 4) * 100
        TEM = round((Precio_Final / Precio) ** (1 / difference_in_days_360) - 1, 4) * 100

        return {
            "TNA": TNA,
            "TEA": TEA,
            "TEM": TEM,
            "REN": REN,
            "Duration": difference_in_days_360,
            "Dias": difference_in_days
        }

    

# Crear varias instancias de Lecaps
S26L4 = Lecaps("S26L4", "2024-07-26", 109.012)
S16G4 = Lecaps("S16G4", "2024-08-16", 109.347)
S30G4 = Lecaps("S30G4", "2024-08-30", 113.250)
S13S4 = Lecaps("S13S4", "2024-09-13", 113.142)
S30S4 = Lecaps("S30S4", "2024-09-30", 113.142)
S14O4 = Lecaps("S14O4", "2024-10-14", 131.902)
S29N4 = Lecaps("S29N4", "2024-11-29", 134.983)
S13D4 = Lecaps("S13D4", "2024-12-13", 126.830)
S17E5 = Lecaps("S17E5", "2025-01-17", 131.185)
S31E5 = Lecaps("S31E5", "2025-01-31", 172.653)
S28F5 = Lecaps("S28F5", "2025-02-28", 158.288)
S31M5 = Lecaps("S31M5", "2025-03-31", 155.582)

lista_lecaps = [S26L4, S16G4, S30G4, S13S4, S30S4, S14O4, S29N4, S13D4, S17E5, S31E5, S28F5, S31M5]

def lecaps_vigentes(lecaps_nombres = lista_lecaps): 
    print("Las Lecaps vigentes son: ")
    for lecap in lecaps_nombres: 
        print(lecap.nombre)   

def imprimir_tasa_lecaps(lecaps_nombres = lista_lecaps, precios = None):
    tasa = input("Por favor selecciona TNA, TEM o TEA: ")
    if tasa == "TEM": 
        for lecaps, precio in zip(lecaps_nombres, precios):
            print(f"{lecaps.nombre} TEM: {lecaps.Tasas(precio)['TEM']}")
    elif tasa == "TNA": 
        for lecaps, precio in zip(lecaps_nombres, precios):
            print(f"{lecaps.nombre} TNA: {lecaps.Tasas(precio)['TNA']}")
    elif tasa == "TEA": 
        for lecaps, precio in zip(lecaps_nombres, precios):
            print(f"{lecaps.nombre} TEA: {lecaps.Tasas(precio)['TEA']}")
    else: 
        print("Hubo un error, intenta de nuevo.")

def curva_de_tasas(lecaps_list = lista_lecaps, precios = None): 
    duration = []
    tem = []
    names = []

    for lecaps, precio in zip(lecaps_list, precios):
        duration.append(lecaps.Tasas(precio)['Duration'])
        tem.append(lecaps.Tasas(precio)['TEM'])
        names.append(lecaps.nombre)

# Convertir listas a numpy arrays para facilitar el manejo
    duration = np.array(duration)
    tem = np.array(tem)

# Calcular la línea de tendencia (ajuste polinómico)
    poly_fit = np.polyfit(duration, tem, 2)  # Ajuste polinómico de grado 2

# Generar puntos para la línea de tendencia
    poly_x = np.linspace(duration.min(), duration.max(), 100)
    poly_y = np.polyval(poly_fit, poly_x)

# Graficar los puntos y la línea de tendencia
    plt.figure(figsize=(10, 6))
    plt.scatter(duration, tem, label='Datos LECAPS', color='blue')
    plt.plot(poly_x, poly_y, label='Línea de Tendencia', color='red')
    plt.xlabel('Duration')
    plt.ylabel('TEM')
    plt.title('Duration vs TEM de LECAPS')
    plt.grid(True)
    plt.legend()

    # Etiquetar cada punto con el nombre de LECAPS
    for name, x, y in zip(names, duration, tem):
        plt.text(x, y, name, fontsize=9, ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

message = """

Aclaraciones:
- La base temporal de cálculos que se toma es de 360 días.
- El rendimiento está calculado como (Precio/Precio Final) - 1. Se asume que se compran y venden la misma cantidad de nominales.
- Los precios finales se toman de la calculadora de CocosCapital.
"""

separator = "-" * 20

print(message)
print(separator)
