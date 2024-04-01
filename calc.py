from datetime import datetime
import random
import math


import flet
import pyperclip
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
        self.result_text = Text(value="", color=colors.WHITE, size=20,)
        self.result_numeric_value = 0
        self.general_result_text = Text(value="",color = colors.CYAN, size=30, max_lines=2)
        
        # Initialize with an empty list of items
        self.popup_menu_button = flet.PopupMenuButton(items=[], expand=True,)
        
        # Modify the PopupMenuButton instantiation to include the items attribute
        popup_menu_row = Row(controls=[self.popup_menu_button])  # Add the PopupMenuButton to a Row

        #initialize the dropdown
        self.dropdown = flet.Dropdown(options=[], color=colors.BLUE_200, focused_bgcolor= colors.YELLOW_300,expand=True)
      
        dropdown_row = Row(controls = [self.dropdown])
        dropdown_row_controls = Row([
                ElevatedButton(
                                text="REMOVE",
                                bgcolor=colors.BLUE_GREY_600,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="RMV",
                            ),
                    ElevatedButton(
                                text="COPY TO CLIPBOARD",
                                bgcolor=colors.BLUE_GREY_600,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="CC",
                            ),
        ])
            
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
                    #popup_menu_row,
                    dropdown_row,
                    dropdown_row_controls,
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
                                text="SQRT",
                                bgcolor=colors.BLUE_GREY_400,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="SQRT",
                            ),
                             ElevatedButton(
                                text="RAND",
                                bgcolor=colors.BLUE_GREY_400,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="RAND",
                            ),
                             ElevatedButton(
                                text="TESTE",
                                bgcolor=colors.BLUE_GREY_400,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="TESTE",
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


    def add_popup_menu_item(self, text, on_click=None):
            max_items = 10
            # TODO: Só deve adicionar 10 e faz pop do mais antigo quando chega a este numero DONE
            # TODO: Deve ter indice - tem indice, não é é visivel DONE
            # TODO: deve poder apagar? SEMI DONE
            # TODO: deve ter data hora DONE
            # TODO: Um botão para adicionar à area de transferencia do dispositivo DONE
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current date and time
            new_item_text = f"{current_datetime} # {text}"  # Include the current index in the text
            new_item = flet.PopupMenuItem(text=new_item_text, icon=flet.icons.SUMMARIZE, on_click=on_click)
            
            if len(self.popup_menu_button.items) >= max_items:
                self.popup_menu_button.items.pop(0)  # Remove the oldest item (index 0)

            self.popup_menu_button.items.append(new_item)
            
            ## do the dropdown
            self.dropdown.options.append(flet.dropdown.Option(new_item_text))
            self.dropdown.value = text
            # como faço o update? não é preciso pois é feito no button_clicked
            # page.update            
    
    def button_clicked(self, e):
            
        def handle_dynamic_item_click(event):
            clicked_item_text = event.control.text
            print("Dynamic item clicked!")
            print (F"The chosen item was:({clicked_item_text})")
            #copies to the main text
            self.general_result_text.value= event.control.text
            self.update()
            
        # não sei se vou precisar disto... talvez para apagar coisas no futuro?
        def check_item_clicked(e):
            e.control.checked = not e.control.checked
            e.control.update()
            print("check_item_clicked()")
            
        def find_option(option_name):
            for option in self.dropdown.options:
                if option_name == option.key:
                    return option
            return None

            
        data = e.control.data
        if self.result_numeric_value == "Error" or data == "CE": # apaga só o principal
            self.result_numeric_value = ""
            self.result_text.value=""
            self.reset()
        elif data == "AC": # apaga tudo
            self.result_numeric_value = ""
            self.result_text.value=""
            self.general_result_text.value=""
            self.reset()
        elif data =="LOG":
            self.result_numeric_value = "LOG(" + str(self.result_numeric_value)
            self.result_text.value= self.result_numeric_value
            self.update()
        elif data =="EXP":
            self.result_numeric_value = "EXP(" + str(self.result_numeric_value)
            self.result_text.value= self.result_numeric_value
            self.update()
        elif data =="SQRT":
            self.result_numeric_value = "SQRT(" + str(self.result_numeric_value) 
            self.result_text.value= self.result_numeric_value
            self.update()
        elif data == "(": #adiciona parentesis
            self.result_numeric_value = "(" + str(self.result_numeric_value) 
            self.result_text.value= self.result_numeric_value
            self.update()
        elif data == ")": #adiciona parentesis
            self.result_numeric_value = str(self.result_numeric_value) + ")"
            self.result_text.value= self.result_numeric_value
            self.update()
            
        elif data == "<-":
            # Remove the rightmost character
            self.result_numeric_value= str(self.result_numeric_value)[:-1]
        elif data == "RMV":
            # DOne
            #remove current item from the dropdown
            print("Value removed from dropdown")
            option = find_option(self.dropdown.value)
            if option != None:
                self.dropdown.options.remove(option)
                print(F"Removed!{option.key}")
                print ("MUST REMOVE FROM localStorage!")
                # d.value = None
                #page.update() # not needed
            
        elif data == "CC":
            #copy current RESULT to the device clipboard
            text_to_copy = self.result_text.value
            print (F"Copied to clipboard:{text_to_copy}")
            pyperclip.copy(text_to_copy)
        elif data == "RAND":
            random_number = random.random()
            self.result_numeric_value = random_number
        elif data == "TESTE":
            #add the item do the stack
            item_text = F"Random number: {random.random()}"
            self.add_popup_menu_item(item_text, on_click=handle_dynamic_item_click)
            print ("MUST ADD to localStorage!")
        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            #Old code
            # if self.result_numeric_value == "0" or self.new_operand == True:
            #     #self.result.value = data # old code
            #     self.result_numeric_value= data
            #     self.new_operand = False
            # else:
            #     self.result_numeric_value = self.result_numeric_value + data
            
            #new code
            if (self.result_numeric_value==0):
                self.result_numeric_value = data
            else :
                self.result_numeric_value = str(self.result_numeric_value) + data
            

        elif data in ("+", "-", "*", "/"):
            # Old code
            # precalc_value = self.result_numeric_value
            # self.result_numeric_value = self.calculate(
            #     self.operand1, float(self.result_numeric_value), self.operator
            # )
            # self.operator = data
            # if self.result_numeric_value == "Error":
            #     self.operand1 = "0"
            # else:
            #     # adiciona o operador à caixa maior
            #     self.general_result_text.value=self.general_result_text.value + str(precalc_value) + str(self.operator)
            #     #codigo antigo, sem mudanças
            #     # self.operand1 = float(self.result.value)  
            #     self.operand1 = self.result_numeric_value  
            # self.new_operand = True
            self.general_result_text.value= str(self.general_result_text.value) + str(self.result_numeric_value) + str(data)
            self.result_numeric_value=""
            ##NOTAS:
            # eleiminar new_operand?
            # usar data?
            

        elif data in ("="):
            # Old Code
            # self.result_numeric_value = self.calculate(
            #     self.operand1, float(self.result_numeric_value), self.operator
            # )
            # self.reset()
            
            #New Code
       
            try:
                # first copy the current value
                self.general_result_text.value= str(self.general_result_text.value) + str(self.result_numeric_value)

                # Then evaluate the expression
                expression = self.general_result_text.value
                # do the replacements
                # For LOG
                expression = expression.replace("LOG", "math.log")
                # For LOG
                expression = expression.replace("SQRT", "math.sqrt")
                # For EXP
                expression = expression.replace("EXP", "math.exp")
              
                # end replacements
                evaluation = eval(expression)
                self.general_result_text.value = evaluation
                # clears the input
                self.result_numeric_value=""
            except Exception as e:
                print (F"Error: {e}")
                self.result_numeric_value = "Error in expression"
                self.reset()
       

        elif data in ("%"):
            self.result_numeric_value = float(self.result_numeric_value) / 100
            self.reset()

        elif data in ("+/-"):
            #Aqui simplesmente adiciona o sinal de menos que é o que está a fazer
            # tem é que deixar de dar erro
            try:
                if float(self.result_numeric_value) > 0:
                    self.result_numeric_value = "-" + str(self.result_numeric_value)

                elif float(self.result_numeric_value) < 0:
                    self.result_numeric_value = str(
                        self.format_number(abs(float(self.result_numeric_value)))
                    )
            except Exception as e:
                print ("Erro inverting signal")
                self.result_numeric_value = "Error"
        #formata numero antes de fazer update
        self.result_text.value= self.format_number(self.result_numeric_value)
        print (F"Result text: {self.result_text.value} - Numberic value: {self.result_numeric_value}")

        #estava a dar erro
        self.update()

    def format_number(self, num):
    #esta função está aqui para tirar o .0 dos resultados que são todos doubles.
        # Remove spaces from the string
        try:
            
            #if num=='' : num =0 # nao preciso dos leading zeros
            num = str(float(num))
            number_string_without_spaces = str(num).replace(" ", "")
            # convert it back to number
            number_string_without_spaces = float(number_string_without_spaces)
            if number_string_without_spaces % 1 == 0: # removes the .0
                number_string_without_spaces= int(number_string_without_spaces)
            formatted_number = "{:,}".format(number_string_without_spaces).replace(",", " ")
            print(formatted_number)

            return formatted_number
        except Exception as e:
            return num
  
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
    print("change something")
    page.title = "Calc App"

    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


#flet.app(target=main)
flet.app(target=main, port=8080, view=flet.WEB_BROWSER)
