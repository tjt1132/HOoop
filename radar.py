"""
Define el similador del Radar
"""
class Radar(object):


    def __init__(self, generador, detector):
        self.generador = generador
        self.detector = detector


    def detectar(self, medio, tiempo_inicial, tiempo_final):

        """
        Detecta si hay un blanco en un medio, en un intervalo de tiempo.
        """
        #Generar senal
        una_senal = self.generador.generar(tiempo_inicial, tiempo_final)
        #Retener una copia de la senal original
        una_senal_original = una_senal[:]

        #Mandar senal al medio
        una_senal_reflejada = medio.reflejar(una_senal, tiempo_inicial, \
        tiempo_final)

        #
        return self.detector.detectar(una_senal_original, una_senal_reflejada)

    #TODO agregar el metodo plotear_senal
    #Done
    def plot(self, senal):
        from matplotlib import pyplot as pp

        pp.figure()
        pp.scatter(range(len(senal)), senal)
        pp.show()
