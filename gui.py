import PySimpleGUI as sg

layout = [[sg.Text('My Layout', size=(20, 1), pad=((10, 5), (5, 50)))],
          [sg.Input(key='-INPUT-')],
          [sg.Button('OK'), sg.Button('Cancel')]]

window = sg.Window('Minluck Bot Dictionary Updater', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Cancel'):
        break
    if event in ('OK'):
        window.FindElement('-INPUT-').update("")

window.close()
