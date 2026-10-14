"""
Demostracion del semaforo con patron State.
"""
from semaforo import Semaforo


def main():
    semaforo = Semaforo()
    print("=== Ciclo normal ===")
    for _ in range(6):
        print("Estado:", semaforo.actual())
        semaforo.siguiente()

    print("\n=== Con modo peatonal activado ===")
    semaforo.activar_modo_peatonal()
    for _ in range(8):
        print("Estado:", semaforo.actual())
        semaforo.siguiente()


if __name__ == "__main__":
    main()
