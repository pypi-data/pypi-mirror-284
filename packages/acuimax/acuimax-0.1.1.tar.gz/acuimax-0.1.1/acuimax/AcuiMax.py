def calcular_capacidad_carga(T, R, alpha):
    return alpha * R * T

def calcular_tiempo_agotamiento(V, Q_max):
    return V / Q_max

def capacidad_carga_maxima(transmisividad, recarga_anual, factor_seguridad):
    return factor_seguridad * recarga_anual * transmisividad

def tiempo_agotamiento(volumen, capacidad_carga_maxima):
    return volumen / capacidad_carga_maxima
