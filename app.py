from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivymd.button import MDFlatButton
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationDrawer
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListView


kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import NavigationDrawer kivymd.navigationdrawer.NavigationDrawer
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import SingleLineTextField kivymd.textfields.SingleLineTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem

BoxLayout:
    orientation: 'vertical'
    Toolbar:
        id: toolbar
        title: 'KivyMD Kitchen Sink'
        background_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: app.nav_drawer.toggle()]]
        right_action_items: [['more-vert', lambda x: app.nav_drawer.toggle()]]
    ScreenManager:
        id: scr_mngr
        Screen:
            name: 'rants'
            RantsFeed
            # MDRaisedButton:
            #     text: "Open list bottom sheet"
            #     opposite_colors: True
            #     size_hint: None, None
            #     size: 4 * dp(48), dp(48)
            #     pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            #     on_release: app.show_example_bottom_sheet()
            MDRaisedButton:
                text: "Open grid bottom sheet"
                opposite_colors: True
                size_hint: None, None
                size: 4 * dp(48), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                on_release: app.show_example_grid_bottom_sheet()

        Screen:
            name: 'login'
            SingleLineTextField:
                text: 'asd'
                size_hint: None, None
                size: 4 * dp(48), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            MDRaisedButton:
                text: "Log in"
                size_hint: None, None
                size: 4 * dp(48), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}

<NavDrawer>
    title: "DevRant"
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Rants"
        on_release: app.root.ids.scr_mngr.current = 'rants'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Log in"
        on_release: app.root.ids.scr_mngr.current = 'login'

<RantsFeed>
    ScrollView:
        do_scroll_x: False
        MDList:
            OneLineListItem:
                text: 'foo'
            OneLineListItem:
                text: 'bar'
            OneLineListItem:
                text: 'foo'
            OneLineListItem:
                text: 'bar'
            OneLineListItem:
                text: 'foo'
            OneLineListItem:
                text: 'bar'
            OneLineListItem:
                text: 'foo'
            OneLineListItem:
                text: 'bar'
            OneLineListItem:
                text: 'foo'
            OneLineListItem:
                text: 'bar'
            OneLineListItem:
                text: 'foo'
            OneLineListItem:
                text: 'bar'
            OneLineListItem:
                text: 'foo'
            OneLineListItem:
                text: 'bar'
            OneLineListItem:
                text: 'foo'
            OneLineListItem:
                text: 'bar'
            OneLineListItem:
                text: 'foo'
            OneLineListItem:
                text: 'bar'
            OneLineListItem:
                text: 'foo'
            OneLineListItem:
                text: 'bar'
            OneLineListItem:
                text: 'foo'
            OneLineListItem:
                text: 'bar'
            OneLineListItem:
                text: 'foo'
            OneLineListItem:
                text: 'bar'
'''


class NavDrawer(NavigationDrawer):
    pass


class MyButton(MDFlatButton):
    pass

class RantsFeed(ScrollView):
    pass

class TestApp(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def build(self):
        # self.theme_cls.theme_style = 'Dark'
        main = Builder.load_string(kv)
        self.nav_drawer = NavDrawer()
        return main

TestApp().run()
