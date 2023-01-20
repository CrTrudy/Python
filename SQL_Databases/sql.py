from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp

from kivy.uix.stacklayout import StackLayout

import mysql.connector




mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="")

my_curser = mydb.cursor()




class BaseListe(StackLayout):
    base = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label_bas = Label(text="bases", size=(dp(180), dp(25)), size_hint=(None, None))
        self.add_widget(label_bas)
    

        my_curser.execute(f"show databases")
        self.bname = my_curser.fetchall()

        for i in self.bname:
            button = Button(text=i[0], size=(dp(180), dp(25)), size_hint=(None, None))
            button.bind(on_press=self.show_tables)
            self.add_widget(button)

    def show_tables(self, obj):
        self.base = obj
        app = App.get_running_app()
        tab = app.root.ids.table_liste
        tab.clear_widgets()

        label_tab = Label(text=obj.text, size=(dp(180), dp(25)), size_hint=( None, None))
        tab.add_widget(label_tab)

        print(obj.text)

        my_curser.execute(f"use {obj.text}")                
        my_curser.execute(f"show tables")
        self.tname = my_curser.fetchall()
        
        for i in self.tname:
            button = Button(text=i[0], size=(dp(180), dp(25)), size_hint=(None, None))
            button.bind(on_press=self.change_grid)
            tab.add_widget(button)
        

    def change_grid(self, obj):
        app = App.get_running_app()
        grid = app.root.ids.main_grid
        grid.clear_widgets()


        my_curser.execute(
        f"SELECT COLUMN_NAME  FROM INFORMATION_SCHEMA.COLUMNS where table_name = '{obj.text}' and table_schema = '{self.base.text}';")
        self.tablecols = my_curser.fetchall()
        print(self.tablecols)


        my_curser.execute(f"SELECT column_name, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = '{obj.text}'")
        self.table_type = my_curser.fetchall()
        print(self.table_type)


        my_curser.execute(f"select * from {obj.text};")
        self.tablegrid = my_curser.fetchall()

        
        if len(self.tablegrid) >= 1:

            grid.rows = len(self.tablegrid) +1
            grid.cols = len(self.tablegrid[0])

            z = []
            z = [0] * int(grid.cols)
            p = 0
            for i in self.tablecols:
                xx = len(str(i))*5+10
                if xx > z[p]:
                    z[p] = xx
                p +=1

            for y in self.tablegrid:
                p = 0
                for j in y:
                    xx = len(str(j))*7+15
                    if xx > z[p]:
                        z[p] = xx
                    p +=1
                

            q = 0
            for i in self.tablecols:
                button = Button(text=i[0], size=(dp(z[q]), dp(20)), size_hint=(None, None))
                grid.add_widget(button)
                q += 1


            for i in self.tablegrid:
                r = 0
                for j in i:
                    button = Button(text=str(j), size=(dp(z[r]), dp(20)), size_hint=(None, None))
                    grid.add_widget(button)
                    r += 1



class TableListe(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label_tab = Label(text="tables", size=(dp(180), dp(25)), size_hint=( None, None))
        self.add_widget(label_tab)

    pass

class MainGrid(GridLayout):
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)
        
    pass


class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
       
class SQLApp(App):
    pass


SQLApp().run()