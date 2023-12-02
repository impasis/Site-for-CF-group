from pywebio.output import *
from pywebio.input import *
from pywebio import start_server
from pywebio.session import run_js

import webbrowser


def check_name(name):
    if name in users:
        return "The name is already in use"
    elif name == "":
        return "You can't keep an empty name"


def open_chat():
    webbrowser.open_new("host")  # every running new!


async def main():
    def logout():
        users.discard(username)
        run_js('window.location.reload()')

    msg_box = output()
    put_scrollable(msg_box, height=500, keep_bottom=True)

    username = await input("Name:", validate=check_name)
    users.add(username)

    put_button("Log out", onclick=logout)
    put_button("Chat", onclick=open_chat)
    msg_box.append(put_markdown(f"{group_description}"))

    msg_box.append(put_markdown("## Наши проекты: "))
    msg_box.append(put_link("Text-Editor-For-C++", "https://github.com/impasis/Text-Editor-For-C-"))
    msg_box.append("")
    msg_box.append(put_link("Algorithms", "https://github.com/impasis/Algorithms"))
    msg_box.append("")
    msg_box.append(put_link("Online Chat", "https://github.com/impasis/Online-Chat"))
    msg_box.append("")
    msg_box.append(put_link("This Site", "https://github.com/impasis/Site-for-CF-group"))
    msg_box.append(put_markdown("## Техподдержка: "))
    msg_box.append(put_html("<a href='mailto:lolkek99800@gmail.com'>lolkek99800@gmail.com</a>"))


users = set()
group_description = """
Группа "О, Хавчик!" предоставляет отличную возможность для общения и поиска новых друзей среди единомышленников.
Участники группы активно обсуждают и анализируют различные алгоритмические задачи, делятся своими 
решениями, а также предлагают советы и рекомендации другим участникам. Кроме того, в группе можно найти полезные 
материалы по программированию и алгоритмам, которые помогут в улучшении навыков."""

if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)
