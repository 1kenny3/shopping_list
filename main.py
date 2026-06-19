import flet as ft
from db import main_db


def main_page(page: ft.Page):
    page.title = "Список покупок"
    page.theme_mode = ft.ThemeMode.LIGHT
    product_list = ft.Column(scroll=ft.ScrollMode.AUTO)

    filter_type = "all"

    def load_product():
        product_list.controls.clear()
        for product_id, product, completed in main_db.get_products(filter_type):
            product_list.controls.append(
                view_product(
                    product_id=product_id, product_text=product, completed=completed
                )
            )
        page.update()

    def view_product(product_id, product_text, completed):
        product_field = ft.TextField(value=product_text, read_only=True, expand=True)

        checkbox = ft.Checkbox(
            value=bool(completed),
            on_change=lambda e: toggle_task(
                product_id=product_id, is_completed=e.control.value
            ),
        )

        def delete_product(_):
            main_db.delete_product_db(product_id)
            product_list.controls.remove(row)
            page.update()

        delete_btn = ft.IconButton(
            icon=ft.Icons.DELETE_OUTLINE,
            icon_color=ft.Colors.RED_400,
            tooltip="Удалить",
            on_click=delete_product,
        )
        row = ft.Row([checkbox, product_field, delete_btn])
        return row

    def toggle_task(product_id, is_completed):
        main_db.toggle_product_db(product_id=product_id, completed=int(is_completed))

    def add_product(_):
        if product_input.value:
            product_text = product_input.value.strip()
            product_id = main_db.add_product_db(product=product_text)
            product_list.controls.append(
                view_product(
                    product_id=product_id, product_text=product_text, completed=False
                )
            )
            product_input.value = ""
            page.update()

    product_input = ft.TextField(label="Добавить продукт", on_submit=add_product)

    add_button = ft.Button("добавить в список", icon=ft.Icons.ADD, on_click=add_product)
    main_row = ft.Row(
        [product_input, add_button], alignment=ft.MainAxisAlignment.CENTER
    )

    def set_filter(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_product()

    filter_buttons = ft.Row(
        [
            ft.Button("Все", on_click=lambda e: set_filter("all")),
            ft.Button("Некупленные", on_click=lambda e: set_filter("uncompleted")),
            ft.Button("Купленные", on_click=lambda e: set_filter("completed")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(main_row, filter_buttons, product_list)
    load_product()


if __name__ == "__main__":
    main_db.init_db()
    ft.run(main_page)
