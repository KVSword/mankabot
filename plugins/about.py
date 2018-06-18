from handler.base_plugin_command import CommandPlugin
from vk.data import Message


class AboutPlugin(CommandPlugin):
    __slots__ = ("version", )

    def __init__(self, *commands, prefixes=None, strict=False, version=7.3):
        """Answers with information about bot."""

        super().__init__(*commands, prefixes=prefixes, strict=strict)

        self.version = version

        self.set_description()

    def set_description(self):
        example = self.command_example()
        self.description = [f"О боте",
                            f"Вывод информации о боте.",
                            f"{example} - вывести информацию."]

    async def process_message(self, msg: Message):
        message = "" \
                  "Jotaro - бот, способный выполнять очень сложные задачи, команды. На основе этого бота " \
                  "можно строить очень сложные системы и сервисы. Этот бот очень надёжен и стабилен - обрабатывает " \
                  "очень многие ошибки и избегает их. Бот обновляется, обретает новые плагины и т.д.\n" \
                  "" \
                  "" \
                  ""

        return await msg.answer(message)
