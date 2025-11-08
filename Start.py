import json
from re import search
from tkinter.ttk import Button
from markdown_it.rules_block import table
import JsonManagement as jm
import Data
import TimeManager
from CalendarManager import AddEvent
from textual.app import App
from textual.widgets import Header, DataTable, Input, Static, Button
from textual.containers import Container
from textual.reactive import reactive
from textual.events import Key
from textual.binding import Binding


log = "Data/log.txt"
class Calendar(App):
    BINDINGS = [
        Binding("a", "add_event", "Add Event"),
        Binding("t", "today", "Today"),
        Binding("ctrl+t", "tomorrow", "Tomorrow"),
        Binding("w", "week", "This Week"),
        Binding("n", "next_week", "Next Week"),
        Binding("/", "focus_search", "Focus Search"),
        Binding("escape", "clear_search", "Clear Search/ Unfocus"),
    ]
    query = reactive("")
    def compose(self):
        yield Header()
        yield Input(placeholder="Search events...", id="search_input")
        yield DataTable(id="events_table")

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Title", "Date", "Time", "Description")
        self.refreshTable()

    def on_input_changed(self, event: Input.Changed) -> None:
        self.query = event.value
        self.refreshTable()

    def action_add_event(self) -> None:
        self.call_later(self.AddEvent)
    def action_today(self) -> None:
        self.Today()
    def action_tomorrow(self) -> None:
        self.Tommorow()
    def action_week(self) -> None:
        self.ThisWeek()
    def action_next_week(self) -> None:
        self.NextWeek()
    def action_focus_search(self) -> None:
        search_input = self.query_one("#search_input", Input)
        search_input.focus()
    def action_clear_search(self) -> None:
        search_input = self.query_one("#search_input", Input)
        search_input.value = ""
        self.query = ""
        self.refreshTable()
        search_input.blur()

    def refreshTable(self):
        table = self.query_one(DataTable)
        table.clear()
        events = jm.Fetch()
        if self.query == "":
            for event in events:
                table.add_row(event["title"], event["date"], event["time"], event["description"])
        else:
            for event in events:
                if self.query.lower() in event["title"].lower() or self.query.lower() in event["description"].lower() or self.query.lower() in event["date"].lower():
                    table.add_row(event["title"], event["date"], event["time"], event["description"])
    def Today(self):
        self.query = TimeManager.TodayDate()
        self.refreshTable()
    def Tommorow(self):
        self.query = TimeManager.TommorowDate()
        self.refreshTable()
    def ThisWeek(self):
        week_dates = TimeManager.ThisWeekDate()
        self.query = ""

        table = self.query_one(DataTable)
        table.clear()

        events = jm.Fetch()
        for event in events:
            if event["date"] in week_dates:
                table.add_row(event["title"], event["date"], event["time"], event["description"])
    def NextWeek(self):
        week_dates = TimeManager.NextWeekDate()
        self.query = ""

        table = self.query_one(DataTable)
        table.clear()

        events = jm.Fetch()
        for event in events:
            if event["date"] in week_dates:
                table.add_row(event["title"], event["date"], event["time"], event["description"])
    async def AddEvent(self):
        table = self.query_one("#events_table")
        search = self.query_one("#search_input")


        table.display = False
        search.display = False

        form = EventForm()
        await self.mount(form)
        self.query = ""
        self.refreshTable()


class EventForm(Static):
    def compose(self):
        yield Input(placeholder="Title", id="title_input")
        yield Input(placeholder="Date (DD-MM-YY)", id="date_input")
        yield Input(placeholder="Time (HH:MM) or leave blank for all-day event", id="time_input")
        yield Input(placeholder="Description", id="description_input")
        yield Button("Save", id="save_button")
        yield Button("Cancel", id="cancel_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "save_button":
            title = self.query_one("#title_input").value
            date = self.query_one("#date_input").value
            if self.query_one("#time_input").value == "":
                time = "All-day"
            else:
                time = self.query_one("#time_input").value
            description = self.query_one("#description_input").value
            data = {
                "title": title,
                "date": date,
                "time": time,
                "description": description
            }
            jm.Add(data)
            self.remove()

            table = self.app.query_one("#events_table")
            search = self.app.query_one("#search_input")

            table.display = True
            search.display = True

            self.app.refreshTable()
        elif event.button.id == "cancel_button":
            self.remove()

            table = self.app.query_one("#events_table")
            search = self.app.query_one("#search_input")

            table.display = True
            search.display = True

if __name__ == "__main__":
    app = Calendar()
    app.run()