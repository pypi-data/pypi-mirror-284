import arrow.arrow as arrow
import calendar
import dateutil
import ics.event
import ics.icalendar
import requests

TIMEEDIT_EVENTS = [
    "Datorlaboration",
    "Computer lab",
    "Examination",
    "Exkursion",
    "Excursion",
    "Fältövning",
    "Field exercise",
    "Frågestund",
    "Question time",
    "Question Time",
    "Föreläsning",
    "Lecture",
    "FX-komplettering",
    "FX-completion",
    "Handledning",
    "Tutorial",
    "Information",
    "Kontrollskrivning",
    "Partial Exam/Quiz",
    "Laboration",
    "Lab",
    "Lektion",
    "Lesson",
    "Omtenta",
    "Re-exam",
    "Re-Exam",
    "Presentation",
    "Projektarbete",
    "Project work",
    "Project Work",
    "Redovisning",
    "Reporting",
    "Räknestuga",
    "Math work session",
    "Seminarium",
    "Seminar",
    "Samverkansinlärning",
    "Supplemental instruction",
    "Supplemental Instruction",
    "Studiebesök",
    "Study visit",
    "Tentamen",
    "Exam",
    "Upprop",
    "Roll-call",
    "Webinarium",
    "Webinar",
    "Verksamhetsförlagd utbildning",
    "Pre-service Placement",
    "Workshop",
    "Övning",
    "Exercise",
]


def format_header(event, week=True):
    """
    Formats the event header, a one-line representation (week, date, time,
    event title)

    If the `week` parameter is `True` (default), the week number and weekday
    will be included in the header.
    """
    header = ""

    if week:
        header += (
            f"Week {event.begin.isocalendar()[1]} "
            + calendar.day_name[event.begin.weekday()]
            + " "
        )

    header += event.begin.to(dateutil.tz.tzlocal()).format("DD/MM HH:mm")

    header += f" {event.name}"

    return header


def format_event(event, week=True):
    """
    Takes event (ics.event.Event) object,
    returns long string representation (header, location, description over
    several lines)

    The `week` parameter is passed to the `format_header` function, it results
    in the week number and day being included in the header. Default is `True`.
    """
    header = format_header(event, week)
    location = event.location
    description = "\n".join(
        filter(lambda x: "http" not in x, event.description.splitlines())
    )

    return f"{header}\n{location}\n{description}".strip()


def filter_event_description(
    event_desc, ignore=["http", "grupp", "group", "ID ", "Daniel Bosk"], separator="; "
):
    """
    Takes event description event_desc as string,
    returns filtered string with newlines replaced by semicolons.
    Rows of description containing any term in list ignore, will not appear in
    the returned string.
    The filtered rows of the description are joined again by the string in
    separator.
    """
    desc_parts = event_desc.splitlines()
    desc_parts_keep = []

    for part in desc_parts:
        found = False
        for term in ignore:
            if term in part:
                found = True
                break

        if not found:
            desc_parts_keep.append(part)

    return separator.join(desc_parts_keep)


def format_event_short(event, week=False):
    """
    Takes event (ics.event.Event) object,
    returns a short string representation (one line)

    The `week` parameter is passed to the `format_header` function, it results
    in the week number and day being included in the header. Default is
    `False`.
    """
    header = format_header(event, week)
    description = filter_event_description(event.description)

    return f"{header} {description}".strip()


def format_event_csv(event, week=False, location=False):
    """
    Takes event (ics.event.Event) object,
    returns a list of strings, which can be used as a row in a CSV file.

      [0] Week number and day (if week is True)
      [1] Date and time
      [2] Event name
      [3] Location (if location is True)
      [4] Description

    The `week` parameter set to True results in the week number and day being
    included at index 0. Default is `False`.

    The `location` parameter set to True results in the location being included
    at index 2. Default is `False`.
    """
    row = []

    if week:
        row.append(
            f"Week {event.begin.isocalendar()[1]} "
            + calendar.day_name[event.begin.weekday()]
        )

    row.append(event.begin.to(dateutil.tz.tzlocal()).format("DD/MM HH:mm"))
    row.append(event.name)

    if location:
        row.append(event.location)

    description = filter_event_description(event.description, separator="; ")
    row.append(description)

    return row


def read_calendar(url):
    """
    Input: url is a string containing the URL to the ICS-formatted calendar.
    Output: an [[ics.icalendar.Calendar]] object.
    """
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return ics.icalendar.Calendar(imports=response.text)
    raise Exception(response.text)


def event_filter(events, whitelisted=TIMEEDIT_EVENTS):
    """
    Takes a list of events (ics.event.Event), returns a filtered list of events
    (generator). The events to include are the teaching events.

    It covers the following events:

      "Datorlaboration", "Computer lab",
      "Examination",
      "Exkursion", "Excursion",
      "Fältövning", "Field exercise",
      "Frågestund", "Question time", "Question Time",
      "Föreläsning", "Lecture",
      "FX-komplettering", "FX-completion",
      "Handledning", "Tutorial",
      "Information",
      "Kontrollskrivning", "Partial Exam/Quiz",
      "Laboration", "Lab",
      "Lektion", "Lesson",
      "Omtenta", "Re-exam", "Re-Exam",
      "Presentation",
      "Projektarbete", "Project work", "Project Work",
      "Redovisning", "Reporting",
      "Räknestuga", "Math work session",
      "Seminarium", "Seminar",
      "Samverkansinlärning", "Supplemental instruction",
      "Supplemental Instruction",
      "Studiebesök", "Study visit",
      "Tentamen", "Exam",
      "Upprop", "Roll-call",
      "Webinarium", "Webinar",
      "Verksamhetsförlagd utbildning", "Pre-service Placement",
      "Workshop",
      "Övning", "Exercise"
    """
    for event in events:
        for event_type in whitelisted:
            if event_type in event.name:
                yield event
                break
