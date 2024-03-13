import flet
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
)


class CalculatorApp(UserControl):
    def build(self):
        self.reset()
        self.result_text = Text(value="0", color=colors.WHITE, size=20,)
        self.result_numeric_value = 0
        self.general_result_text = Text(value="",color = colors.CYAN, size=30, max_lines=2)
        
        
        # application's root control (i.e. "view") containing all other controls
        return Container(
            width=450,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[self.general_result_text], alignment="end"),
                    Row(controls=[self.result_text], alignment="end"),
                    Row(
                        controls=[
                             ElevatedButton(
                                text="LOG",
                                bgcolor=colors.BLUE_GREY_400,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="LOG",
                            ),
                             ElevatedButton(
                                text="EXP",
                                bgcolor=colors.BLUE_GREY_400,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="EXP",
                            ),
                             ElevatedButton(
                                text="ABS",
                                bgcolor=colors.BLUE_GREY_400,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="ABS",
                            ),
                             ElevatedButton(
                                text="RAND",
                                bgcolor=colors.BLUE_GREY_400,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="RAND",
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                             ElevatedButton(
                                text="CE",
                                bgcolor=colors.BLUE_GREY_300,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="CE",
                            ),
                              ElevatedButton(
                                text="<-",
                                bgcolor=colors.BLUE_GREY_300,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="<-",
                            ),
                               ElevatedButton(
                                text="(",
                                bgcolor=colors.BLUE_GREY_300,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="(",
                            ),
                                ElevatedButton(
                                text=")",
                                bgcolor=colors.BLUE_GREY_300,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data=")",
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="AC",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="AC",
                            ),
                            ElevatedButton(
                                text="+/-",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="+/-",
                            ),
                            ElevatedButton(
                                text="%",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="%",
                            ),
                            ElevatedButton(
                                text="/",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="/",
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="7",
                            ),
                            ElevatedButton(
                                text="8",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="8",
                            ),
                            ElevatedButton(
                                text="9",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="9",
                            ),
                            ElevatedButton(
                                text="*",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="*",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="4",
                            ),
                            ElevatedButton(
                                text="5",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="5",
                            ),
                            ElevatedButton(
                                text="6",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="6",
                            ),
                            ElevatedButton(
                                text="-",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="-",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="1",
                            ),
                            ElevatedButton(
                                text="2",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="2",
                            ),
                            ElevatedButton(
                                text="3",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="3",
                            ),
                            ElevatedButton(
                                text="+",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="+",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="0",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=2,
                                on_click=self.button_clicked,
                                data="0",
                            ),
                            ElevatedButton(
                                text=".",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data=".",
                            ),
                            ElevatedButton(
                                text="=",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="=",
                            ),
                        ]
                    ),
                ],
            ),
        )

    def button_clicked(self, e):
        data = e.control.data
        if self.result_numeric_value == "Error" or data == "CE": # apaga só o principal
            self.result_numeric_value = "0"
            self.result_text.value="0"
            self.reset()
        elif data == "AC": # apaga tudo
            self.result_numeric_value = "0"
            self.result_text.value="0"
            self.general_result_text.value="0"
            self.reset()
        elif data == "<-":
            # Remove the rightmost character
            self.result_numeric_value= str(self.result_numeric_value)[:-1]
        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result_numeric_value == "0" or self.new_operand == True:
                #self.result.value = data # old code
                self.result_numeric_value= data
                self.new_operand = False
            else:
                self.result_numeric_value = self.result_numeric_value + data

        elif data in ("+", "-", "*", "/"):
            precalc_value = self.result_numeric_value
            self.result_numeric_value = self.calculate(
                self.operand1, float(self.result_numeric_value), self.operator
            )
            self.operator = data
            if self.result_numeric_value == "Error":
                self.operand1 = "0"
            else:
                # adiciona o operador à caixa maior
                self.general_result_text.value=self.general_result_text.value + str(precalc_value) + str(self.operator)
                #codigo antigo, sem mudanças
                # self.operand1 = float(self.result.value)  
                self.operand1 = self.result_numeric_value  
            self.new_operand = True

        elif data in ("="):
            self.result_numeric_value = self.calculate(
                self.operand1, float(self.result_numeric_value), self.operator
            )
            self.reset()

        elif data in ("%"):
            self.result_numeric_value = float(self.result_numeric_value) / 100
            self.reset()

        elif data in ("+/-"):
            if float(self.result_numeric_value) > 0:
                self.result_numeric_value = "-" + str(self.result_numeric_value)

            elif float(self.result_numeric_value) < 0:
                self.result_numeric_value = str(
                    self.format_number(abs(float(self.result_numeric_value)))
                )
        #formata numero antes de fazer update
        self.result_text.value= self.format_number(self.result_numeric_value)
        print (F"Result text: {self.result_text.value} - Numberic value: {self.result_numeric_value}")

        self.update()

    def format_number(self, num):
    #esta função está aqui para tirar o .0 dos resultados que são todos doubles.
        # Remove spaces from the string
        if num=='' : num =0
        number_string_without_spaces = str(num).replace(" ", "")
        # convert it back to number
        number_string_without_spaces = float(number_string_without_spaces)
        if number_string_without_spaces % 1 == 0: # removes the .0
            number_string_without_spaces= int(number_string_without_spaces)
        formatted_number = "{:,}".format(number_string_without_spaces).replace(",", " ")
        print(formatted_number)

        return formatted_number
  
    def calculate(self, operand1, operand2, operator):

        # este código pode ser simplificado
        if operator == "+":
            return operand1 + operand2

        elif operator == "-":
            return operand1 - operand2

        elif operator == "*":
            return operand1 * operand2

        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return operand1 / operand2

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True        

def main(page: Page):
    page.title = "Calc App"

    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


#flet.app(target=main)
flet.app(target=main, port=8080, view=flet.WEB_BROWSER)
