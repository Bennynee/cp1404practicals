from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

COLOUR = (1, 0, 0, 1)


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        """Load the root widget from the KV file"""
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Dynamically create Labels and add them to the layout."""
        main_layout = self.root.ids.main
        for name in self.names:
            temp_label = Label(text=name, font_size=24)
            main_layout.add_widget(temp_label)
            temp_label.background_color = COLOUR


DynamicLabelsApp().run()