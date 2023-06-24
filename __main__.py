class Main:
	import os, platform, pip
	__osVersion = platform.system()
	if __osVersion == "Windows":
		PIP = pip.__version__[:2]
		os.system("pip -VV")
		if  int(PIP) >= 20:
			dirname = os.path.dirname(__file__)
			os.system("pip install -r requirements.txt")
			cmd = os.path.join(dirname, "src/mainpage.py")
			os.system("python "+cmd)
		else:
			os.system('exit')  

if __name__ == '__main__':
    Main()
