  
from pyrogram import Client, Filters, Emoji
import random
import time
app = Client("session",bot_token="663574960:AAGWg1VGruCPuckHzjbpDLRIbPWkX6YcDlc",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b")  


@app.on_message(Filters.command('bowl'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
    if len(message.text.split(' ')) > 1:
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
      z = random.choice(["dot ball","wide ball","no ball"])
      a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("1"))
      k = a.replace('Ball 0.{}🎾:','').replace('Runs','').replace('Score','').replace('dot ball','0').replace('no ball','1').replace('wide ball','1')
      print(k)
      time.sleep(2)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
      z = random.choice(["dot ball","wide ball","no ball"])
      if a.text == "Ball 0.1🎾: no ball" or a.text == "Ball 0.1🎾: wide ball":
        a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("1"))
        k = k + a.replace('Ball 0.{}🎾:','').replace('Runs','').replace('Score','').replace('dot ball','0').replace('no ball','1').replace('wide ball','1')
        print(k)
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
        z = random.choice(["dot ball"])
        if a.text == "Ball 0.1🎾: no ball" or a.text == "Ball 0.1🎾: wide ball":
          a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("1"))
          k = k + a.replace('Ball 0.{}🎾:','').replace('Runs','').replace('Score','').replace('dot ball','0').replace('no ball','1').replace('wide ball','1')
          print(k)
          time.sleep(2)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
          z = random.choice(["dot ball","wide ball","no ball"])
      a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("2"))
      time.sleep(2)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
      z = random.choice(["dot ball","wide ball","no ball"])
      if a.text == "Ball 0.2🎾: no ball" or a.text == "Ball 0.2🎾: wide ball":
        a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("2"))
        time.sleep(2)
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
        z = random.choice(["dot ball"])
        if a.text == "Ball 0.2🎾: no ball" or a.text == "Ball 0.2🎾: wide ball":
          a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("2"))
          time.sleep(2)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
          z = random.choice(["dot ball","wide ball","no ball"])
      a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("3"))
      time.sleep(2)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
      z = random.choice(["dot ball","wide ball","no ball"])
      if a.text == "Ball 0.3🎾: no ball" or a.text == "Ball 0.3🎾: wide ball":
        a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("3"))
        time.sleep(2)
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
        z = random.choice(["dot ball"])
        if a.text == "Ball 0.3🎾: no ball" or a.text == "Ball 0.3🎾: wide ball":
          a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("3"))
          time.sleep(2)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
          z = random.choice(["dot ball","wide ball","no ball"])
      a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("4"))
      time.sleep(2)
      x = random.choice(["3","2","3","4","2","1","2","4","1","6","3","4","2","3","6","4","3"])
      y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
      z = random.choice(["dot ball","wide ball","no ball"])
      if a.text == "Ball 0.4🎾: no ball" or a.text == "Ball 0.4🎾: wide ball":
        a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("4"))
        time.sleep(2)
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
        z = random.choice(["dot ball"])
        if a.text == "Ball 0.4🎾: no ball" or a.text == "Ball 0.4🎾: wide ball":
          a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("4"))
          time.sleep(2)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
          z = random.choice(["dot ball","wide ball","no ball"])
      a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("5"))
      time.sleep(2)
      x = random.choice(["3","2","3","4","2","1","2","4","1","6","3","4","2","3","6","4","3"])
      y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
      z = random.choice(["dot ball","wide ball","no ball"])
      if a.text == "Ball 0.5🎾: no ball" or a.text == "Ball 0.5🎾: wide ball":
        a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("5"))
        time.sleep(2)
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
        z = random.choice(["dot ball"])
        if a.text == "Ball 0.5🎾: no ball" or a.text == "Ball 0.5🎾: wide ball":
          a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("5"))
          time.sleep(2)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
          z = random.choice(["dot ball","wide ball","no ball"])
      a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("6"))
      time.sleep(2)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
      z = random.choice(["dot ball","wide ball","no ball"])
      if a.text == "Ball 0.6🎾: no ball" or a.text == "Ball 0.6🎾: wide ball":
        a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("6"))
        time.sleep(2)
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
        z = random.choice(["dot ball"])
        if a.text == "Ball 0.6🎾: no ball" or a.text == "Ball 0.6🎾: wide ball":
          a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("6"))
          time.sleep(2)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
          z = random.choice(["dot ball","wide ball","no ball"])
    else:
      message.reply('Please write ball number after command!')


@app.on_message(Filters. command('leavechat'))
def ran(client,message):
 if message.from_user.id == 312525402:
  if len(message.text.split( )) > 1:
    client.leave_chat(int(message.text.split(' ')[1]))
  else:
    client.leave_chat(message.chat.id)
@app.on_message(Filters. command('cnnn'))
def ran(client,message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
  with open("sure.txt","w") as file:
   file.write("no")
   file.close()
   message.reply("Success off")
app.run()
