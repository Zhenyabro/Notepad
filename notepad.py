import PySimpleGUI as sg

def create_notepad(theme='Dark'):
    sg.theme(theme)
    menu_def = [['Save', ['Open', 'Save', 'Exit']],
                ['Theme', ['Light', 'Dark', 'Green', 'Blue']]]

    layout = [[sg.Menu(menu_def)],
              [sg.Multiline(size=(150, 35), key='-ML-', do_not_clear=False)]]

    window = sg.Window('Notepad', layout, icon='icon.ico')

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'Open':
            filename = sg.popup_get_file('Open File', no_window=True)
            if filename:
                with open(filename, 'r') as f:
                    window['-ML-'].update(f.read())
        if event == 'Save':
            filename = sg.popup_get_file('Save File', save_as=True, no_window=True)
            if filename:
                with open(filename, 'w') as f:
                    f.write(values['-ML-'])
        if event in ('Light', 'Dark', 'Green', 'Blue'):
            theme = 'LightGreen' if event == 'Blue' else 'DarkGreen' if event == 'Green' else 'Default' if event == 'Light' else 'Dark'
            window.close()
            create_notepad(theme)

    window.close()

if __name__ == '__main__':
    create_notepad()