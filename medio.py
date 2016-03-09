class Medio(object):

    def __init__(self, blancos):
        #List of blancos
        self.blancos = blancos

    def reflejar(self, una_senal, tiempo_inicial, tiempo_final):
        """
        Los blancos en el medio reflejan la senal
        """
        #TODO reflejar en un medio debe reflejar en todos los blancos de un medio
        #y devolver la senal reflejada
        #Done
        #ret = list()

        #for blanco in blancos:
        #    ret.append(blanco.reflejar( senal, tiempo_inicial, tiempo_final ) ))

        return self.blancos.reflejar( una_senal, tiempo_inicial, tiempo_final )
