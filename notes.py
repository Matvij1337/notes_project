from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit,
    QTextEdit, QListWidget, QPushButton,
    QHBoxLayout, QVBoxLayout
)

window = QWidget()

window.resize(900, 600)
window.setWindowTitle("Замітки")

lbl_list_note = QLabel('Список заміток')

list_notes = QListWidget()

btn_create_note = QPushButton("Створити замітку")
btn_remove_note = QPushButton("Видалити замітку")

h1 = QHBoxLayout()

h1.addWidget(btn_create_note)
h1.addWidget(btn_remove_note)

btn_save_note = QPushButton("Зберегти замітку")

lbl_list_tag = QLabel("Список тегів")

list_tags = QListWidget()

ln_ed_tag = QLineEdit()

btn_add_too_notes = QPushButton("Додати до замітки")
btn_unconnect_of_notes = QPushButton('Відкрипити від замітки')

h2 = QHBoxLayout()

h2.addWidget(btn_add_too_notes)
h2.addWidget(btn_unconnect_of_notes)

search_notes_by_tags = QPushButton("Шукати замітки за тегом")

v_main = QVBoxLayout()

v_main.addWidget(lbl_list_note)
v_main.addWidget(list_notes)
v_main.addLayout(h1)
v_main.addWidget(btn_save_note)
v_main.addWidget(lbl_list_tag)
v_main.addWidget(list_tags)
v_main.addWidget(ln_ed_tag)
v_main.addLayout(h2)
v_main.addWidget(search_notes_by_tags)

Large_area_for_notes = QTextEdit()

for_large_area = QHBoxLayout()

for_large_area.addWidget(Large_area_for_notes)

h_main = QHBoxLayout()

h_main.addLayout(for_large_area, stretch = 2)
h_main.addLayout(v_main, stretch = 1)

window.setLayout(h_main)