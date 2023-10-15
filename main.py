import flet as ft

def ask_for_name():
    name_input = ft.TextField(
        label="Як тебе звати?",
        width=500,
        height=200,
        multiline=False,
        border_radius=10
    )
    name_button = ft.ElevatedButton(
        text="Увійти",
        color="#4CAF50",
        width=200,
        height=80,
        elevation=10,
        on_click=lambda e: login(name_input.value)
    )
    name_row = ft.Row([name_input, name_button], alignment=ft.MainAxisAlignment.CENTER)
    name_container = ft.Container(
        height=100,
        padding=ft.Padding(0, 0, 0, 0),
        content=name_row,
    )
    return name_container

user_input = ft.TextField(
    label="Введення користувача",
    width=500,
    height=200,
    multiline=True,
    max_lines=6,
    min_lines=6,
    border_radius=10
)

gpt_output = ft.TextField(
    label="Вивід GPT",
    color="#677C77",
    multiline=True,
    max_lines=15,
    min_lines=15,
    border_radius=10,
    width=500,
    height=400
)

def create_user_input_row():
    container = ft.Container(
        width=500,
        height=200,
        content=user_input,
        padding=ft.Padding(20, 20, 20, 20)
    )
    card = ft.Card(
        elevation=10,
        color="#6B5B95",
        width=500,
        height=200
    )
    return ft.Row([card], alignment=ft.MainAxisAlignment.CENTER)

def create_gpt_output_row():
    container = ft.Container(
        width=500,
        height=400,
        content=gpt_output,
        padding=ft.Padding(20, 20, 20, 20)
    )
    card = ft.Card(
        elevation=10,
        color="#FF0000",
        width=500,
        height=400
    )
    return ft.Row([card], alignment=ft.MainAxisAlignment.CENTER)

def login(name):
    if name:
        # Вхід в систему після введення імені
        # Ви можете ввести вашу логіку для входу в систему тут.
        name_container.hidden = True  # Приховуємо поле введення імені
        # Показуємо поле введення користувача та виводу GPT
        user_input.hidden = False
        gpt_output.hidden = False
    else:
        # Встановлюємо повідомлення про помилку для поля введення імені
        name_input.error_message = "Будь ласка, введіть ваше ім'я."

name_container = ask_for_name()
name_container.hidden = False  # Показуємо поле введення імені

def main(page: ft.Page):
    page.title = "FletGpt"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#F2F4F3"
    page.window_maximized = True

    user_input_row = create_user_input_row()

    def click_button(e):
        from gpt_core import send_request
        gpt_output.value = send_request(user_input.value)
        gpt_output.update()
        page.update()

    send_button = ft.ElevatedButton(
        text="Відправити",
        color="#4CAF50",
        width=200,
        height=80,
        elevation=10,
        on_click=click_button
    )
    button_row = ft.Row([send_button], alignment=ft.MainAxisAlignment.CENTER)
    button_container = ft.Container(
        height=100,
        padding=ft.Padding(0, 0, 0, 0),
        content=button_row,
    )

    gpt_output_row = create_gpt_output_row()

    column = ft.Column(
        [name_container, user_input_row, button_container, gpt_output_row],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(column)

ft.app(target=main)