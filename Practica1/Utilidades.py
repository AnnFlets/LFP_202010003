class Utilidades:

    def __init__(self):
        pass

    def comprobarEntero(self, valor):
        try:
            dato = int(valor)
            return True
        except:
            return False

    def comprobarDecimal(self, valor):
        try:
            dato = float(valor)
            return True
        except:
            return False