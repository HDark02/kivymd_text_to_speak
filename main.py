from kivy.uix.spinner import Spinner
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield  import MDTextField
import webbrowser
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screenmanager import ScreenManager
from kivymd.toast.kivytoast.kivytoast import toast
# from kivy.core.audio import SoundLoader
Window.keyboard_anim_args ={'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
from kivymd.uix.list import OneLineListItem
from kivy.properties import StringProperty
from gtts import gTTS
from gtts.langs import _langs
import pyttsx3
from system_sounds import list_files_from_directory
import os

try:
    from kivmob import Kivmob
except:
    pass
# Window.size = (398,804)
class audioCard(OneLineListItem):
    text= StringProperty()
    font_size = 20
    font_style = "H5"
    theme_text_color= "Custom"
    text_color= "white"
class school(MDApp):
    def build(self):
        global screen_manager, note_default
        #initialise
        try:
            self.ads = Kivmob("ca-app-pub-8803263812567783~9785836190")
            self.ads.new_banner(
                ad_id="ca-app-pub-8803263812567783/8211501276",
                top_pos=False,
                overlap=False
            )
            self.ads.request_banner()
            self.ads.show_banner()
        except:
            pass
        screen_manager= ScreenManager()
        screen_manager.add_widget(Builder.load_file("acceuil_1.kv"))
        screen_manager.add_widget(Builder.load_file("enter_text.kv"))
        screen_manager.add_widget(Builder.load_file("about_us.kv"))
        screen_manager.add_widget(Builder.load_file("folder_list.kv"))
        
        return screen_manager
    def contater_nous(self, index):
        if (index== 1) or (index == 2):
            webbrowser.open("https://t.me/Thekingdynamo")
        elif index == "about_us":
            screen_manager.transition.direction = "left"
            screen_manager.current = "about_us"
    def back(self, index):
        if index: #back simple from about_us to enter_text
            screen_manager.transition.direction = "right"
            screen_manager.current = index
    def continu(self):
        screen_manager.transition.direction = "left"
        screen_manager.current = "work_space"
    def convert_text_to_audio(self, text, audio_name_id, slow_of_fast, language_id):
        language = language_id
        try:
            if audio_name_id=="":
                note_default+=1
                audio_name_id=f"audio_1{note_default}"
            language = language
            print(language, audio_name_id)
            if int(slow_of_fast)<=1: #if True
                speech= gTTS(text=text, lang=language, slow=True, tld="com.au")
                
            else:
                speech= gTTS(text=text, lang=language, slow=False, tld="com.au")
            speech.save(f"{audio_name_id}.mp3")
            screen_manager.get_screen("folder_list").audio_list.add_widget(audioCard(text=audio_name_id))
            toast(f"{audio_name_id}.mp3 save successfully")
            
        except:
            rate =100
            engine=pyttsx3.init()
            voice= engine.getProperty("voices")
            if language=="fr":
                engine.setProperty("voice", voice[0].id)
            elif language=="en":
                engine.setProperty("voice", voice[1].id)
            if int(slow_of_fast)<=1: #if True
                engine.setProperty("rate", rate+50)
                if int(slow_of_fast)<=130:
                    engine.setProperty("rate", slow_of_fast)
            else:
                engine.setProperty("rate", rate+30)
            engine.save_to_file(text, f"{audio_name_id}.mp3")
            screen_manager.get_screen("folder_list").audio_list.add_widget(audioCard(text=audio_name_id))
            engine.runAndWait()
            toast(f"{audio_name_id}.mp3 save successfully")
            
    def convert(self, index):
        global dialog, audio_name, slow_or_fast, lang
        dialog = None
        
        if index==1:
            
            slow_or_fast=Spinner(text="140", values=([str(i) for i in range(0, 200)]), font_size="25sp",size_hint= (.45, .2), pos_hint={"center_x": .75, "center_y": .5})
            lang=Spinner(text="French", values=([ i for i in _langs.values()]), font_size="25sp",size_hint= (.45, .2), pos_hint={"center_x": .25, "center_y": .5})
            close_bt=MDRaisedButton(text="save", on_release=self.close_box, pos_hint={"center_x": .5, "center_y": .2},size_hint= (.5, .2), font_size="25sp")
            audio_name=MDTextField(hint_text="Name of the audio file", pos_hint={"center_y": .8, "center_x": .5}, size_hint_x=.7, text_color_normal="black", font_size="25sp")
            float_layout=MDFloatLayout(
                audio_name,
                lang,
                slow_or_fast,
                close_bt,
                pos_hint={"center_x": .6, "center_y": .5})
            if not dialog:
                dialog=Popup(title= "Edit the file name",
                             title_color="black",
                                pos_hint={"center_x": .5, "center_y": .5},
                                size_hint= (.9, .6),
                                background="white"
                                )
                dialog.add_widget(float_layout)
            dialog.open()
    def close_box(self, obj):
        text = screen_manager.get_screen("work_space").entrer_text.text
        slow_of_fast = slow_or_fast.text
        #looking for index of the language name
        language_enter = lang.text
        indice=list(_langs.keys())
        name=list(_langs.values())
        tr=name.index(language_enter)
        language_enter=indice[tr]
        self.convert_text_to_audio(text, audio_name.text, slow_of_fast, language_enter)
        dialog.dismiss()
    def on_stop(self):
        try:
            self.ads.hide_banner()
        except:
            pass
        exit()
    def list_of_audio_all(self):
        audio_list = screen_manager.get_screen("folder_list").audio_list
        audio_list.clear_widgets()
        custom_sounds = list_files_from_directory(os.getcwd(), extensions={".mp3"}) #list of files form the current directory
        for audio in custom_sounds:
            audio = (audio.split("\\"))[-1]
            screen_manager.get_screen("folder_list").audio_list.add_widget(audioCard(text=str(audio)))
    def on_start(self):
        try:
            self.ads.show_banner()
        except:
            pass
        self.list_of_audio_all()
    def play_audio(self, index_name):
        audio_list = screen_manager.get_screen("folder_list").audio_list
        # Rechercher le widget to play
        for audio in audio_list.children:
            if audio.text == index_name:
                sound=audio.text
                try:
                    self.sound.play()
                except:
                    toast("Error to play\nTry it with your music player")
                break
    def remove_audio(self, index_name):
        audio_list = screen_manager.get_screen("folder_list").audio_list
        # Rechercher le widget to remove
        for audio in audio_list.children:
            if audio.text == index_name:
                try:
                    audio_text = (os.getcwd()+ "\\" + audio.text )
                    os.remove(audio_text)
                    audio_list.remove_widget(audio)
                except:
                    toast("Error to delec...")
                break
    def on_pause(self):
        try:
            self.ads.hide_banner()
        except:
            pass
if __name__ == "__main__":
    school().run()






