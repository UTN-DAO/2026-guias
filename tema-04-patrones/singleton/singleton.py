'''
Ejemplo de implementación de patrón Singleton
'''

class Singleton:
    # Variable de instancia, para contener el objeto
    _instance = None

    def __new__(cls):
        """El operador __new__ se dispara automáticamente al
        crear un objeto de una clase. 
        :cls: Clase que se está creando
        :return: Devuelve un nuevo objeto
        """
        # Si no está asignado _instance
        if cls._instance is None: 
            # Pedirle al padre (super), que cree un objeto cls 
            # y lo asigne a _instance
            cls._instance = super(Singleton, cls).__new__(cls)
        # Retornar _instance, ya sea si estaba asignado o
        # si se acaba de crear 
        return cls._instance