#!/usr/bin/env python3
# MaskURL
# By: Euronymou5

from colorama import Fore
import os
import pyshorteners
import time

logo = f"""
{Fore.BLUE}╔╦╗┌─┐┌─┐┬┌─{Fore.RED}╦ ╦╦═╗╦  
{Fore.BLUE}║║║├─┤└─┐├┴┐{Fore.RED}║ ║╠╦╝║  
{Fore.BLUE}╩ ╩┴ ┴└─┘┴ ┴{Fore.RED}╚═╝╩╚═╩═╝
  {Fore.BLUE}By: {Fore.LIGHTRED_EX}Euronymou5
"""

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

s = pyshorteners.Shortener()

def menu():
    clear()
    print(logo)
    
    url = input(f'\n{Fore.YELLOW}[>] Ingresa la url: ')
    if "https://" or "http://" in url:
       try:
          try:
            ey = s.isgd.short(url)
          except:
            print(f'{Fore.RED}\n[!] Ha ocurrido un error al intentar cortar la url.')
            time.sleep(2)
            menu()
          mod = input(f'\n{Fore.YELLOW}[>] Ingresa el dominio que quieres suplantar (https://google.com): ')
          print(f'\n{Fore.CYAN}[~] Ejemplo: seguidores-gratis-instagram')
          word = input(f'\n{Fore.YELLOW}[>] Ingresa palabras de ingenieria social separadas con "-": ')
          ey = ey.replace("https://", "")
          print(f'\n{Fore.GREEN}[#] Link acortado: {mod}-{word}@{ey}')
       except KeyboardInterrupt:
          print(f'\n{Fore.RED}[!] Saliendo del programa')
          time.sleep(2)
          exit()
    else:
        print(f'{Fore.RED}\n[!] Error la url debe de contener "http://" o "https://"')
        time.sleep(2)
        menu()

if __name__ == "__main__":
    menu()
