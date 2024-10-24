import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")

window = sg.Window(title="Profile", 
                    layout=[[sg.Text("FTI UNISKA",size=(25,1),justification="center")],
                            [sg.Text("FAKULTAS TEKNOLOGI INFORMASI",size=(25,1),justification="left")],
                            [sg.Text("UNISKA MAB BANJARMASIN",size=(25,1),justification="right")]],
                    size=(430,200),
                    font=("Times", 18))
window()
window.close()