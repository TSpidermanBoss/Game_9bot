from pyrogram import Client, Filters
import random

app = Client('835349563:AAEraMgAMwRFzOdv7kMLVOYSRgYBL-mlTwA')
@app.on_message(Filters. command('toss'))
def randheadtain(client, message):
    client.send_message(message.chat.id, random.choice(['Coin flipped: Head', 'Coin flipped: Tail']))


@app.on_message(Filters.command('roll'))
def ran(client, message):
 if len(message.text.split(' ')) > 1:
  client.send_message(message.chat.id, random.choice(range(1, int(message.text.split(' ')[1]))))
 else:
  message.reply('Please set a range!')





@app.on_message(Filters. command('show'))
def show(client, message):
    client.send_message(message.chat.id, [random.choice(['A','1','2','3','4','5','6','7','8','9','10','J','K','Q'])for i in range(3)])

app.run()

while 1:
    time.sleep(10)