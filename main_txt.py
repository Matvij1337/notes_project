from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QInputDialog
app = QApplication([])
from notes import *

notes = []

def show_note():
    key = list_notes.selectedItems()[0].text()
    for note in notes:
        if note[0] == key:
            Large_area_for_notes.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])
list_notes.itemClicked.connect(show_note)

def add_note():
    note_name, ok = QInputDialog.getText(window, "Додати замітку", "Назва замітки")
    if ok and note_name != "":
        note = [note_name, '', []]
        notes.append(note)
        list_notes.addItem(note[0])
        list_tags.addItems(note[2])
        with open(str(len(notes)-1)+".txt", "w", encoding='utf-8') as file:
            file.write(note[0]+'\n')
btn_create_note.clicked.connect(add_note)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = Large_area_for_notes.toPlainText()
                with open(str(index)+".txt", "w", encoding='utf-8') as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    for tag in note[2]:
                        file.write(tag+' ')
                    file.write('\n')
            index += 1
    else:
        print("Замітка для збереження не вибрана!")
btn_save_note.clicked.connect(save_note)

name = 0
note = []
while True:
    filename = str(name)+".txt"
    try:
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                line = line.replace('\n', '')
                note.append(line)
        tags = note[2].split('/')
        note[2] = tags

        notes.append(note)
        note = []
        name += 1

    except IOError:
        break

    
print(notes)
for note in notes:
    list_notes.addItem(note[0])

window.show()
app.exec_()