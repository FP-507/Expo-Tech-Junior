"""Creare la forma de reporducir videos en flet para usarlo e la aplicacion"""

import flet as ft
import os

class Video:
    def __init__(self,filename):
        self.filename = filename
        self.title = os.path.splitext(filename)[0]

def main(page:ft.Page): 
    page.window.always_on_top = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#ffffff"
    page.title = "Prueba de video"
    page.spacing = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #VideoMedia convierte archivos mp4 para poder usarlos libremente
    list_videos = [
        ft.VideoMedia('Listening_Video\Assets\Avengers_ Infinity War (2018) - _Dangers Of Strangers_ _ Movie Clip.mp4'),
        ft.VideoMedia("Listening_Video\Assets\Bohemian Rhapsody - I'm In Love With My Car Scene (Rami Malek_Freddie Mercury).mp4"),
        ft.VideoMedia("Listening_Video\Assets\Star Wars_ Episode V - I am your Father.mp4"),
    ]

    #ft.video se usa para mostrarlo en panalla y usarlo como cotenedor, playlist es el video o grupos de videos que se van a mostrar 
    video = ft.Video(
        expand= True,
        playlist=list_videos[0:2],
        playlist_mode=ft.PlaylistMode.LOOP,
        fill_color='#1465BB',
        aspect_ratio=16/9,
        volume=100,
        autoplay=False,
        filter_quality=ft.FilterQuality.HIGH,
        muted=False,
        on_loaded=lambda e: print("Video loaded successfully!"),
        on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
        on_exit_fullscreen=lambda e: print("Video exited fullscreen!"),
    )

    contenedor_v = ft.Container(
        content=(video), 
        border_radius=10, 
        height=499, 
        width=886, 
    )

    answers = ft.Column(
        controls=[
            ft.ElevatedButton("Opcion1", bgcolor= "#1465bb", color= '#ffffff'),
            ft.ElevatedButton("Opcion2", bgcolor= "#1465BB", color= '#ffffff'),
            ft.ElevatedButton("Opcion3", bgcolor= "#1465BB", color= '#ffffff'),
            ft.ElevatedButton("Opcion4", bgcolor= "#1465BB", color= '#ffffff'),
            
        ]
    )

    page.add(contenedor_v, answers)






ft.app(target=main)