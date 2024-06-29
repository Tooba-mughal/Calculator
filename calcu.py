import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x500")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying the result
        result_entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=4, width=14,
                                borderwidth=4)
        result_entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_value = 1
        col_value = 0

        for button in buttons:
            button_action = lambda x=button: self.on_button_click(x)
            button_widget = tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 18), command=button_action)
            button_widget.grid(row=row_value, column=col_value, sticky="nsew")

            col_value += 1
            if col_value > 3:
                col_value = 0
                row_value += 1

        # Clear button
        clear_button = tk.Button(self, text='C', padx=20, pady=20, font=('Arial', 18), command=self.clear_result)
        clear_button.grid(row=row_value, column=0, columnspan=4, sticky="nsew")

        # Configure grid
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        current_text = self.result_var.get()
        if char == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            new_text = current_text + str(char)
            self.result_var.set(new_text)

    def clear_result(self):
        self.result_var.set("")


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
