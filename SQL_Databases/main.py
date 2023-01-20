
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout  
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp

import mysql.connector
from kivy.uix.stacklayout import StackLayout

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="")

my_curser = mydb.cursor()



class MainWidget(AnchorLayout):

    pass


class BaseListe(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lab = Label(text="bases", size=(dp(180), dp(40)), size_hint=( None, None))
        self.add_widget(lab)
        self.bname = SQLApp.base(self)
        for i in self.bname:
            event = SQLApp()
            event.bases = i[0]
            button = Button(text=i[0], size=(dp(180), dp(40)), size_hint=(None, None))
            button.on_press = event.click_tables
            print(i[0])
            self.add_widget(button)

        

class TableListe(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        lab = Label(text="tables", size=(dp(180), dp(40)), size_hint=( None, None))
        self.add_widget(lab)
        
    def go(self, table_namen):
        for i in table_namen:
            print(i[0])
            button = Button(text=i[0], size=(dp(180), dp(40)), size_hint=(None, None))
            self.add_widget(button) 



class MainGrid(GridLayout):

    def __init__(self, **kwargs):                                                   ###in prog
        super().__init__(**kwargs)
       
        for i in range(81):
            button = Button(text="hallo", size=(dp(40), dp(40)), size_hint=(None, None))
            self.add_widget(button)


    def go(self):
        for i in self.grid:
            print(i[0])
            button = Button(text=i[0], size=(dp(40), dp(40)), size_hint=(None, None))
            self.add_widget(button)



class SQLApp(App):


    def base(self):
        my_curser.execute(f"show databases")
        self.bname = my_curser.fetchall()
        return self.bname
        
    
    bases = 0

    def tables(self):
        self.bases                             
        my_curser.execute(f"use {self.bases}")                
        my_curser.execute(f"show tables")
        self.table_namen = my_curser.fetchall()
        return self.table_namen
    
    def view(self, table_name):
        my_curser.execute(f"select * from {table_name};")
        self.tablegrid = my_curser.fetchall()
        return self.tablegrid

    def input(self, input):
        my_curser.execute(f"{input}")
        self.userput = my_curser.fetchall()
        return self.userput


    def click_tables(self):
        self.table_namen = self.tables()
        self.start = TableListe()
        self.start.go(self.table_namen)
        #start.clear_widgets(button)


    def build(self):
        return MainWidget()
        
SQLApp().run()