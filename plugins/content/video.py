from handler.base_plugin_command import CommandPlugin
from handler.base_plugin_command import CommandPlugin
from vk.helpers import parse_user_id
from utils import plural_form

import asyncio, re


class VideoPlugin(CommandPlugin):
    __slots__ = ("command_groups",)

    def __init__(self, audio_commands=None, video_commands=None, prefixes=None, strict=False):
        """This plugin allows users to do votes in chats with ability to kick someone with votekick"""

        if not audio_commands:
            audio_commands = ["music", "музыка"]

        if not video_commands:
            video_commands = ["video", "видео"]

        super().__init__(*(video_commands + audio_commands), prefixes=prefixes, strict=strict)

        self.command_groups = video_commands, audio_commands
        p = self.prefixes[-1]
        self.description = [f"Видео и музыка"
                            f"{p}{video_commands[0]} [запрос] - поиск музыки "
							f"{p}{audio_commands[0]} [запрос] - поиск видео по запросу"
        ]

    async def process_message(self, msg):
		
        if command in self.command_groups[0]:
         data = await self.api.video.search(
            q=self.parse_message(msg, full_text=False)[2] or "anime.webm Jojo",
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
		
	    if command in self.command_groups[1]:
          data = await self.api.audio.search(
		  q=self.parse_message(msg, full_text=True)[1] or "Imagine Drgons"
		  sort=10
		  count=10
		  adult=10
		  )
		
		if not data or not data.get("items")
		     return await msg.answer("бот или админ ретард который не может нормально сделать плагин")
			 
	            return await msg.answer(
            'Приятного прослушивания!',
            attachment=','.join(
                f"audio{vid['owner_id']}_{vid['id']}"
                    for vid in data["items"]
            )
        )
        		
