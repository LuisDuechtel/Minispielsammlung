# Flappy Bird Game Code Review

## Prozedurale Programmierung in Python - Flappy Bird Spiel

Dieser Code implementiert das Flappy Bird Spiel in Python unter Verwendung der Pygame-Bibliothek. Hier sind einige Punkte zur Überprüfung und Verbesserung:
Link zum GitHub der Gruppe: https://github.com/ActiveClientMods/Flappybird-Projekt

### Grundelemente der prozeduralen Programmierung
- **Funktionen:** Der Code verwendet Funktionen, um bestimmte Aufgaben zu erfüllen, z. B. die `draw_text`-Funktion für die Anzeige von Text auf dem Bildschirm. Dies fördert die Wiederverwendbarkeit und Lesbarkeit des Codes.
  
  Beispiel:
  ```
  def draw_text(text, font, text_col, x, y):
      img = font.render(text, True, text_col)
	    screen.blit(img, (x, y)) ```

### Syntax und Semantik von Python
- **Klassen und Objekte**: Der Code verwendet Klassen, um Objekte wie den Vogel (Bird), die Rohre (Pipe), die Schaltfläche (Button) und das Game-Over-Bild (game_over_img_cl) zu repräsentieren. Dies fördert eine strukturierte Programmierung.

Beispiel:
```
class Bird(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for num in range(1, 4):
			img = pygame.image.load(f"images/bird{num}.png")
			self.images.append(img)
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.vel = 0
		self.clicked = False

	def update(self):
		if flying == True:
			# apply gravity
			self.vel += 0.9
			if self.vel > 8:
				self.vel = 8
			if self.rect.bottom < 768:
				self.rect.y += int(self.vel)

		if game_over == False:
			# jump
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				self.vel = -9
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False
			if pygame.key.get_pressed()[K_SPACE] == 1 and self.clicked == False:
				self.clicked = True
				self.vel = -9
			if pygame.key.get_pressed()[K_SPACE] == 0:
				self.clicked = False
			# handle the animation
			flap_cooldown = 5
			self.counter += 1

			if self.counter > flap_cooldown:
				self.counter = 0
				self.index += 1
				if self.index >= len(self.images):
					self.index = 0
				self.image = self.images[self.index]
			# rotate the bird
			self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
		else:
			# point the bird at the ground
			self.image = pygame.transform.rotate(self.images[self.index], -90)
```

### Datenstrukturen und deren Anwendung
- **Sprite-Gruppen:** Der Code organisiert Vogel- und Rohr-Objekte in Pygame-Sprite-Gruppen. Dies ermöglicht eine effiziente Verwaltung und Aktualisierung mehrerer Objekte.

Beispiel:
```
pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()
```

- **Liste von Bildern:** Die 'Bird'-Klasse verwendet eine Liste von Bildern, um eine Animationssequenz zu erstellen. Dies zeigt den effektiven Einsatz von Datenstrukturen.

Beispiel:
'''
self.images = []
'''

### Code Beispiele 
Hier werden spezifische Abschnitte im vorliegenden Code hervorgehoben, um verschiedene Aspekte der Implementierung zu veranschaulichen.
- **Animation und Steuerung des Vogels (Bird):**
Die Bird-Klasse enthält Methoden zur Aktualisierung der Position und Animation des Vogels. Dabei wird auf Mausklicks und Tastenanschläge reagiert, um die Flugbewegung des Vogels zu steuern.

Beispiel:
```
def update(self):
		if flying == True:
			# apply gravity
			self.vel += 0.9
			if self.vel > 8:
				self.vel = 8
			if self.rect.bottom < 768:
				self.rect.y += int(self.vel)

		if game_over == False:
			# jump
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				self.vel = -9
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False
			if pygame.key.get_pressed()[K_SPACE] == 1 and self.clicked == False:
				self.clicked = True
				self.vel = -9
			if pygame.key.get_pressed()[K_SPACE] == 0:
				self.clicked = False
			# handle the animation
			flap_cooldown = 5
			self.counter += 1

			if self.counter > flap_cooldown:
				self.counter = 0
				self.index += 1
				if self.index >= len(self.images):
					self.index = 0
				self.image = self.images[self.index]
			# rotate the bird
			self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
		else:
			# point the bird at the ground
			self.image = pygame.transform.rotate(self.images[self.index], -90)
```

- **Rohr-Objekt('Pipe')**
Das Pipe-Objekt repräsentiert ein Rohr im Spiel. Es wird je nach Position (oben oder unten) erstellt und entsprechend der Spiellogik aktualisiert. Die update-Methode steuert die Bewegung der Rohre.

Beispiel:
```
class Pipe(pygame.sprite.Sprite):

	def __init__(self, x, y, position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/pipe.png")
		self.rect = self.image.get_rect()
		#position variable determines if the pipe is coming from the bottom or top
		#position 1 is from the top, -1 is from the bottom
		if position == 1:
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
		elif position == -1:
			self.rect.topleft = [x, y + int(pipe_gap / 2)]


	def update(self):
		self.rect.x -= scroll_speed
		if self.rect.right < 0:
			self.kill()
```
- **Game-Loop und Ereignisverarbeitung**
Die Haupt-Spiel-Schleife (while run) koordiniert die Aktualisierung von Spielobjekten und die Verarbeitung von Ereignissen wie Tastatureingaben. Dieser Abschnitt zeigt die grundlegende Struktur der Spiellogik.

Beispiel:
```
while run:

	clock.tick(fps)
	pygame.display.set_caption("FPS: {:.2f}".format(clock.get_fps()))

	#draw background
	screen.blit(bg, (0,0))

	pipe_group.draw(screen)
	bird_group.draw(screen)
	bird_group.update()

	#draw and scroll the ground
	screen.blit(ground_img, (ground_scroll, 768))

	#check the score
	if len(pipe_group) > 0:
		if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
			and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
			and pass_pipe == False:
			pass_pipe = True
		if pass_pipe == True:
			if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
				score += 1
				pass_pipe = False
	draw_text(str(score), font, white, center_vertical, 20)


	#look for collision
	if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
		game_over = True
	#once the bird has hit the ground it's game over and no longer flying
	if flappy.rect.bottom >= 768:
		game_over = True
		flying = False	


	if flying == True and game_over == False:
		#generate new pipes
		time_now = pygame.time.get_ticks()
		if time_now - last_pipe > pipe_frequency:
			pipe_height = random.randint(-150, 100)
			btm_pipe = Pipe(screen_width * 1.5, center_horizontal + pipe_height, -1)
			top_pipe = Pipe(screen_width * 1.5, center_horizontal + pipe_height, 1)
			pipe_group.add(btm_pipe)
			pipe_group.add(top_pipe)
			last_pipe = time_now

		pipe_group.update()

		ground_scroll -= scroll_speed
		if abs(ground_scroll) > 35:
			ground_scroll = 0
	

	#check for game over and reset
	if game_over == True:
		game_over_img.draw()
		if button.draw():
			game_over = False
			score = reset_game()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				run = False
		if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
			flying = True
		if event.type == pygame.KEYDOWN and flying == False and game_over == False:
			if event.key == pygame.K_SPACE:
				flying = True

	pygame.display.update()
```

### Verbesserungsvorschläge:
- **Kommentare**: Wir empfehlen, zusätzliche Kommentare in komplexeren Abschnitten einzufügen, um den Code für andere Entwickler leichter verständlich zu machen.

- **Dokumentation**: Wir schlagen vor, eine umfassendere Dokumentation für Klassen und Funktionen hinzuzufügen, um ihre Zwecke, Funktionalitäten und Verwendung klar zu erklären.

- **Strukturierte Dateiorganisation**: Die Verbesserung der Lesbarkeit könnte durch eine strukturierte Organisation des Codes in Module oder Klassen erreicht werden. Dies fördert die Klarheit und Verständlichkeit des Gesamtprojekts.

- **Konsistenz**: Es wird darauf hingewiesen, darauf zu achten, dass Variable- und Funktionsnamen konsistent sind und gängigen Konventionen folgen. Dies erleichtert anderen Entwicklern das Verständnis des Codes.

- **Dateipfade**: Es wird empfohlen, relative Pfade oder eine Konfigurationsdatei zu verwenden, um die Verweise auf Bilddateien flexibler zu gestalten. Dies ermöglicht eine reibungslosere Zusammenarbeit und erleichtert die Anpassung des Codes für verschiedene Umgebungen.

  Dieser Code bietet eine solide Grundlage für das Flappy Bird Spiel, und die genannten Verbesserungen könnten die Wartbarkeit und Erweiterbarkeit weiter verbessern.
