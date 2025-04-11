import flet as ft
import os 

def main(page:ft.Page):
    page.window.always_on_top = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#ffffff"
    page.title = "Prueba de Medallas"
    page.spacing = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    nivel = 5
    medallas_obt = {}
    medallas=[ft.Image(x) for x in os.listdir('Sistema_Medallas\Assets')]

    
    

    def cargar_medallas(): 
        nonlocal medallas_obt
        nonlocal nivel
        nonlocal medallas

        grid.controls.clear()

        x=0
        for m in medallas:
            x += 5
            medallas_obt.update({m : x})

        for img in medallas_obt.keys(): 
            if medallas_obt.get(img) <= nivel: 
                grid.controls.append(img)
                page.update()
       
    
    def subir_nivel(cant_subir): 
        nonlocal nivel
        nivel+= cant_subir
        cargar_medallas()
        page.update()
        
    

    grid = ft.GridView(
        expand= True,
        max_extent= 220,
        child_aspect_ratio=1, 
        spacing= 10,
        run_spacing= 100,
    )


    btn_level = ft.ElevatedButton("subir nivel",bgcolor='#059862', on_click= lambda _: subir_nivel(1))
    btn_level2 = ft.ElevatedButton("bajar nivel",bgcolor='#059862', on_click= lambda _: subir_nivel(-1))
    

    controls = ft.Row([btn_level,btn_level2])
        

    cargar_medallas()
    page.add(grid,controls)



ft.app(target=main)