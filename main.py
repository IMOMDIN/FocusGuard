from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import notification
from kivy.core.window import Window


class FullScreenBlock(BoxLayout):
    def __init__(self, unblock_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20
        self.unblock_callback = unblock_callback

        label = Label(
            text="Отдохни 30 секунд!",
            font_size=40,
            color=(1, 1, 1, 1)
        )
        self.add_widget(label)

        Clock.schedule_once(self.unblock, 30)

    def unblock(self, dt):
        self.unblock_callback()


class Reminder(BoxLayout):
    timer_event = None

    def start_timer(self, *args):
        if self.timer_event:
            self.timer_event.cancel()

        self.timer_event = Clock.schedule_interval(self.remind, 20 * 60)
        notification.notify(
            title="FocusGuard",
            message="Напоминания включены",
            timeout=5
        )

    def stop_timer(self, *args):
        if self.timer_event:
            self.timer_event.cancel()
            self.timer_event = None

        notification.notify(
            title="FocusGuard",
            message="Напоминания выключены",
            timeout=5
        )

    def remind(self, dt):
        notification.notify(
            title="FocusGuard",
            message="Отведи взгляд на 30 секунд!",
            timeout=10
        )

        Window.fullscreen = True
        Window.clearcolor = (0, 0, 0, 1)

        def unblock():
            Window.fullscreen = False
            app = App.get_running_app()
            app.root.clear_widgets()
            app.root.add_widget(Reminder())

        block = FullScreenBlock(unblock)
        app = App.get_running_app()
        app.root.clear_widgets()
        app.root.add_widget(block)


class FocusGuardApp(App):
    def build(self):
        return Reminder()


if __name__ == "__main__":
    FocusGuardApp().run()