from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class AccessibleCalculator(BoxLayout):

    def __init__(self, **kwargs):
        super(AccessibleCalculator, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = 20

        # Operator track karne ke liye
        self.selected_operator = None

        # Title Label
        self.add_widget(
            Label(
                text="AI Accessible Calculator",
                font_size=24,
                size_hint_y=None,
                height=40,
            )
        )

        # --- 1. Pehla Number aur uska Clear button ---
        self.add_widget(
            Label(text="Enter first number", size_hint_y=None, height=25)
        )
        row1 = BoxLayout(
            orientation="horizontal", spacing=10, size_hint_y=None, height=50
        )

        self.num1_input = TextInput(
            multiline=False,
            input_filter="float",
            input_type="number",  # Mobile par numeric keypad open karega
            size_hint_x=0.7,
        )
        self.clear_btn1 = Button(text="Clear 1", size_hint_x=0.3)
        self.clear_btn1.bind(on_press=self.clear_input1)

        row1.add_widget(self.num1_input)
        row1.add_widget(self.clear_btn1)
        self.add_widget(row1)

        # --- 2. Dusra Number aur uska Clear button ---
        self.add_widget(
            Label(text="Enter second number", size_hint_y=None, height=25)
        )
        row2 = BoxLayout(
            orientation="horizontal", spacing=10, size_hint_y=None, height=50
        )

        self.num2_input = TextInput(
            multiline=False,
            input_filter="float",
            input_type="number",
            size_hint_x=0.7,
        )
        self.clear_btn2 = Button(text="Clear 2", size_hint_x=0.3)
        self.clear_btn2.bind(on_press=self.clear_input2)

        row2.add_widget(self.num2_input)
        row2.add_widget(self.clear_btn2)
        self.add_widget(row2)

        # Operator Selection Label
        self.add_widget(
            Label(text="Select an operator", size_hint_y=None, height=25)
        )

        # Operator Buttons Layout
        self.operator_layout = BoxLayout(
            orientation="horizontal", spacing=10, size_hint_y=None, height=50
        )
        self.op_buttons = {}
        for op in ["+", "-", "*", "/"]:
            btn = Button(text=op, font_size=20)
            btn.bind(on_press=self.select_operator)
            self.op_buttons[op] = btn
            self.operator_layout.add_widget(btn)
        self.add_widget(self.operator_layout)

        # --- 3. Calculate Button ---
        self.calc_button = Button(
            text="Calculate Result",
            font_size=22,
            background_color=(0.2, 0.6, 1, 1),
            size_hint_y=None,
            height=55,
        )
        self.calc_button.bind(on_press=self.perform_calculation)
        self.add_widget(self.calc_button)

        # Result Label
        self.result_label = Label(
            text="Result will appear here", font_size=20, size_hint_y=None, height=50
        )
        self.add_widget(self.result_label)

    def clear_input1(self, instance):
        self.num1_input.text = ""
        self.result_label.text = "First number cleared"

    def clear_input2(self, instance):
        self.num2_input.text = ""
        self.result_label.text = "Second number cleared"

    def select_operator(self, instance):
        self.selected_operator = instance.text
        self.result_label.text = f"Selected operator: {self.selected_operator}. Now click on Calculate Result."

    def perform_calculation(self, instance):
        if not self.selected_operator:
            self.result_label.text = (
                "Error: Please select an operator first (+, -, *, /)"
            )
            return

        try:
            n1 = float(self.num1_input.text)
            n2 = float(self.num2_input.text)
            operator = self.selected_operator

            if operator == "+":
                res = n1 + n2
            elif operator == "-":
                res = n1 - n2
            elif operator == "*":
                res = n1 * n2
            elif operator == "/":
                if n2 != 0:
                    res = n1 / n2
                else:
                    res = "Error: Division by zero"

            self.result_label.text = f"Result is: {res}"

        except ValueError:
            self.result_label.text = "Error: Please enter valid numbers"


class CalculatorApp(App):

    def build(self):
        self.title = "Accessible Calculator Pro"
        return AccessibleCalculator()


if __name__ == "__main__":
    CalculatorApp().run()
