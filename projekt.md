# Abschlussprojekt  
  
## Aufgabenstellung
[deutsch](https://htmlpreview.github.io/?https://github.com/ue-basismodul-ws2021/ue-basismodul-ws2021.github.io/blob/main/projekt_de.html)  
[english](https://htmlpreview.github.io/?https://github.com/ue-basismodul-ws2021/ue-basismodul-ws2021.github.io/blob/main/projekt_en.html)  
  
[Test-Wortliste](wordlist.txt) (10.000 Wörter, UTF-8, sortiert)

## FAQ
- *Ich würde das Projekt gerne zu zweit angehen, habe allerdings noch keinen Partner. Wie kann man das lösen?*  
Ein Hinweis per E-Mail genügt, dann wird der Kontakt zu dem/der nächsten hergestellt, der/die sich ebenfalls noch einen Partner wünscht.
- ***Daciuk***: *Ich habe den Algorithmus exakt nachprogrammiert, aber der Startzustand ist am Ende nie Teil des Registers. Was mache ich falsch?*  
Das ist im Algorithmus auch so vorgesehen. Ob der Startzustand im Register liegt oder nicht, ist unerheblich, da er immer eine eigene Äquivalenzklasse bildet und nicht weiter minimiert werden kann.
- ***Ausgabe der Sprache des Automaten***: *Darf man auch einfach die ursprüngliche Wortliste benutzen, um alle Wörter auszugeben?*  
Nein, nur der Automat selbst soll verwendet werden, um die Wörter zu generieren. Außerdem ist die langfristige Speicherung der Wortliste generell keine gute Idee, da wir den Automaten ja implementieren, um genau diesen Speicherplatzverbrauch zu reduzieren.
- ***Perfect Hashing***: *Wie soll das Programm reagieren, wenn der Nutzer eine Meta-Information zu einem Wort speichern will, das nicht Teil der Sprache des Automaten ist?*  
Dann soll genau das ausgegeben werden, nämlich dass der Lookup fehlgeschlagen ist.
- ***Kombination Perfect Hashing/Speichern und Laden***: *Muss die Hash-Tabelle mit den Meta-Informationen ebenfalls abgespeichert werden?*  
Nein, die Hash-Tabelle muss für das Bestehen der Aufgabe nicht abgespeichert werden. Dann muss sie aber ggfs. neu erstellt werden, wenn man das MinDict aus einer Datei lädt.
- ***argparse***: *Ich frage in meinem Programm alle Nutzereingaben während der Laufzeit ab. Ist es trotzdem Pflicht, argparse zu verwenden?*  
Wenn es keine Kommandozeilenargumente gibt, die geparsed werden müssen, kann selbstverständlich auf argparse verzichtet werden. Die Verwendung des ArgumentParsers ist ohnehin kein Teil der Anforderung, sondern vielmehr eine Hilfestellung.
