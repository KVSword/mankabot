from handler.base_plugin_command import CommandPlugin

class VideoPlugin(CommandPlugin):
    __slots__ = ("commands", "prefixes", "models", "pwmanager", "active")

    def __init__(self, prefixes=("",), video="видео", music="музыка", hentai="хентай", postprefix=""):

        super().__init__()

        self.commands = [(postprefix + " " if postprefix else "") + c.lower() for c in (video, music, hentai,)]  # [-1] == [10]
        self.prefixes = prefixes

        self.description = [" \Разное\"",
		                    f"{self.prefixes[0]}{self.commands[0]} - поиск видео n\""
                            f"{self.prefixes[0]}{self.commands[1]} - поиск музыки "]

    async def process_message(self, msg):
        if msg.meta["__pltext"].lower() == self.commands[0]:
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