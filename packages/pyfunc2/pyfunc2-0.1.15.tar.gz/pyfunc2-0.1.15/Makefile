genexecutable:
	cp main.py pyfunc2
	sed  -i '1i #!/usr/bin/python\n' pyfunc2

install: genexecutable
	sudo cp pyfunc2 /usr/bin/
	sudo chmod +x /usr/bin/pyfunc2
	rm pyfunc2