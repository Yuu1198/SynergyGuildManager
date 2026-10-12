class GuildMember:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name

    def __repr__(self):
        return f"GuildMember(name={self.name}, class_name={self.class_name}))"