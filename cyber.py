#coding=utf-8
import os
import sys
import time
def load():
    load = ['\033[94m             ╼╣\033[91m█\033[90m▒▒▒▒▒▒▒▒▒▒▒▒▒\033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████████████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '\033[94m             ╼╣\033[91m█\033[90m▒▒▒▒▒▒▒▒▒▒▒▒▒\033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████████████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '\033[94m             ╼╣\033[91m█\033[90m▒▒▒▒▒▒▒▒▒▒▒▒▒\033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████████████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '\033[94m             ╼╣\033[91m█\033[90m▒▒▒▒▒▒▒▒▒▒▒▒▒\033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████████████\033[94m╠╾ ', '             \033[94m╼╣\033[91m███████\033[90m▒\033[91m███████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██████\033[90m▒▒▒\033[91m██████\033[94m╠╾ ', '             \033[94m╼╣\033[91m████\033[90m▒▒▒▒▒▒▒\033[91m████\033[94m╠╾ ', '             \033[94m╼╣\033[91m██\033[90m▒▒▒▒▒▒▒▒▒▒▒\033[91m██\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[91mDin-zUgex95 \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[93mDin-zUgex95 \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[92mDin-zUgex95 \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[96mDin-zUgex95 \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[91mDin-zUgex95 \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[93mDin-zUgex95 \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[92mDin-zUgex95 \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[96mDin-zUgex95 \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[91mDin-zUgex95 \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[93mDin-zUgex95 \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[92mDin-zUgex95 \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '             \033[94m╼╣\033[91m█ \033[96mDin-zUgex95 \033[91m█\033[94m╠╾ ', '             \033[94m╼╣\033[91m█             █\033[94m╠╾ ', '                                     ', '']
    for o in load:
        print '\r' + o,;sys.stdout.flush();time.sleep(0.1)



os.system("clear")
def banner():
    print """\033[97m
  ▄     ▄    \033[95m﹏﹏﹏﹏﹏﹏\033[97m
 █████████   \033[91m╔═╦═╕╔══╕╦═≎╗╔═╦═╗╦  ╦─══╗ ╦≽
 \033[97m█▄█████▄█   \033[90m╽ ╫  ╠═╡ ╠╪╦╝║ ╨ ║║  ║ ╔═╬═╝
 \033[97m█\033[91m▼▼▼▼▼▼       \033[97m╩  ╚═≓═╝ ╚═╬   ╩╚≐═╝─╩─╚══≑═≽
 \033[97m█\033[90m(̅_̅_̅(̅(̅_̅_̅_̅_̅_̅_̅̅\033[92m()\033[97m╦═╗ ╔≒═╗╔═╗╽╔╔══╕╔══╡╔≑═╗╔╦═╗
 \033[97m█\033[91m▲▲▲▲▲▲       \033[90m╠═╩╗╠══╣║ ║ ║╫ ╾╗╚═╪╗╠══╣╿║ ╫
 \033[97m█████████    \033[91m╼╩≑═╝║ ═╩╝ ╚≒╝╚══╝╞══╝╩  ╩═╩═╝
                                \033[95m﹋﹋﹋﹋﹋﹋"""
    print "\033[94m▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔"

time.sleep(2)
banner()
time.sleep(0.5)
load()
os.system("sh h.sh")
("sh h.sh")
