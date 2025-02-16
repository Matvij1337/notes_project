from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QInputDialog
app = QApplication([])
from notes import *

import json

notes = {
    "Вигравання детей в роблоксе" : {
        "Текст" : "випити чаю",
        "Теги" : ["Англієць", "Великобританія"]
    },
}

def show_notes():
    key = list_notes.selectedItems()[0].text()
    Large_area_for_notes.setText(notes[key]["Текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["Теги"])
list_notes.itemClicked.connect(show_notes)

def add_note():
    note_name, ok = QInputDialog.getText(window, "Додати замітку", "Назва замітки")
    if ok and note_name != "":
        notes[note_name] = {"Текст" : "", "Теги" : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["Теги"])
btn_create_note.clicked.connect(add_note)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["Текст"] = Large_area_for_notes.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file)
    else:
        print("Замітка для збереження не вибрана!")
btn_save_note.clicked.connect(save_note)

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        Large_area_for_notes.clear()
        list_notes.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file)
    else:
        print("Замітка для вилучення не обрана!")
btn_remove_note.clicked.connect(del_note)

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = ln_ed_tag.text()
        if not tag in notes[key]["Теги"]:
            notes[key]["Теги"].append(tag)
            list_tags.addItem(tag)
            ln_ed_tag.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file)
    else:
        print("Замітка для додавання тега не обрана")
btn_add_too_notes.clicked.connect(add_tag)

def del_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["Теги"].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]["Теги"])
        with open('notes_data.json', "w") as file:
            json.dump(notes, file)
btn_unconnect_of_notes.clicked.connect(del_tag)

def search_tag():
    tag = ln_ed_tag.text()
    if search_notes_by_tags.text() == "Шукати замітки за тегом" and tag:
        notes_filtered = {} 
        for note in notes:
            if tag in notes[note]["Теги"]:
                notes_filtered[note] = notes[note]
        search_notes_by_tags.setText("Скинути пошук")
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
    elif search_notes_by_tags.text() == "Скинути пошук":
        ln_ed_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        search_notes_by_tags.setText("Шукати замітки по тегу")
search_notes_by_tags.clicked.connect(search_tag)

#with open("notes_data.json", "w", encoding='utf-8') as file:
    #json.dump(notes, file)

with open("notes_data.json") as file:
    notes = json.load(file)
list_notes.addItems(notes)

window.show()
app.exec_()