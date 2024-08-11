# Side Chat with Bots over Tools etc.

## Ich:

Ich habe einen Chatverlauf mit ChatGPT im Markdown Format (siehe Anlage). Ich möchte daraus entweder a) eine Sammlung von html Dateien erstellen.
Der Chatverlauf hat immer eine Überschrift "Ich" und dann eine Antwort vom Bot die mit der Überschrift "Bot" markiert ist. Diese Überschriften wechseln sich ab. Ich stelle mir vor eine fortlaufende Folge von Seiten (in html) zu haben bei der eine Startseite mit dem Titel "Chatverlauf" auf die erste "Ich" Seite verweist. Die "Ich" Seite hat (wie auch alle anderen folgenden Seiten) einen Verweis auf a) die Startseite b) die Folgeseite c) die vorhergehende Seite. Auf die "Ich" Seite folgt immer eine "Bot" Seite die die Antwort des Bots enthält.
Hier der Beispieltext:
``` md
## Ich:
Als Experte für die Steuerung automatischer Anwendungen in Python möchte ich Sie um Ihre Hilfe bei der Entwicklung von zwei privaten Projekten bitten. Bitte geben Sie für jedes Projekt eine detaillierte Beschreibung der gewünschten Funktionalität, der technischen Anforderungen und der spezifischen Unterstützung, die Sie benötigen. Projekt 1: Verwaltung von Dokumenten (PDF, Word, Bilder)- Entwickeln Sie eine KI-basierte Oberfläche, mit der Sie eine Sammlung von Dokumenten wie Rechnungen, Kontoauszüge, Bedienungsanleitungen und interessante Artikel durchsuchen und abrufen können.- Ermöglichen Sie Abfragen wie "Zeige mir alle Rechnungen von Amazon aus dem Jahr 2023" oder "Finde die Bedienungsanleitung für meine Waschmaschine".- Beschreiben Sie detailliert, wie Sie die Dokumente derzeit kategorisieren und beschriften, z.B. durch Verwendung der ChatGPT-API. Erläutern Sie genau, wo Sie Unterstützung benötigen, um eine effiziente Suche und Abruffunktion zu implementieren.- Geben Sie an, welche Technologien, Tutorials oder Ressourcen Sie für die Umsetzung dieses Projekts für hilfreich erachten. Projekt 2: Verwaltung von Familienfotos- Entwickeln Sie eine KI-basierte Lösung, mit der Sie eine große Sammlung von über 10.000 Familienfotos durchsuche (... more)
```
## Bot
Um den Chatverlauf in eine Sammlung von HTML-Dateien zu konvertieren, können wir ein Python-Skript erstellen, das den Markdown-Text liest, die Seiten entsprechend strukturiert und die Navigation zwischen den Seiten ermöglicht. Hier ist ein Beispielskript, das dies erreicht:

1. Installiere die benötigten Bibliotheken:
   ```bash
   pip install markdown2
   ```

2. Erstelle das Python-Skript:

   ```python
   import markdown2
   import os

   # Funktion zum Konvertieren von Markdown zu HTML
   def markdown_to_html(markdown_text):
       return markdown2.markdown(markdown_text)

   # Funktion zum Erstellen der HTML-Seiten
   def create_html_pages(chat_markdown):
       pages = []
       lines = chat_markdown.split('\n')
       current_page = ""
       for line in lines:
           if line.startswith('## Ich:') and current_page:
               pages.append(current_page)
               current_page = line
           else:
               current_page += f"\n{line}"
       pages.append(current_page)

       if not os.path.exists('chat_pages'):
           os.makedirs('chat_pages')

       start_page = """
       <!DOCTYPE html>
       <html>
       <head>
           <title>Chatverlauf</title>
       </head>
       <body>
           <h1>Chatverlauf</h1>
           <a href="chat_pages/page1.html">Start</a>
       </body>
       </html>
       """
       with open('index.html', 'w', encoding='utf-8') as f:
           f.write(start_page)

       for i, page in enumerate(pages):
           if page.startswith('## Ich:'):
               page_type = 'Ich'
           elif page.startswith('## Bot:'):
               page_type = 'Bot'
           else:
               continue

           html_content = markdown_to_html(page)
           prev_page = f"page{i}.html" if i > 0 else "../index.html"
           next_page = f"page{i+2}.html" if i < len(pages) - 1 else "../index.html"

           html_page = f"""
           <!DOCTYPE html>
           <html>
           <head>
               <title>Chat Page {i+1}</title>
           </head>
           <body>
               {html_content}
               <div>
                   <a href="../index.html">Startseite</a> |
                   <a href="{prev_page}">Vorherige Seite</a> |
                   <a href="{next_page}">Nächste Seite</a>
               </div>
           </body>
           </html>
           """

           with open(f'chat_pages/page{i+1}.html', 'w', encoding='utf-8') as f:
               f.write(html_page)



``` md
   # Beispiel-Chatverlauf im Markdown-Format
   chat_markdown = """
   ## Ich:
   Als Experte für die Steuerung automatischer Anwendungen in Python möchte ich Sie um Ihre Hilfe bei der Entwicklung von zwei privaten Projekten bitten. Bitte geben Sie für jedes Projekt eine detaillierte Beschreibung der gewünschten Funktionalität, der technischen Anforderungen und der spezifischen Unterstützung, die Sie benötigen. Projekt 1: Verwaltung von Dokumenten (PDF, Word, Bilder)- Entwickeln Sie eine KI-basierte Oberfläche, mit der Sie eine Sammlung von Dokumenten wie Rechnungen, Kontoauszüge, Bedienungsanleitungen und interessante Artikel durchsuchen und abrufen können.- Ermöglichen Sie Abfragen wie "Zeige mir alle Rechnungen von Amazon aus dem Jahr 2023" oder "Finde die Bedienungsanleitung für meine Waschmaschine".- Beschreiben Sie detailliert, wie Sie die Dokumente derzeit kategorisieren und beschriften, z.B. durch Verwendung der ChatGPT-API. Erläutern Sie genau, wo Sie Unterstützung benötigen, um eine effiziente Suche und Abruffunktion  .... more, I stopped the bot
```
