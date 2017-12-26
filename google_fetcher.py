import google
import imp
reload(google)
  
def fetch_url(filePath):
        with open(filePath, "r") as ins:
                for line in ins:
                        line = line[:-1]
                        google.search('"' + line + '"', stop=1)

fetch_url("/mnt/c/Users/Kamil/OneDrive/Dokumenty/Praca magisterska/Skrypt/relational_databases.txt")
fetch_url("/mnt/c/Users/Kamil/OneDrive/Dokumenty/Praca magisterska/Skrypt/non-relational_databases.txt")

