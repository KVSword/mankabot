from handler.base_plugin_command import CommandPlugin


class VideoPlugin(CommandPlugin):
    __slots__ = ("command_groups",)

    def __init__(self, vote_commands=None,  vote_undo_commands=None, votekick_commands=None, prefixes=None, strict=False):
        """This plugin allows users to do votes in chats with ability to kick someone with votekick"""

        if not vote_commands:
            vote_commands = ["vote", "+"]

        if not vote_undo_commands:
            vote_undo_commands = ["unvote", "-"]

        super().__init__(*(video_commands + audio_commands), prefixes=prefixes, strict=strict)

        self.command_groups = video_commands, audio_commands
        self.votes = {}

        p = self.prefixes[-1]
        self.description = [f"Видео и музыка"
                            f"{p}{video_commands[0]} [запрос] - поиск музыки "
							f"{p}{audio_commands[0]} [запрос] - поиск видео по запросу"
        ]

    async def process_message(self, msg):
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
	async def process_message(self, msg):
        data = await self.api.audio.search(
		q=self.parse_message(msg, full_text=True)[1] or "Imagine Drgons"
		sort=10
		count=10
		adult=10
		)
		
		if not data or not data.get("items")
		     return await msg.answer("бот или админ ретард который не может нормально сделать плагин")
        		
