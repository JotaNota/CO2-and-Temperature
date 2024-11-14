import matplotlib.pyplot as plt

def plot_annual_anomalies(annual_anomalies):
    """
    Grafica las anomalías de temperatura anuales.
    Args:
        annual_anomalies (pd.Series): Serie de anomalías anuales agrupadas por año.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(annual_anomalies.index, annual_anomalies.values, marker='o', linestyle='-', color='b', label='Annual Anomaly')
    plt.title('Annual Temperature Anomalies (1980 - Most Recent Year)')
    plt.xlabel('Year')
    plt.ylabel('Temperature Anomaly (°C)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()
