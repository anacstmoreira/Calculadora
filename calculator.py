import tkinter

button_values =[
["AC", "+/-", "%", "÷"], 
["7", "8", "9", "×"], 
["4", "5", "6", "-"],
["1", "2", "3", "+"],
["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count= len(button_values) #5 linhas
column_count= len(button_values[0]) #4 colunas

granite_gray= "#5F6368"
old_silver= "#80868B"
arsenic= "#3C4043"
blueberry= "#4285F4"
white= "#FFFFFF"
dark_gray= "#1A1818"


#Janela

window= tkinter.Tk()
window.title("Calculadora")
window.resizable(False,False)

frame= tkinter.Frame(window)
label= tkinter.Label(frame, text="0", font=("Arial", 45), background= granite_gray, foreground=white, anchor= "e", width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky= "we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text= value, font=("Arial", 30), background= granite_gray, width=column_count-1, height=1, command=lambda value=value: button_clicked(value))

        if value in top_symbols:
            button.config(foreground=dark_gray, background= arsenic)
        elif value in right_symbols:
            button.config(foreground= white, background= blueberry)
        else:
            button.config(foreground=white, background= arsenic)

        button.grid(row=row+1, column=column)

frame.pack()

#Possiveis contas A+B, A-B, A*B, A/B
A = "0"
operator= None
B= None

def clear_all():
    global A, B, operator

    A = "0"
    operator= None
    B= None

def remove_zero_deciaml(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA= float(A)
                numB= float(B)

                if operator == "+":
                    label["text"] = remove_zero_deciaml(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_deciaml(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_deciaml(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_deciaml(numA / numB)

                clear_all()

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"]= "0"
                B = "0"

                operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"]= "0"

        elif value == "+/-":
            result = float(label["text"])* -1
            label["text"] = remove_zero_deciaml(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_deciaml(result)

    else: #digitos ou .
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        
        elif value == "√":
            pass

        elif value in "0123456789":

            if label["text"] == "0":
                label["text"] = value

            else:
                label["text"] += value

#Centralizando a janela

window.update()
window_width= window.winfo_width()
window_height= window.winfo_height()
screen_width= window.winfo_screenwidth()
screen_height= window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#Formatação "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()

