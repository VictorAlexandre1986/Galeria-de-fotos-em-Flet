import flet as ft

def main(page: ft.Page):

    def image(num: int):
        return ft.Image(
                src=f'https://picsum.photos/150/150?random={num}',
                fit = ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT
            )
    
    def change_view(e):
        btn1.style= btn_style
        btn2.style = btn_style
        e.control.style = btn_style_selected

        if e.control.text == 'Todas as fotos':
            layout.controls[0] = grid2 
        else:
            layout.controls[0] = grid1

        layout.update()


    grid1 = ft.GridView(
        controls=[ image(i) for i in range(30)],
            expand=True,
            runs_count=5,#Defini o numero de colunas, mas como estamos de definindo max_extent, ele assume o valor de 150 para cada foto
            spacing=10,
            max_extent=150,
            child_aspect_ratio=1.0
        )

    grid2 = ft.Column(
        expand=True,
        controls=[
            ft.Text(value='2022', size=30),
            ft.GridView(
                controls=[ image(i) for i in range(0,4)],
                runs_count=4,
                child_aspect_ratio=1.0,
                spacing=10,
                run_spacing=10
            ),
            ft.Text(value='2023', size=30),
            ft.GridView(
                controls=[ image(i) for i in range(5,9)],
                runs_count=4,
                child_aspect_ratio=1.0,
                spacing=10,
                run_spacing=10
            ),
            ft.Text(value='2024', size=30),
            ft.GridView(
                controls=[ image(i) for i in range(10,14)],
                runs_count=4,
                child_aspect_ratio=1.0,
                spacing=10,
                run_spacing=10
            ),
        ]
    )

    btn_style_selected = ft.ButtonStyle(
        bgcolor= ft.colors.BLACK54,
        color=ft.colors.WHITE,
        elevation=0,
        overlay_color=ft.colors.BLACK12
    )

    btn_style = ft.ButtonStyle(
        bgcolor= ft.colors.TRANSPARENT,
        color=ft.colors.BLACK54,
        elevation=0,
        overlay_color=ft.colors.BLACK12
    )



    footer = ft.Container(
        bgcolor=ft.colors.BLACK54,
        margin=ft.margin.symmetric(vertical=5, horizontal=10),
        padding=ft.padding.all(5),
        border_radius=ft.border_radius.all(50),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                btn1 := ft.ElevatedButton(
                    text='Todas as fotos', 
                    style=btn_style_selected,
                    on_click=change_view),
                btn2 := ft.ElevatedButton(
                    text='Agrupadas por ano', 
                    style=btn_style,
                    on_click=change_view),
            ],
            tight=True
        )
    )

    layout = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        controls=[grid2, footer],
    )


    page.add(layout)
   


if __name__=='__main__':
    ft.app(target=main)