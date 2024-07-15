from niceapp_hoge import ViewMain
from nicegui import ui

viewMain = ViewMain()
viewMain.view()
ui.run(
    reload=True,
)
