import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox
from smtplib import SMTP
from tkinter import *
import os


confirme_enviar = True
def enviar_file(destinatario, endereco_file, assunto):
    global confirme_enviar
    try:
      # cria o servidor SMTP
      context = ssl.create_default_context()
      server = smtplib.SMTP('smtp.outlook.com', 587)
      server.ehlo()
      server.starttls(context=context)
      server.ehlo()

      # dados do remetente
      sender_email = 'expertemcifras@outlook.com'
      password = '@#Mmlx1985'

      # dados do destinatário
      receivers = [f'{destinatario}']

      # dados do e-mail
      body = assunto
      message = MIMEMultipart()
      message['Subject'] = assunto
      message['From'] = sender_email
      message['To'] = ','.join(receivers)
      message.attach(
        MIMEText(
          f'{assunto}',
          'plain'
        )
      )

      # define os atributos do anexo
      filename = os.getcwd() + rf'/Minhas_cifras/{endereco_file}.txt'
      attachment = MIMEBase('application', 'octet-stream')

      with open(filename, 'rb') as f:
        attachment.set_payload(f.read())

      encoders.encode_base64(attachment)

      attachment.add_header(
        'Content-Disposition',
        f'attachment; filename={filename}',
      )

      # anexa o arquivo no e-mail
      message.attach(attachment)

      # realiza login no servidor
      server.login(sender_email, password)

      # envia o email
      server.sendmail(sender_email, receivers, message.as_string())
      #messagebox.showinfo(message=f'Email enviado com sucesso')

    except Exception as e:
      confirme_enviar = False
      print(e)
    finally:
      # fecha o servidor
      server.quit()

if __name__ == '__main__':
  enviar_file('moises.miss@gmail.com', 'B', '')
