from flask import *
from termcolor import colored
import os
import os
import sys
import cowsay

class Server:
    def banner(self):
        print(colored("    __  __   ", 'red'))
        print(colored("   (_\\)(/_) ", 'red'))
        print(colored("   (_(__)_)     [ Project Skynet ]", 'red'))
        print(colored("  (_(_)(_)_)         [ By ]", 'red'))
        print(colored("   (_(__)_)     [ Fajar Firdaus ]", 'red'))
        print(colored("     (__)    \n", 'red'))
        print(colored("{\n  Coder: 'FajarTheGGman', ", 'yellow'))
        print(colored("  Github: 'FajarTheGGman' ", 'yellow'))
        print(colored("  IG: @kernel024 ", 'yellow'))
        print(colored("  Twitter: @kernel024 \n}\n", 'yellow'))

    def main(self):
        app = Flask(__name__)

        @app.route('/')
        def main():
            return "Hello World! 🤖"

        @app.route('/stand')
        def stand():
            os.system('python3 bot.py 3 2')
            os.system('python3 bot.py 17 10')
            os.system('python3 bot.py 5 2')
            os.system('python3 bot.py 13 10')
            return "[+] Robot is stand"

        @app.route('/sit')
        def sit():
            os.system('python3 bot.py 13 5')
            os.system('python3 bot.py 17 5')
            os.system('python3 bot.py 3 7')
            os.system('python3 bot.py 5 6')
            return "[+] Robot is sit"

        @app.route('/walk')
        def walk():
            os.system('python3 bot.py 3 8')
            os.system('python3 bot.py 3 12')

            os.system('python3 bot.py 13 12')
            os.system('python3 bot.py 13 10')

            os.system('python3 bot.py 5 4')
            os.system('python3 bot.py 5 2')

            os.system('python3 bot.py 17 6')
            os.system('python3 bot.py 17 9')

            return "[+] Robot is walking"

        @app.errorhandler(404)
        def not_found(error):
            return "There is no page left 😞", 404

        @app.route('/ldr')
        def sensor_ldr():
            os.system('python3 ldr.py > /dev/null 2>&1 &')

        try:
            if str(sys.argv[1]) == '--help':
                print('Usage : python3 app.py local_ip, example: python3 app.py 192.168.1.3')
            else:
                app.run(host=str(sys.argv[1]))
        except:
            app.run()


try:
    x = Server()
    x.banner()
    x.main()
except KeyboardInterrupt:
    print(colored('Exiting program...', 'red'))
    os.system('killall python3')
