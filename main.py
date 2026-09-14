from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class PrankApp(App):
    def build(self):
        Window.fullscreen = True
        Window.clearcolor = (0, 0, 0, 1)

        self.title_label = Label(
            text="[color=#ff0000]⚠ SYSTEM SECURITY ALERT ⚠[/color]",
            markup=True, font_size="22sp", bold=True,
            size_hint_y=None, height="70dp"
        )
        self.message = Label(
            text="Initializing security scan...",
            color=(1,1,1,1), font_size="18sp", bold=True,
            size_hint_y=None, height="70dp"
        )
        self.progress = Label(
            text="SCAN: 0%", color=(1,0,0,1),
            font_size="24sp", bold=True,
            size_hint_y=None, height="70dp"
        )
        self.status = Label(
            text="Please wait...", color=(1,1,1,1),
            font_size="16sp", size_hint_y=None, height="70dp"
        )

        box = BoxLayout(orientation="vertical", padding=30, spacing=10)
        box.add_widget(self.title_label)
        box.add_widget(self.message)
        box.add_widget(self.progress)
        box.add_widget(self.status)

        self.percent = 0
        Clock.schedule_once(lambda dt: self.scan(0), 1)
        Window.bind(on_touch_down=self.exit_on_touch)
        return box

    def scan(self, dt=None):
        if self.percent <= 100:
            self.progress.text = f"SCAN: {self.percent}%"
            if self.percent < 30:
                self.status.text = "Checking system files..."
            elif self.percent < 60:
                self.status.text = "Checking applications..."
            elif self.percent < 90:
                self.status.text = "Checking device security..."
            else:
                self.status.text = "Finalizing scan..."
            self.percent += 1
            Clock.schedule_once(self.scan, 0.1)
        else:
            self.reveal()

    def reveal(self):
        self.title_label.text = "[color=#ff0000]⚠ HACKER ⚠[/color]"
        self.message.text = "DEVICE SECURITY COMPROMISED!"
        self.progress.text = "HACKED BY DANIEL 😈"
        self.progress.font_size = "26sp"
        self.status.text = "😂 DON'T PANIC!\\n\\nTHIS IS JUST A PRANK!"
        Clock.schedule_interval(self.blink, 0.4)

    def blink(self, dt):
        self.title_label.color = (1,1,1,1) if self.title_label.color == (1,0,0,1) else (1,0,0,1)

    def exit_on_touch(self, window, touch):
        # First tap after the prank is revealed exits; during scan it does not.
        if self.percent > 100:
            self.stop()
            return True
        return False

if __name__ == "__main__":
    PrankApp().run()
