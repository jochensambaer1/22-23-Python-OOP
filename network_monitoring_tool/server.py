class Server:
    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address
        self.status = None

    def ping(self):
        # implement ping logic here, for example using the ping library
        # return True if ping succeeds, False otherwise
        pass

    def check_status(self):
        if self.ping():
            self.status = "online"
        else:
            self.status = "offline"

    def to_dict(self):
        return {"name": self.name, "ip_address": self.ip_address, "status": self.status}
