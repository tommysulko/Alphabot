import AlphaBot
import socket 
import time
import sqlite3


avanti = ["forward","f","avanti","dritto","a"]
dietro = ["backward","diesto","retromarcia","b"]
destra = ["right","r","destra","d"]
sinistra = ["left","l","sinistra","s"]
quadrato = ["quadrato","quad","q"]
curva_destra = ["curvad","curva_d","curva destra","curva d","curva a destra"]
curva_sinistra = ["curvas","curva_s","curva sinistra","curva s","curva a sinistra"]


bot = AlphaBot.AlphaBot()

tutti_comandi = {"f":bot.forward,"r":bot.right,"l":bot.left,"b":bot.backward,"s":bot.stop}

#                      IPv4             TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("192.168.0.130",5000)) #SOLO SUI SERVER
s.listen()
connection, address = s.accept()

"""
def curva_a_destra(bot):
    bot.forward()
    time.sleep(float(1.9))
    bot.stop()
    bot.right()
    time.sleep(float(0.23))
    bot.stop()
    bot.forward()
    time.sleep(float(1.9))
    bot.stop()

def curva_a_sinistra(bot):
    bot.forward()
    time.sleep(float(1.9))
    bot.stop()
    bot.left()
    time.sleep(float(0.23))
    bot.stop()
    bot.forward()  
    time.sleep(float(1.9))
    bot.stop()
"""

con = sqlite3.connect("./comandi.db")
cur = con.cursor()


while True:
    msg = connection.recv(4096) #4096 è la dimensione in byte
    msg = msg.decode()

    if len(msg) == 1:
        res = cur.execute(f"SELECT Movimento FROM Movimenti WHERE ID={msg}")
        comandi = str(res.fetchone()[0]).split(";")
        for comando in comandi:
            comandi = comando.split("|")
            tutti_comandi[comandi[0]]()
            time.sleep(float(comandi[1]))
    else:
        listaMex = msg.split("|")
        azione,tempo = listaMex[0],listaMex[1]
        if azione in avanti:
            bot.forward()
            time.sleep(float(tempo))
            bot.stop()
        if azione in destra:
            bot.right()
            time.sleep(float(tempo))
            bot.stop()
        if azione in sinistra:
            bot.left()
            time.sleep(float(tempo))
            bot.stop()
        if azione in dietro:
            bot.backward()  
            time.sleep(float(tempo))
            bot.stop()