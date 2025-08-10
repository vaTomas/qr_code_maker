class Tag:
  def __init__(self, name, email, type):
    self.name = name
    self.email = email
    self.type = type

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(
        self, value: str
    ) -> None:
        self._name = value

    @property
    def email(self) -> str:
        return self._email

    @name.setter
    def email(
        self, value: str
    ) -> None:
        self._email = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(
        self, value: str
    ) -> None:
        self._type = value