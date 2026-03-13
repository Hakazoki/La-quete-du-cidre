from datetime import datetime
from textual.app import App, ComposeResult
from textual.widgets import Digits
from textual.widgets import Footer, Label, RichLog, ListView

class Game(App):


    def compose(self) -> ComposeResult:
        yield Digits()
        yield RichLog(auto_scroll=True, highlight=True, markup=True)
    
    def on_key(self, event):
        if event.key == "q":
            self.exit()

        if event.key in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            self.query_one(Digits).add_digit(event.key)

        if event.key == "backspace":
            self.query_one(Digits).remove_digit()


if __name__ == "__main__":
    app = Game()
    app.run()