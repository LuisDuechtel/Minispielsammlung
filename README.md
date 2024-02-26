<!-- https://github.com/skills/communicate-using-markdown -->

Martrikelnummern:
- 8595958
- 6812340
- 3844189

# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)

Prozedurale Programmierung besteht aus folgenden grundlegenden Elementen:
- Funktionen
- Variablen 
- Kontrollstrukturen (Schleifen und Abfragen)
- Algorithmenbeschreibung
- Datentypen
- E/A-Operationen und Dateiverarbeitung
- Operatoren
- Stringverarbeitung
- Strukturierte Datentypen

In unserem Python-Projekt haben wir unser gelerntes Wissen über die Programmierung angewendet und alle Elemente verwendet. Im Folgenden sind paar Beispiele aus dem Code auflistet.

### Funktionen:
Es wurden Funktionen im Code verwendet, damit man den Code leichter lesen kann und er strukturierter ist. Zusätzlich kann eine Funktion öfters in einem Programmdurchlauf aufgerufen werden.
Da z.B. im Spiel Hangman weiter Wörter erraten möchte, haben wir ein Button "Neues Spiel" eingebaut. Dieser Button führt eine Variable aus die Variablen zurücksetzt, damit man ein neues Spiel starten kann.

![Funktionen](/screenshots/Funktionen_Frage_1.png)

### Variablen:

In dem folendem Bild aus dem Code "Hangman_V2.py" sieht man gut das Variablen verwendet deklariert worden sind.

Zusätzlich wurde das Schlüsselwort "global" verwendet, da die Variable in einer Funktion deklariert worden ist. Durch "global" ist die Variable nicht nur lokal ind er Funktion sondern auch außerhalb der Funktion aufrufbar ist.

![Variablen](/screenshots/Variablen_Frage_1.png)

### Kontrollstrukturen (Schleifen und Abfragen):
Kontrollstrukturen beinhalten zum Beispiel For-Schleifen und If-Abfragen.
Im folgenden Bild wurde eine Schleife und Abfrage verwendet um zu überprüfen ob der eingegebe Buchstaben im gesuchten Wort vorhanden ist. Da ein Buchstabe mehrfach vorhanden sein kann benötigt man eine Schleife.

![For-Schleife_und_If-Abfrage](/screenshots/For_Schleife_Frage_1.png)

### Algorithmenbeschreibung
In dem folgender Funktion wird ein Wort für das Hangman-Spiel ausgesucht.
Die Wörter die verwendet werden können, stehen in der Liste die in dem Code eingelesen wurde. Die Wörter der eingelesen Liste stehen in der Variable "data". 
- Zuerst werden die Zeilen der Datei abefragt (Pro Zeile ist ein Wort).
- Danach wird mit random.randint eine zufälligen Index herausgesucht 
- Dieser zufälliger Index wird in der Liste abgefragt. Das entspricht dem Wort.
- Als nächstes wird das Wort in Großbuchstaben umgewandelt.
- Bei return Hangman_word wird die Variable wieder aus der Funktion ausgegben.

![Algo_beschreibung](/screenshots/Choose_Word_Frage1.png)

### Datentypen
In unserem Python Projekt wurden die typischen Datentypen verwendet wie z.B.:
- Listen
- Strings
- Integer

### E/A-Operationen und Dateiverarbeitung
Ein und Ausgabe wurde ebenfalls im Projekt verwendet.
Eingabe ist z.B.: über Buttons bei Hangman, damit man Buchstaben auswählen kann.
Ausgabe wurde zum Beispiel mit Labels umgesetzt. Wenn ein Spiel gewonnen / verloren wurde gibt es eine Ausgabe mit einem Label.

![Ausgabe](/screenshots/Ausgabe_Frage1.png)

### Operatoren
Operatoren wie zum Beispiel das Hochzählen mit einer Addition wurden oft verwendet:
z.B.: index_counter += 1


### Stringverarbeitung
Im Folgenden Code, wird ein "Underscore_String" erstellt. Der Underscore_String sieht zuerst nur so aus "____" Durch das "join" werden Leerzeichen hinzugefügt "_ _ _ _"
```
    Underscore_String = ["_"] * Len_word
    Word_with_blanks = " ".join(Underscore_String)

```

### Strukturierte Datentypen
Im Projekt wurden viele Listen verwendet zum Beispiel im Code von Schere-Stein-Papier
```
    choices = ["Schere", "Stein", "Papier"]
```

# Sie können die Syntax und Semantik von Python (10)
Worauf ich stolz bin ist die Tastatur-GUI.
Durch die For-Schleife und ascii_uppercase wurde eine Tastatur mit Buttons gebaut.
Wenn ein Button ausgewählt wird, wird eine Funktion ausgeführt, die den Buchstaben im gesuchten Wort prüft.
Durch den Button "Neues Spiel" wird die Funktion "new-Game" ausgeführt und das Spiel wird mit einem neuen Wort gestartet.

![Tastatur+Button](/screenshots/Buttons_Frage_1.png)


# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
Das Projekt wurde mit Luis Düchtel (LuisDuechtel) Robin Schuch (WeltraumEnte0) und Philipp Rambacher (PhilippR84) durchgeführt.
Die Idee zur Spielesammlung haben wir durch ChatGPT gefunden. 
Wir sind der Meinung, dass aufgrund der Zeit und unserem Können das Projekt gut gewählt worden ist. 
Wir haben uns dauerhaft oft über Discord kommuniziert, damit jeder auf dem aktuellen Stand ist, wie das Projekt steht.
Zusätzlich haben wir ein gemeinsames GIT-Repo aufgebaut.
Das war für uns alle neu, da wir bisher noch nicht viel mit GIT gearbeitet haben.
Da jeder an seinem eigenen Teil-Projekt arbeiten konnte, ohne jemand anderen zu stören haben wir nicht viel commited sondern eher lokal gearbeitet. 
Trotzdem haben wir wenn wir uns besprochen haben oder Probleme hatten unseren aktuellen Stand auf Git gepusht.
Im folgedem sieht man ein Ausschnitt aus GIT:

![GIT_Commits](/screenshots/GIT_Commits_Frage_1.png)


# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->

Der folgende Codeausschnitt aus unserem Hangman Game der Spielesammlung ist einer der coolsten im Projekt. Die verschachtelten if-Statements haben ihre Zeit in Anspruch genommen, bis alles so funktioniert hat, wie es soll. Jetzt funktionert aber alles und ich habe alles in der Funktion "make_guess" zusammengeführt. Sie nimmt den Buchstaben vom Benutzer entgegen und prüft, ob er im Wort enthalten ist. Wenn ja, aktualisiert sie die Anzeige des Wortes mit den richtigen Buchstaben. Wenn nicht, erhöht sie den Versuchszähler und zeigt das nächste Bild des Galgenmännchens an. Am coolsten ist, dass sie auch überprüft, ob das Wort vollständig erraten wurde, und dann die passende Meldung ausgibt – entweder "Gewonnen!" oder "Verloren!". Das ist die wichtigste Logik im Spiel und hat viel Spaß gemacht zu coden. Dieser Abschnitt ist auch während einer unserer Discord Calls in Zusammenarbeit entstanden. Daher ist diese Stelle für mich/uns auch eine der coolsten.

```code
def make_guess(Letter):
    global correct_guess, int_versuche, Underscore_String, Word_with_blanks
    Word_without_blanks = ""
    if int_versuche < 11:
        if Letter in Hangman_Word:
            index_counter = 0
            for One_Letter in Hangman_Word:
                if One_Letter == Letter:
                    correct_guess += 1
                    Underscore_String[index_counter] = Letter
                index_counter += 1
            Word_with_blanks = " ".join(Underscore_String)
            word_label.config(text=Word_with_blanks)
            Word_without_blanks = Word_with_blanks.replace(" ", "")
            
        else:
            int_versuche += 1
            imgLabel.config(image=photos[int_versuche])
        
        if Word_without_blanks == Hangman_Word:
            pygame.mixer.music.play()
            messagebox.showinfo("Gewonnen!", f"Herzlichen Glückwunsch! Du hast das Wort '{Hangman_Word}' richtig erraten.")
    
    else:
        messagebox.showinfo("Verloren!", f"Du hast das Wort: '{Hangman_Word}' NICHT erraten.")

```


## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->

<!-- GIT -->
It was the first time using git for all of us. At the beginning it took some time to get used to commiting and pulling in VS Code. But after we figured that out, git is a really cool tool to organize your code. Way better than just sending zip. files over discord the whole day long...(was terrible)
https://github.com/LuisDuechtel/Minispielsammlung
<!-- VSC -->
I've used other IDEs like Eclipse before, but VS really convinced me to continue using it. VS Code is way easyer to handle and I quite like the minimalistic and simple design. You're always just seeing the windows and informations you want to see, nothing of the unnecessary stuff.
![alt text](/screenshots/vs_code.png)
<!-- Copilot -->
We got some problems with the registration process for the GitHub Copilot...But we found another really good AI for coding. 
It's called tabnine, and the way how it works is pretty much the same. You got a very percise auto completion, which helps a lot in repetitive things. For example, when coding all the different winning combinations for TicTacToe you start tipping the first 2 and get the rest suggested. That's a huge advantage, because the code is kind of redundant but you would need to change the list indixes all the time. This step is completely done by the ai. You just check in the end if everything's working and correct. This saves a lot of time, when writing many lines of code.
![alt text](/screenshots/tabnine_ai.png)
<!-- other -->
ChatGPT
We used ChatGPT for getting information about how to write better and more effective code. For example, we asked chat when we had our code on how to push the performance and make it more efficient. Also ChatGPT's really good for asking about, how to implement a certain functionality or how to properly use Tkinter. (chat is quite helpful for Tkinter, but we still despaired sometimes...) :D


## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->
Our main goal was to work close together in our team, so we solved most of the problems while our Discord coding-sessions. But we had some problems where we weren't able to solve in our group or nobody was available so we had a good exchange with other groups aswell. Was interesting to see what kinds of problems and challenges other teams are facing during der projects.
![alt text](/screenshots/support_message.png)

![Philipp_Support_Message](/screenshots/Philipp_Support_Message.png)

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->



## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->



## Kenntnisse in prozeduraler Programmierung:

# - Algorithmenbeschreibung

# - Datentypen

# - E/A-Operationen und Dateiverarbeitung

# - Operatoren

# - Kontrollstrukturen

# - Funktionen

# - Stringverarbeitung

# - Strukturierte Datentypen

