import smtplib
from email.message import EmailMessage
import time
from datetime import datetime as dt
import socketio
import Adafruit_DHT


class Email(object):
    def __init__(self, server, port):
        self.smtp = smtplib.SMTP(server, port)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo()
        self.from_addr = ''

    def login(self, user_addr, password):
        self.smtp.login(user_addr, password)
        self.from_addr = user_addr

    def quit(self):
        self.smtp.quit()

    def sendMail(self, content, subject, to_addr):
        message = EmailMessage()
        message.set_content(content)
        message['From'] = self.from_addr
        message['Subject'] = subject
        message['To'] = to_addr
        self.smtp.send_message(message)


# configuracao: estas variaveis devem ser modificadas para cada dispositivo
url_socket = 'localhost:3000'
nome_dispositivo = 'DEVICE-01'
nome_aux = 'dispositivo 1'
temperatura_alerta = 25
tempo_alerta = 180

login = 'email@mail.com'
senha = 'senha123'

destino_alerta = "suporte@mail.com"


sensor = Adafruit_DHT.DHT11
pin = 4

SERVER = 'smtp.office365.com'
PORT = 587

sio = socketio.Client()

try:
    sio.connect(url_socket)
except:
    print('nao foi possivel conectar o servidor socket')






tai_on = False
alerta_emitido = False
email_enviado = False

print(f'Monitor iniciado')

while True:
    umidade, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    print(f'Leitura: Temperatura: {temperatura} | Umidade: {umidade}')

    try:
        sio.emit('message', {'dispositivo': str(nome_dispositivo), 'nome_aux': str(nome_aux), 'temperatura': str(temperatura), 'umidade': str(umidade)})
    except:
        print('nao foi possivel enviar dados via socket. Tentando conectar...')
        try:
            sio.connect(url_socket)
            sio.emit('message',
                     {'dispositivo': str(nome_dispositivo), 'nome_aux': str(nome_aux), 'temperatura': str(temperatura),
                      'umidade': str(umidade)})
        except:
            print('nao foi possivel conectar o servidor socket')
    finally:
        pass

    if temperatura is not None:
        if temperatura > temperatura_alerta:
            if tai_on is False:
                tempo_alerta_iniciado = time.time()
                print('alerta iniciado')

            tai_on = True
            if time.time() - tempo_alerta_iniciado > tempo_alerta:
                 print(f'Tempo corrido: {time.time()-tempo_alerta_iniciado}')
                 if alerta_emitido is False and email_enviado == False:
                     print('Email enviado')
                     email_enviado = True
                     email = Email(SERVER, PORT)
                     email.login(login, senha)
                     email.sendMail(f'Temperatura além do limite em {nome_dispositivo}\nÚltima leitura as {dt.now()}: {temperatura}ºC',
                    f'Temperatura além do limite em {nome_aux}', destino_alerta)
                     email.quit()

        else:
            email_enviado = False
            print("temperatura normalizada")
            tai_on = False




 
