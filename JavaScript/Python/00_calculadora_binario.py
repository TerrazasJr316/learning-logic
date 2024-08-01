"""
Dasarrolla una calculadora que convierta un numero decimal
a binario y de binario a decimal
"""

import tkinter as tk

def decimal_binary():
    try:
        
        decimal_num = int(input_field.get())
        binary_num = bin(decimal_num).replace("0b", "")
        output_label.config(text = f"Binary: {binary_num}")
    except ValueError:
        output_label.config(text = "Entrada invalida. Por favor introduce un numero deciaml: ")
        
def binary_decimal():
    try:
        binary_num = input_field.get()
        decimal_num = int(binary_num, 2)
        output_label.config(text = f"Binary: {decimal_num}")
    except ValueError:
        output_label.config(text = "Entrada invalida. Por favor introduce un numero binario: ")
        
def clear_output():
    output_label.config(text = "")

root = tk.Tk()
root.title("Convertidor Binario-Decimal")

menu_frame = tk.Frame(root)
menu_frame.pack()

decimal_binary_button = tk.Button(menu_frame, text = "Decimal a Binario", command = decimal_binary)
decimal_binary_button.pack(side = tk.LEFT)

binary_decimal_button = tk.Button(menu_frame, text = "Binario a Decimal", command = binary_decimal)
binary_decimal_button.pack(side = tk.LEFT)

clear_output = tk.Button(root, text = "Borrar", command = clear_output)
clear_output.pack()

input_field = tk.Entry(root)
input_field.pack()

convert_button = tk.Button(root, text = "Convertir", command = lambda: None)
convert_button.pack()

output_label = tk.Label(root, text = "", pady = 10)
output_label.pack()