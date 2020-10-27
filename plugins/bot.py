from disco.bot import Plugin


class SimplePlugin(Plugin):
    @Plugin.listen('ChannelCreate')
    def on_channel_create(self, event):
        event.channel.send_message('Sick channel dude.')

    @Plugin.command('ping')
    def on_ping_command(self, event):
        event.msg.reply('Fuck off.')

    @Plugin.command('echo', '<content:str...>')
    def on_echo_command(self, event, content):
        event.msg.reply(content)
