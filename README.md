# PythonSocksChat
- Simple socks base application.

# ℹ️ Anleitung: Installtion und Nutzung ℹ️

🌟Folgende Anleitung ist für die einfach Nutzung. Weiter unten findest du die Anleitung zum selber bauen! 🌟

## ❓ Was brauche ich?

- WinRar (gibt es [hier](https://www.heise.de/download/product/winrar-1380/download))
- Das eigentlich Programm (gibt es [hier](https://github.com/sera619/PythonSocksChat/releases/download/v1.0.5/Chat_winX64.rar))
Das war es schon.

## ❓ Okay, ich habe WinRar und das Programm.

- Entpacke das WinRar Verzeichnis in dein Verzeichnis deiner Wahl.
- Öffne das eben entpackte Verzeichnis dort findest du 2 .exe
- Starte den Server immer als erstes! (PyhtonChatServer.exe)
- Starte die PythonChatClient.exe (der eigentliche "Chat")
- gebe einen Nutzernamen ein den du gerne verwenden möchtest
- Starte eine 2. PythonChatClient.exe und wähle auch hier einen Nutzernamen
- Fertig beide Clienten koennen nun über den Server kommunizieren

# ℹ️ Anleitung: Do it yourself! ℹ️

🌟 Folgende Anleitung ist zum selber machen. Hier braucht es etwas mehr. 🌟
📺 🎬 [YouTube Video](https://www.youtube.com/watch?v=H01qDY6g914) zur Anleitung. 

## ❓ Was brauche ich?

- Python ( ❗ Stelle sicher das du beim installieren das Häkchen bei "Python zum System PATH hinzufügen" gesetzt hast ❗ )
- IDE (Microsoft Visual Studio Code) (IDE = integrated development environment = integrierte Entwicklungsumgebung = Der Editor zum Bearbeiten des Codes.)
- Unter Windows: Kommandokonsole | Unter Linux/OS: Terminal

## ❓ Okay, installiert und nun?

Windows:
- Lade dir von dieser Seite die .zip herunter (grüner Button am seiten Anfang)
- Entpacke diese ZIP-Datei in ein Verzeichnis deiner Wahl (BSP: C:/User/<DEIN BENUTZERNAME>)
- Öffne Visual Studio Code
- Klicke dort in der linken unteren Bildecke auf das Zahnrädchen und wähle "Extensions" aus
- Gebe im Suchfeld des sich gerade geöffneten Fensters "Python" ein und installiere die oberste Extension
- Warte einen Moment je nach System kann die Installation einen moment dauern
- (Unten Ecke links findest du eine Glocke wenn du darauf klickst kannst du sehen ob die IDE noch etwas tut)
- Klicke auf File im oberen Fenstermenü und wähle "open Folder" - Gebe dort das Verzeichnis der heruntergeladenen Datei an
- Nun kannst du im Fileexplorer von Studio Code die beiden Scripte im Ordner "src/script/ ClientPyChat.py | ServerPyChat.py öffnen 

## ❓ Ja und wie starte ich das Ding?

- Öffne das Verzeichnis im Explorer
- Öffne im Verzeichnis den Ordner "script"  (Pfad '../src/srcipt')
  🚨 ---- MARKIERUNG ---- 🚨
- Halte Shift gedrückt und Rechtsklicke mit der Maus in einen freien Bereich im Ordner
- Wähle hier "Powershell Fenster öffnen"
- in der PowerShell 'cmd' eintippen und mit Enter bestätigen
- (damit öffnen wir die Kommandokonsole und können Python direkt ansprechen)
- Wichtig SERVER Skript immer zuerst ausführen und laufen lassen!
- in der Kommandokonsole: 'python ClientPyChat.py' eingeben und mit Enter bestätigen
- Im Anschluss den Client starten dazu einfach die Schritte ab der Markierung wiederholen
- Nun python ClientPyChat.py eingeben
- Hier kann man nun einen 'Nickname' eingeben
- Auf der Server Konsole muss jede neue eingehende Verbindung einmal mit Enter bestätigt werden.
- Um nun Chatten zu können braucht es 2 Clients auf 1 Server somit nocheinmal eine neue Konsole und ab der Makierung nocheinmal
- Wenn beide Clients beim server bestätigt sind können sie nun mit einander schreiben mit gewohnten Chateingaben

*work in progress*
