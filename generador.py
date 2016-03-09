"""
Un generador de senal es el responsable de generar una senal portadora.

"""

class Generador(object):

    def __init__(self, amplitud, fase, frecuencia):
        #Amplitud de la senal generada
        self.amplitud = amplitud
        #Fase en porcentage de defasado
        self.fase = fase
        #Frecuencia de la senal
        self.frecuencia = frecuencia

        #  Samples per second (Nyquist Rate)
        self.frecuencia_muestreo = frecuencia*2

    def generar(self, tiempo_inicial, tiempo_final):

        import math

        cantidad_muestras = int((tiempo_final - tiempo_inicial).seconds * \
        self.frecuencia_muestreo)

        muestras = range(cantidad_muestras)
        #TODO agregar un ruido blanco a la senal

        ret = [self.amplitud*math.sin( ( 8. / 3180. ) * self.frecuencia * i \
        + ( math.pi * self.fase ) ) for i in muestras]

        return ret
