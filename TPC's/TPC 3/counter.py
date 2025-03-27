import time
from graphics import *

print("Posso contar as palavras de um text!")
time.sleep(1.5)
input("Press Enter to continue...")
print(f"A frase tem {len(input("Introduza a frase que pretende: ").split())} palavras")
