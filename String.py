import pyrogram

app = pyrogram.Client(
    "session_name",
    22731079,
    "40f6f6599de18cdedc025fab927bb16b",
    in_memory=True
)

app.start()

string_session = app.export_session_string()

app.send_message("me", f"`{string_session}`")

print("\n\nCHECK SAVED MESSAGES")
