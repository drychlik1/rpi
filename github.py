#### Sprawdź czy jest GIT
git --version
git config --global user.name "drychlik1"
git config --global user.email "damian.rychlik1@gmail.com"

#### Sprawdź połączenie
config --list
git status
#### Operacje na plikach
git add index.css             # Dodaj
git add *                     # dodaj pliki, których nie ma
git rm --cached index.css     # Uswanie pliku
git commit                    # Zapisz zmiany lokalnie 
  git comit -m "Aktualizacja" # Komentarz dla innych
  git comit -a                # Zatwierdzenie zmian w migawce
  git comit --amend           # Dodaje zmiany do obecnego zatwierdzenia
git push                      #! Aktualizacja lokalne>zdalne

######## Repoztyrium github.com dla 
mkdir rpi                     # Utwórz katalog demo
cd rpi                        # przejdź

git init                      # Inicjalizacja repo na /home/pi/rpi/.git/
ls - la                       # widać .git folder
nano README.md                # O czym jest repozytorium
git status                    # Tu powinien być widoczny status zatwierdzeń
git add README.md             # Dodaj do poczekalni 
git remote add origin https://github.com/drychlik1/nazwapliku.git
git remote -v                 # Ustawienie połączenia
git push origin master        # Dodajemy do repozytoriuum zdalnego 

### Więcej info:  https://docs.github.com/en
