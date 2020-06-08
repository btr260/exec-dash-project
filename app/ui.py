import PySimpleGUI as sg

sg.ChangeLookAndFeel("GreenTan")

layout = [
    [sg.Text("Welcome to your monthly sales report!",
             size=(30, 1), font=("Helvetica", 25))],
    [sg.Text("Please select the month of interest:")],
    #[sg.InputText("This is my text")],
    #[sg.Checkbox("My first checkbox!"), sg.Checkbox(
    #    "My second checkbox!", default=True)],
    #[sg.Radio("My first Radio!     ", "RADIO1", default=True),
    # sg.Radio("My second Radio!", "RADIO1")],
    #[sg.Multiline(default_text="This is the default Text should you decide not to type anything", size=(35, 3)),
    # sg.Multiline(default_text="A second multi-line", size=(35, 3))],
    #[sg.InputCombo(("Combobox 1", "Combobox 2"), size=(20, 3)),
    # sg.Slider(range=(1, 100), orientation="h", size=(34, 20), default_value=85)],
    [sg.Listbox(values=("Listbox 1", "Listbox 2", "Listbox 3"), size=(30, 3))],
    [sg.Text("_" * 80)],
    #[sg.Text("Choose A Folder", size=(35, 1))],
    #[sg.Text("Your Folder", size=(15, 1), auto_size_text=False, justification="right"),
    # sg.InputText("Default Folder"), sg.FolderBrowse()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window("Monthly sales report",
                   default_element_size=(40, 1)).Layout(layout)
button, values = window.Read()
sg.Popup(button, values)
