"""
Demostracion del patron Command: circuito de alta de clientes.
"""
from circuito import (Solicitud, RepositorioClientes, Notificador,
                      ProcesadorCircuito, circuito_para)


def main():
    repositorio = RepositorioClientes()
    notificador = Notificador()
    procesador = ProcesadorCircuito()

    altas = [
        ("20304050", "Ana Gomez", "persona"),
        ("30708090", "Textil SRL", "pyme"),
        ("30111222", "Holding SA", "corporativo"),
    ]

    for documento, nombre, segmento in altas:
        solicitud = Solicitud(documento, nombre, segmento)
        comandos = circuito_para(solicitud, repositorio, notificador)
        procesador.procesar(solicitud, comandos)

    print("Clientes registrados:", len(repositorio.clientes))
    print("\nAuditoria:")
    for linea in procesador.registro:
        print(linea)


if __name__ == "__main__":
    main()
