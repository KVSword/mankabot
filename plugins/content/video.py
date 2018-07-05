from handler.base_plugin import BasePlugin
import random

class VideoPlugin(BasePlugin):
    __slots__ = ("prefixes", "video_commands", "music_commands")

    def __init__(self, video_commands=None, music_commands=None, prefixes=("!", "бот")):
       """Answers with a message it received."""
	
       super().__init__()
	
       self.prefixes = prefixes
       self.video_commands = video_commands or ["видео"]
       self.music_commands = music_commands or ["музыка"]
	
       self.description = ["разное", f"{self.prefixes[0]}{self.video_commands[0]} - поиск видео", "\n"
       "музыка", f"{self.prefixes[1]}{self.music_commands[1]} - поиск музыки", "\n" ]
	
    async def check_messages(self, msg):
        current_text = msg.text
        has_prefix = False
        for pref in self.prefixes:
            if current_text.startswith(pref):
                current_text = current_text.replace(pref, "", 1)
                has_prefix = True
                break

        if current_text in self.video_commands and has_prefix:
            msg.meta["__cmd"] = "video"

        elif current_text in self.music_commands and has_prefix:
            msg.meta["__cmd"] = "music"

        return "__cmd" in msg.meta 
    async def process_message(self, msg):
        if msg.meta["__cmd"] == "video":
           data = await self.api.video.search(
               q=self.parse_message(msg, full_text=False)[1] or "anime.webm jojo",
               sort=5,
               count=10,
               adult=10,
               offset= random.randint(1, 300)
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
        if msg.meta["__cmd"] == "music":
           data = await self.api.video.search(
               q=self.parse_message(msg, full_text=False)[1] or "neta",
               sort=5,
               count=10,
               adult=10,
               offset= random.randint(1, 300)
           )

           if not data or not data.get("items"):
               return await msg.answer("Я не могу получить песню!")

           return await msg.answer(
               'Приятного пролушивания!',
               attachment=','.join(
                   f"audio{vid['owner_id']}_{vid['id']}"
                       for vid in data["items"]
               )
           )