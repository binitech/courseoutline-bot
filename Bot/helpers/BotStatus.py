from Bot import bot


def status():

    TEXT = f"Total Bot Users: " \
           f"\nActive Users: " \
           f"\nDead Users: " \
           f"\nTotal Courses: " \
           f"\nTotal Materials: "
    return TEXT


async def log(event):
    TEXT = f"""**-----------LOG-----------**
🆔 {event.from_user.id} ( [{event.from_user.first_name}](tg://user?id={event.from_user.id}) )
🤖 {event.from_user.is_bot}
👤 {event.from_user.first_name}
➡️ {event.from_user.last_name}
🌀 @{event.from_user.username}

   **{event.text}**"""
    await bot.send_message(-619480714, TEXT, parse_mode="MARKDOWN")