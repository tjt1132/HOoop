class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        #TODO: completar con la inicializacion de los parametros del objeto
        #Done
        #Scalar factor for amplitude response
        self.amplitud = amplitud
        #Time of target appearance
        self.tiempo_inicial = tiempo_inicial
        #Time of target disappereance
        self.tiempo_final = tiempo_final

    def reflejar(self, senal, tiempo_inicial_senal, tiempo_final_senal):

        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        #Done
        if tiempo_inicial_senal <= self.tiempo_final and \
        tiempo_final_senal >= self.tiempo_final and \
        tiempo_inicial_senal >= self.tiempo_inicial:
            tiempo_de_deteccion = (self.tiempo_final - tiempo_inicial_senal).seconds
            senal[:tiempo_de_deteccion] = [ i * self.amplitud \
            for i in senal[:tiempo_de_deteccion]]

        elif tiempo_inicial_senal <= self.tiempo_inicial and \
        tiempo_final_senal >= self.tiempo_inicial and \
        tiempo_final_senal <= self.tiempo_final:
            tiempo_de_deteccion = (tiempo_final_senal - self.tiempo_inicial).seconds
            senal[len(senal) - tiempo_de_deteccion:] = [ i * self.amplitud \
            for i in senal[len(senal) - tiempo_de_deteccion:]]

        elif tiempo_inicial_senal < self.tiempo_inicial and \
        tiempo_final_senal > self.tiempo_final:
            tiempo_de_deteccion = (self.tiempo_final - self.tiempo_inicial).seconds
            index_inicial = (self.tiempo_inicial - tiempo_final_senal).seconds
            senal[index_inicial:index_inicial + tiempo_de_deteccion] = \
            [ i * self.amplitud for i in \
             senal[index_inicial:index_inicial + tiempo_de_deteccion]]

        elif tiempo_inicial_senal > self.tiempo_inicial and \
        tiempo_final_senal < self.tiempo_final:
            senal = [ i * self.amplitud for i in senal ]

        return senal
