class Detector(object):

    def __init__(self):
        #TODO: completar con la inicializacion de los parametros del objeto
        #Done
        pass

    def detectar(self, senal_original, senal):

        #TODO: Completar
        #Done
        delta = [senal_original[i] - senal[i] for i in range(len(senal_original))]

        if sum(delta):
            return True
        else:
            return False
