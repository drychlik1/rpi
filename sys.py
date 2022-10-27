# PAKIETY
apt-cache policy #LISTA repozytoriów w systemie i hierarchia
#/etc/apt/sources - instrukcje systemu dla pakietów
cat /etc/apt/sources.list
ls /etc/apt/soruces.list.d # Dodatkowe pakiety
sudo nano /etc/apt/soruces.list #Edycja listy - najlepiej komentować listę "#"
sudo apt-get update # Dopiero wtedy nastąpi aktualizacja nowych pakietów

# Czy macos obsługuje wiele sesji terminalowych? 

ls -la # szczegóły plików

pwd # bieżaca ścieżka katalogu
touch test #tworzy plik test 
cat test #wyświetla zawartość test
rm test # usuwa test
rm -rf /folder/ #usuń z plikami
sudo rm -rf /folder/ # gdy uprawnienia nie pozwalają 
mkdir #Utwórz folder
rmdir # zmień nazwę plku
mv /lokalizacja/lok1 /lokalizacja/lok2 #przenieś plik
cp /lokalizacja/lok1 /lokalizacja/lok2 # kopiuj plik
wget #Pobierz 


lsusb # pokaż wszystkie partycje
sudo blkid # info szczeg. o partycjach
sudo fdisk -l # info o dyskach, partycjach i pamięci

#ALIAS - złota rada. Umożliwia zastępowanie długiego polecenia krótkim (aliasem)
## sudo apt-get install -> install
alias -p [nazwa[=wartość] ...] # wartość nie może mieć $1 takich znaków
unalias [-a] [name ...] # nazwa nie może mieć alias/unalias
p - print
a - remove

alias # samo wyświetla listę aliasów
sudo nano /.bash_aliases # /..bash_aliases polecenie uruchamiające, domyślnie /.bash_aliases dodaje do startu aliasy :)
alias c='clear' # Alias C czyści ekran

alias nazwaaliasu=wartość
alias nazwaaliasu='komenda'
alias nazwaliasu='komenda argument1 argument2' 
alias nazwaaliasu='/path/to/script'

#Przykład na aktualizacje systemu
# Alias dla sudo apt update && sudo apt full-upgrade
sudo nano /..bash_aliases
alias aktualizacja='sudo apt update && sudo apt full-upgrade'

# Alias na 4 pakiety ping
alias ping='ping -c 4'

# Jeśli chcesz zachować alias ale skorzystać z pierwotnego polecenia to wpisz;
\ping www.google.pl #odwrotny ukośnik

# Uruchom interfejs graficzny
systemctl show default.target # Pokaż status 
sudo systemctl set-default multi-user.target #Terminal
sudo systemctl set-default graphical.target

#Status usług
service ssh status # sudo - daje szczegóły
sudo service ssh start
sudo service ssh stop
sudo service ssh restart
sudo service ssh reload
sudo service ssh force reload

# Status systemu
systemctl 
systemctl status UNIT.service # UNIT = service, socket, target, device
sudo systemctl start ssh
sudo systemctl stop ssh
sudo systemctl kill ssh

sudo systemctl enable ssh # Automatycznie włączy się w przyszłości
sudo systemctl disable ssh 
systemctl is-enabled ssh # POKAŻ czy włączasz automatycznie
systemctl cat ssh.service # Pokazuje załadowane i aktywne





