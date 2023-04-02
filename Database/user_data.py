class UserData :
    
    def __init__(
            self,
            username : str,
            password : str,
            eventimEmail : str,
            eventimPassword : str
            ) -> None :
        self.username = username
        self.password = password
        self.eventimEmail = eventimEmail
        self.eventimPassword = eventimPassword

    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return "\nUserData:\n\tusername: {}\n\tpassword: {}\n\teventimEmail: {}\n\teventimPassword: {}".format(
            self.username,
            self.password,
            self.eventimEmail,
            self.eventimPassword
        )
    
    def __eq__(self, __value: object) -> bool:
        result = self.username == __value.username
        result = result and self.password == __value.password
        result = result and self.eventimEmail == __value.eventimEmail
        result = result and self.eventimPassword == __value.eventimPassword
        return result