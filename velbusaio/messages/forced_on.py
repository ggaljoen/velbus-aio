"""
:author: Maikel Punie <maikel.punie@gmail.com>
"""
from velbusaio.command_registry import register_command
from velbusaio.message import Message

COMMAND_CODE = 0x14


class ForcedOn(Message):
    def populate(self, priority, address, rtr, data):
        """
        :return: None
        """
        self.needs_low_priority(priority)
        self.needs_no_rtr(rtr)
        self.set_attributes(priority, address, rtr)

    def data_to_binary(self):
        """
        :return: bytes
        """
        return bytes([COMMAND_CODE])


register_command(COMMAND_CODE, ForcedOn)
