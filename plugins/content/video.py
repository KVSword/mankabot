from handler.base_plugin_command import CommandPlugin
from handler.base_plugin import BasePlugin
from vk.helpers import parse_user_id

import peewee_async, peewee, asyncio, random, time

class VideoPlugin(CommandPlugin):
    __slots__ = ("commands", "prefixes", "models", "pwmanager", "active")

    def __init__(self, prefixes=("",), video="видео", music="музыка", hentai="хентай", postprefix=""):

        super().__init__()

        self.commands = [(postprefix + " " if postprefix else "") + c.lower() for c in (video, music, hentai,)]  # [-1] == [10]
        self.prefixes = prefixes

        self.description = [" \Разное\"",
		                    f"{self.prefixes[0]}{self.commands[0]} - поиск видео n\""
                            f"{self.prefixes[0]}{self.commands[1]} - поиск музыки "]
    async def check_message(self, msg):
        prefix = None
        pltext = ""

        for p in self.prefixes:
            if msg.full_text.startswith(p):
                prefix = p
                pltext = msg.full_text.replace(p, "", 1)
                break

        if prefix is None:
            return False

        for c in self.commands:
            if pltext.startswith(c + " ") or pltext.startswith(c + "\n") or pltext == c:
                break
        else:
            return False

        msg.meta["__prefix"] = prefix
        msg.meta["__pltext"] = pltext

        return True

    async def process_message(self, msg):
        if msg.meta["__pltext"].lower() == self.commands[1]:
            video, music, hentai = self.commands
            p = self.prefixes[0]
        data = await self.api.video.search(
            q=self.parse_message(msg, full_text=True)[1] or "anime.webm Jojo",
            sort=10,
            count=10,
            adult=10
        )

        if not data or not data.get("items"):
           return await msg.answer("Я не могу получить видео или ничего не нашлось!")

        return await msg.answer(
            'Приятного просмотра!',
            attachment=','.join(
                f"video{vid['owner_id']}_{vid['id']}"
                    for vid in data["items"]
            )
        )
		if msg.meta["__pltext"].lower() == self.commands[2]:
            p = self.prefixes[0]
        data = await self.api.video.search(
            q=self.parse_message(msg, full_text=True)[1] or "anime.webm Jojo",
            sort=10,
            count=10,
            adult=10
        )

        if not data or not data.get("items"):
           return await msg.answer("Я не могу получить видео или ничего не нашлось!")

        return await msg.answer(
            'Приятного просмотра!',
            attachment=','.join(
                f"video{vid['owner_id']}_{vid['id']}"
                    for vid in data["items"]
            )
        )