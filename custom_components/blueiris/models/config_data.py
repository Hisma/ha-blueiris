from ..helpers.const import *


class ConfigData:
    host: str
    port: int
    ssl: bool
    username: str
    password: str
    password_clear_text: str
    exclude_system_camera: bool

    def __init__(self):
        self.host = ""
        self.port = 0
        self.ssl = False
        self.username = ""
        self.password = ""
        self.password_clear_text = ""
        self.exclude_system_camera = False

    @property
    def protocol(self):
        protocol = PROTOCOLS[self.ssl]

        return protocol

    @property
    def has_credentials(self):
        has_username = self.username and len(self.username) > 0
        has_password = self.password_clear_text and len(self.password_clear_text) > 0

        has_credentials = has_username or has_password

        return has_credentials
