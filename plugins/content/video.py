from handler.base_plugin_command import CommandPlugin


class VideoPlugin(CommandPlugin):
    __slots__ = (1, 2)

    def __init__(self, *commands, prefixes=None, strict=False):
        super().__init__(*commands, prefixes=prefixes, strict=strict)

        self.description = [
            "Видео", f"{self.command_example(1)} [запрос] - поиск видео по запросу"
			"Музыка", f"{self.command_example(2)} [запрос] - поиск музыки "
        ]

    async def process_message(self, msg):
        data = await self.api.video.search(
            q=self.parse_message(msg, full_text=False)[1] or "anime.webm Jojo",
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
                f"audio{vid['owner_id']}_{vid['id']}"
                    for vid in data["items"]
            )
        )
