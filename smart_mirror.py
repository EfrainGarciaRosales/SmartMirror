import tkinter as tk
from datetime import datetime

from weather import get_weather
from mirror_calendar import get_events


class SmartMirror:
    def __init__(self, root):
        self.root = root

        self.root.title("Smart Mirror")
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)

        # Escape exits fullscreen
        self.root.bind("<Escape>", self.exit_fullscreen)

        # TIME
        self.time_label = tk.Label(
            root,
            font=("Helvetica", 72),
            fg="white",
            bg="black"
        )
        self.time_label.pack(anchor="ne", padx=50, pady=(30, 0))

        # DATE
        self.date_label = tk.Label(
            root,
            font=("Helvetica", 28),
            fg="white",
            bg="black"
        )
        self.date_label.pack(anchor="ne", padx=50)

        # WEATHER TITLE
        self.weather_title = tk.Label(
            root,
            text="Weather",
            font=("Helvetica", 30, "bold"),
            fg="white",
            bg="black"
        )
        self.weather_title.place(x=50, y=50)

        # WEATHER INFO
        self.weather_label = tk.Label(
            root,
            text="Loading weather...",
            font=("Helvetica", 24),
            fg="white",
            bg="black",
            justify="left"
        )
        self.weather_label.place(x=50, y=100)

        # CALENDAR TITLE
        self.calendar_title = tk.Label(
            root,
            text="Upcoming Events",
            font=("Helvetica", 30, "bold"),
            fg="white",
            bg="black"
        )
        self.calendar_title.place(x=50, y=400)

        # CALENDAR EVENTS
        self.calendar_label = tk.Label(
            root,
            text="Loading events...",
            font=("Helvetica", 22),
            fg="white",
            bg="black",
            justify="left"
        )
        self.calendar_label.place(x=50, y=450)

        self.update_time()
        self.update_weather()
        self.update_calendar()

    def update_time(self):
        now = datetime.now()

        current_time = now.strftime("%I:%M %p").lstrip("0")
        current_date = now.strftime("%A, %B %d, %Y")

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        self.root.after(1000, self.update_time)

    def update_weather(self):
        weather = get_weather()

        self.weather_label.config(text=weather)

        # Refresh weather every 10 minutes
        self.root.after(600000, self.update_weather)

    def update_calendar(self):
        events = get_events()

        self.calendar_label.config(text=events)

        # Refresh calendar every 5 minutes
        self.root.after(300000, self.update_calendar)

    def exit_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)


if __name__ == "__main__":
    root = tk.Tk()
    app = SmartMirror(root)
    root.mainloop()