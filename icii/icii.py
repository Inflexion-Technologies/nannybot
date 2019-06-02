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
        room = req.get("_room")
        self.send(self.build_identifier(room) if room else None, req["message"])

    @webhook
    def instruction(self, req):
        room = req.get("_room")
        self.send_card(
            to=self.build_identifier(room) if room else None,
            title="Instruction submitted",
            fields=(i for i in req.items() if not i[0].startswith("_")),
            color="red" if req["Type"] == "Withdrawal" else "green",
        )
