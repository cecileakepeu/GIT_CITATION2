from random import choice
from pyfiglet import figlet_format
from rich import print

with open("citations.txt", "r", encoding="utf-8") as f:
    citations = f.readlines() #citations devient une liste 
#f est un objet de type text
#f detecte nos readlines 
citations = [c.strip() for c in citations] #citation tu mets a l'interieur tu fabriques une liste et a l'interieur des comprehension de liste #cstrip enleve tous les espaces en trop et fabrique une nouvelle liste avec chacune de mes phrases nettoyer
citation = choice(citations) #choice est fait par random j'ai une liste de valeur tu lances une au hasard

print(figlet_format("Citation")) #citation tirer au hasard mit en cian 
print(f"[cyan]{citation}[/cyan]")

