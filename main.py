# Importiong the necessary components from Kivy API
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalcApp(App):

    # Constructor to build and initialize the necessary parameters and methods 
    def build(self):
        # Adding Icon for the calculator
        self.icon = "calculator.png"
        # Array with all arithmatic operators 
        self.operators = ["/","*","+","-"]
        # Initializing the last pressed button and operator variables needed for keeping track of the users keystrokes 
        self.last_op = None
        self.last_button = None
        # Initializing the main layout of the calculator that will contain all the buttons and the display in a vertical format 
        main_layout = BoxLayout(orientation = "vertical")
        # Creating the solution display screen 
        self.solution = TextInput(background_color = "black", foreground_color = "white", multiline = False, halign = "right", font_size = "55", readonly = True)
        # Adding the solution display into the main layout
        main_layout.add_widget(self.solution)
        # Creating a 2D array that contains all the buttons 
        buttons = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","+"],
            [".","0","C","-"],
        ]
        # The for loops are used to insert the buttons into a grid format into the main layout
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size = 50, background_color = "grey",
                    pos_hint = {"center_x" : 0.5, "center_y" : 0.5}
                )
                # Binding the button to a function that will handle what will happen when the button is pressed 
                button.bind(on_press = self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        # Adding in the equals button at the bottom
        equal_button = Button(
            text = "=", font_size = 50, background_color = "grey",
            pos_hint = {"center_x" : 0.5, "center_y" : 0.5}
        )
        # Binding the equals button to a function that will calculate and display the result
        equal_button.bind(on_press = self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout
    
    # This function determines what occurs when each button is pressed 
    def on_button_press(self, instance):
        # Initializing the necessary variables, current will show what is currently has been pressed and button_text will contain text of the button the user has pressed 
        current = self.solution.text
        button_text = instance.text
        # This nested if statement is used to make sure that the user's inputs are being honored in real time, as in if the user pressed C then it will clear the solution display
        if button_text == "C":
            self.solution.text = ""
        else:
            # If the user hits two different operators back to back the nothing should occur
            if current and (self.last_op and button_text in self.operators):
                return
            # If the screen is empty and the user inputs an operator then nothign should happen
            elif current == "" and button_text in self.operators:
                return
            # Finally the user has followed the correct use case then we are updating the solution screen with what the user inputs 
            else:
                new_text = current + button_text
                self.solution.text = new_text
        # Setting up the default values to be used 
        self.last_button = button_text
        self.last_op = self.last_button in self.operators

    # This function is where the arithmatic is done and it updates the screen with the correct solution
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__" :
    app = CalcApp()
    app.run()