import PySimpleGUI as sg    
import os 

sg.theme("DarkGrey8")

def add_jpg_magic_header(file_path):
    jpg_magic_bytes = bytes.fromhex("FF D8 FF")

    with open(file_path, "rb") as f:
        file_data = f.read()

    #check to see if file already has a jpg header
    if file_data[:3] == jpg_magic_bytes:
        sg.popup("the file already has jpeg headers, dummy!")
        return 
    #Add the JPEG header to the file
    new_file_data = jpg_magic_bytes + file_data

    with open(file_data,"wb") as f:
        f.write(new_file_data)

    sg.popup("JPEG Magic Header Successfully added")

Layout = [
    [sg.Text("Select a PHP File:")],
    [sg.Input(key="-FILE-", enable_events=True), sg.FileBrowse()],
    [sg.Button("Add Header"), sg.Button("Exit")]
]

window = sg.Window("Transmog", Layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    
    if event == "Add Header":
        file_path = values["-File-"]

        if not file_path:
            sg.popup("No File Selected.")
            continue

        if not os.path.isfile(file_path):
            sg.popup("Invalid file path.")
            continue

        add_jpg_magic_header(file_path)

window.close()        
