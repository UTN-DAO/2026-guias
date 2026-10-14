"""Demostración del patrón Facade: ABM de personas a través de una fachada."""
from fachada import FachadaPersonas, ServicioPersonas


def main():
    fachada = FachadaPersonas()
    servicio = ServicioPersonas(fachada)

    servicio.registrar("30111222", "Martin", "Perez", 34)
    servicio.registrar("27333444", "Ivan", "Gomez", 41)
    servicio.registrar("35666777", "Analia", "Sosa", 29)

    print("Personas cargadas:")
    servicio.mostrar()

    print("\nModificar edad de Martin y dar de baja a Ivan:")
    fachada.modificar("30111222", edad=35)
    fachada.baja("27333444")
    servicio.mostrar()

    print("\nAuditoria:")
    for evento in fachada._auditoria.eventos:
        print("   ", evento)


if __name__ == "__main__":
    main()
