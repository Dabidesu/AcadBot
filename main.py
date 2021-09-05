#Dependencies
import discord
import os
import requests
import json
import random
import os.path


#Discord Auth
from replit import db
client = discord.Client()

#Google Drive API Auth
from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

testo = "xd"
bad_words = ["fuck", "shit", "sex", "cock", "dick", "bitch", "bastard", "ass","retard", "nigger", "chingchong", "bobo", "tanga", "puta", "pota", "sht", "fk", "faggot"]
starter = ["Sorry sir/ma'am, this is a Christian server, **no swearing is allowed.**"]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = "**" + json_data[0]['q'] + "**" + " *-" + json_data[0]['a'] + "*"
  return(quote)


#Bot Events
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$hello'):
    await message.channel.send('Hello ' + message.author.mention)

  if msg.startswith('m$test'):
    await message.channel.send('```Deadlines \n '+ testo + 'asd```')

  if msg.startswith('$motivationpls'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in bad_words):
    await message.channel.send(random.choice(starter))



client.run(os.environ['abtoken'])

