import GUI
from PySide6 import QtCore

def test_entry_selected(qtbot):
    window = GUI.WuFooEntriesWindow()
    window.show
    qtbot.addWidget(window)
    row = 9
    target_item = window.list_control.item(row)
    rectangle = window.list_control.visualItemRect(target_item)
    click_point = rectangle.center()
    qtbot