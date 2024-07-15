from nicegui import ui, app


def exitApp():
    if not app.config.reload:
        app.shutdown()
    else:
        ui.notify("Bye")


class ViewMain:
    def __init__(self):
        pass

    def view(self):
        with ui.header().classes("p-2"):
            with ui.row().classes("items-center fit"):
                ui.label("Hello from niceapp-hoge!")
                ui.space()
                ui.icon("cancel", size="sm").on("click", handler=lambda: exitApp())

        ui.label("This is a niceapp-hoge example.")

        with ui.footer().classes("p-2"):
            ui.space()
            ui.label("Footer")


def main() -> int:
    viewMain = ViewMain()
    viewMain.view()
    ui.run(
        reload=False,
        native=True,
        frameless=True,
        show_welcome_message=False,
    )
    return 0
