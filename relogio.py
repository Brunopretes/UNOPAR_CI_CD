import datetime

def mostrar_hora():
    agora = datetime.datetime.now()
    print(f"Hora atual: {agora.strftime('%H:%M:%S')}")
    print(f"Data: {agora.strftime('%d/%m/%Y')}")

if __name__ == "__main__":
    mostrar_hora()
