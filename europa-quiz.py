WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10

q1 = ["Welche Altersklasse bist du?",
      "Erwachsener", "Kind", "-", "-"]

q2 = ["Was ist die Haupstadt von England ...?",
      "London", "Mallorca", "Hello", "Paris", 1]

q3 = ["Welches Land ist in Rom ...?",
      "Korsika", "Vatikanstaat", "Nigeria", "Rom", 2]

q4 = ["Wo steht der schiefe Turm?",
      "Mailand", "Pisa", "Florenz", "Rom", 2]

q5 = ["Wo ist das Morgarten Denkmal?",
      "Oberägeri", "Deutschland", "Tacos", "Links", 1]

q6 = ["Was ist die Hauptstadt von Grichenland?",
      "Oslo", "Athen", "Istambul", "Ankara", 2]

q7 = ["Was ist die Hauptstadt von Ankara?",
      "Ankara ist schon die Hauptstadt", "Holland", "Niederlande", "Ungarn", 1]

q8 = ["Wo ist der Placa Mayor?",
      "Madrid", "Rom", "Paris", "Dublin", 1]

q9 = ["Dublin ist die Hauptstadt von ...?",
      "Spanien", "Niederlande", "England", "Republik Irland", 4]

q10 = ["Ist Iceland in Europa?",
      "Ja", "Nein", "-", "-", 1]

q11 = ["Es gab mal das Reich Oesterreich-Unganrn.",
       "Ja", "Nein", "-", "-", 1]

q12 = ["Welches Europäsche Land hat keine Hauptstadt?",
       "Luxemburg", "Fürstemtum Lichtenstein", "Albanien", "Mazedonien", 2]

q13 = ["Oslo ist die Haupstadt von Norwegen.",
       "Richtig", "Falsch", "-", "-", 1]

q14 = ["Liegt Grönland in Europa?",
       "Ja", "Nein", "Gönland gehört zu Dänemark, ist aber auf der Nordamerikanischen Platte", "-", 3]

q15 = ["Welcher Sänger kommt aus der Schweiz?",
       "Manni Mather", "Mark Foster", "Capital Bra", "SIDO", 1]

q16 = ["Die Hauptstadt von der Ukraine ist?",
       "Bern", "Kiew", "Ankara", "Moskau", 2]

q17 = ["Aus welchem Land kommt Wilhem Tell?",
       "Deutschland", "Österreich", "Schweiz", "Holland", 3]

q18 = ["Am Morgarten Denkmal haben Schweizer gegen ... gekämpft?",
       "Deutsche", "Niederländer", "Franzosen", "Österreicher", 4]

q19 = ["Robin Hood kam aus ...?",
       "dem UK", "der Republik Irland", "-", "-", 1]

q20 = ["König arthur war König von ...?",
       "Schottland", "Nord Irland", "England", "Wales", 3]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]
question = questions.pop(0)

def draw():
    screen.fill("dim grey")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1

def altersklasse():
    global altersklasse
    altersklasse = age.group  
    if altersklasse:
          if kind.collidepoint(pos):
                screen.draw.questions[q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
          elif erwachsener.collidepoint(pos):
                screen.draw.questions[q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]

def game_over():
    global question, time_left
    message = "Ende. Du hast %s Fragen richtig" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def correct_answer():
    global question, score, time_left

    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10

    else:
        print("Das isch ja super gsi!")
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Du hast angeklickt:" + str(index))
            if index == question[5]:
                print("Das isch ja MEGA he!")
                correct_answer()
            else:
                game_over()
        index = index + 1

def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)
