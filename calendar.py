from datetime import datetime


def get_events():
    """
    Returns upcoming calendar events
    formatted for the smart mirror.
    """

    # Temporary sample events
    events = [
        {
            "time": "9:30 AM",
            "title": "CJ 362"
        },
        {
            "time": "1:00 PM",
            "title": "Lunch"
        },
        {
            "time": "2:30 PM",
            "title": "CSE 420"
        },
        {
            "time": "7:30 PM",
            "title": "Gym"
        }
    ]

    # Get today's date
    today = datetime.now().strftime("%A, %B %d")

    event_lines = []

    for event in events:
        event_lines.append(
            f"{event['time']}  -  {event['title']}"
        )

    formatted_events = "\n\n".join(event_lines)

    return f"{today}\n\n{formatted_events}"