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
