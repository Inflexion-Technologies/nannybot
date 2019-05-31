from errbot import BotPlugin, botcmd, arg_botcmd, webhook


class ICII(BotPlugin):
    """
    icii notifications
    """

    @webhook
    def healthz(self, incoming_request):
        return "healthz"

    @webhook
    def message(self, req):
        self.send(self.build_identifier("#icam_corp_portal"), req["message"])

    @webhook
    def instruction(self, req):
        self.send_card(
            title="Instruction submitted",
            fields=req.items(),
            color="red" if req["Type"] == "Withdrawal" else "green",
        )

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def example(self, message, args):
        """A command which simply returns 'Example'"""
        return "Example"

    @botcmd()
    def hello_card(self, msg, args):
        """Say a card in the chatroom."""
        self.send_card(
            title="Title + Body",
            body="text body to put in the card",
            # thumbnail='https://raw.githubusercontent.com/errbotio/errbot/master/docs/_static/errbot.png',
            # image='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
            # link="http://www.google.com",
            fields=(("First Key", "Value1"), ("Second Key", "Value2")),
            color="red",
            in_reply_to=msg,
        )
