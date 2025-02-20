"""
:author: Thomas Delaet <thomas@delaet.org>
"""
import json

from velbusaio.command_registry import register_command
from velbusaio.message import Message

COMMAND_CODE = 0xF1


class ChannelNamePart2Message(Message):
    """
    send by: VMB6IN, VMB4RYLD
    received by:
    """

    def __init__(self, address=None):
        Message.__init__(self)
        self.channel = 0
        self.name = ""
        self.set_defaults(address)

    def populate(self, priority, address, rtr, data):
        """
        :return: None
        """
        self.needs_low_priority(priority)
        self.needs_no_rtr(rtr)
        self.needs_data(data, 7)
        self.set_attributes(priority, address, rtr)
        channels = self.byte_to_channels(data[0])
        self.needs_one_channel(channels)
        self.channel = channels[0]
        self.name = "".join([chr(x) for x in data[1:]])

    def data_to_binary(self):
        """
        :return: bytes
        """
        return bytes([COMMAND_CODE, self.channels_to_byte([self.channel])]) + bytes(
            self.name, "ascii", "ignore"
        )

    def to_json(self):
        """
        :return: str
        """
        json_dict = self.to_json_basic()
        json_dict["channel"] = self.channel
        return json.dumps(json_dict)


class ChannelNamePart2Message2(ChannelNamePart2Message):
    """
    send by: VMBGP*
    received by:
    """

    def populate(self, priority, address, rtr, data):
        """
        :return: None
        """
        self.needs_low_priority(priority)
        self.needs_no_rtr(rtr)
        self.needs_data(data, 7)
        self.set_attributes(priority, address, rtr)
        self.channel = data[0]
        self.name = "".join([chr(x) for x in data[1:]])


class ChannelNamePart2Message3(ChannelNamePart2Message):
    """
    send by: VMBGP*
    received by:
    """

    def populate(self, priority, address, rtr, data):
        """
        :return: None
        """
        self.needs_low_priority(priority)
        self.needs_no_rtr(rtr)
        self.needs_data(data, 5)
        self.set_attributes(priority, address, rtr)
        self.channel = (data[0] >> 1) & 0x03
        self.name = "".join([chr(x) for x in data[1:]])


register_command(COMMAND_CODE, ChannelNamePart2Message)
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBGP1")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBEL1")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBGP1-2")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBGP2")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBEL2")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBGP2-2")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBGP4")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBEL4")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBGP4-2")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBGPO")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBGPOD")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBGPOD-2")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBELO")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBGP4PIR")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBDMI")
register_command(COMMAND_CODE, ChannelNamePart2Message2, "VMBDMI-R")
register_command(COMMAND_CODE, ChannelNamePart2Message3, "VMB1BL")
register_command(COMMAND_CODE, ChannelNamePart2Message3, "VMB2BL")
