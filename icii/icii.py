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

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def example(self, message, args):
        """A command which simply returns 'Example'"""
        return "Example"
