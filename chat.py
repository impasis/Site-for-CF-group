from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.session import run_js, run_async

import asyncio


class Chat:
    def __init__(self):
        self.users = set()
        self.messages = []

    def check(self, name):
        if name in self.users:
            return "This name is taken!"
        elif name == "":
            return "Write a name"

    async def main(self):
        def logout():
            run_js('window.location.reload()')
            self.users.discard(username)
            self.messages.append(("📢", f"`{username}` left the group!"))
            box.append(put_markdown(f"📢: `{username}` left the group!"))

        put_markdown("## Our Chat")

        box = output()
        put_scrollable(box, height=300, keep_bottom=True)

        username = await input("Your Name", required=True, validate=self.check)
        self.users.add(username)

        run_async(self.enum_messages(username, box))

        self.messages.append(("📢", f"`{username}` join the group!"))
        box.append(put_markdown(f"📢: `{username}` join the group!"))
        put_button("Log out", onclick=logout)

        while True:
            message = await input(placeholder="Write a message...", validate=check_message)

            self.messages.append((username, message))
            box.append(put_markdown(f"`{username}`: {message}"))

    async def enum_messages(self, username, box):

        while True:
            i = len(self.messages)
            await asyncio.sleep(1)

            for el in self.messages[i:]:
                if el[0] != username:
                    box.append(put_markdown(f"`{el[0]}`: {el[1]}"))

            if len(self.messages) >= 1000:
                self.messages = self.messages[500:]

    def run(self):
        start_server(self.main, debug=True, port=5173, cdn=False)


def check_message(message):
    if message == "":
        return "Write a message"


chat = Chat()
chat.run()
