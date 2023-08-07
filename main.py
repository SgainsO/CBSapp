from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.button import Label
from prac import *
from googleDrive import totalUpload, totalDownload
from PythonApplication1 import *
from cooking import *



class ShowAllStore(Label):
    def __init__(self, **kwargs):
        super().__init__()

    def returnAll(self):
        temp = showAll()
        return temp



class EnterButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save(self, tempSave):
        addRec(tempSave)

class CommentButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def cSave(self, rec, comm):
        commenter(rec, comm)

class SearchButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def search(self, temp):
        abac = search(temp)
        return abac

class SaveButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def UploadToServer(self):
        totalUpload()


class HomeScreen(Screen):
    pass

class SearchFor(Screen):
    pass

class OptionOne(Screen):
    pass

class Comment(Screen):
    pass

class All(Screen):
    pass




class My_Manager(ScreenManager):
    pass

class GUIApp(App):
    def build(self):
        return My_Manager()

    def on_start(self, **kwargs):
        printth()
        totalDownload()



    #    self.window = BoxLayout()
    # add widgets to window

    # return self.window


if __name__ == "__main__":
    GUIApp().run()
#GUI().run()
