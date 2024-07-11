import datetime

class EventObject:
    requiredParameters = ['gebeurteniscode', 'actiecode', 'utcisodatetime', 'identificatortype', 'identificator', 'aard']
    
    def __init__(self, **eventParameters) -> None:
        # Initialize with default empty values or with provided parameters
        for param in self.requiredParameters:
            setattr(self, param, eventParameters.get(param, None))
        
        if self.utcisodatetime is None:
            self.utcisodatetime = datetime.datetime.utcnow().isoformat()

    def update_parameters(self, **eventParameters) -> None:
        for param, value in eventParameters.items():
            setattr(self, param, value)

    def validate(self) -> None:
        missing_params = []
        for param in self.requiredParameters:
            if getattr(self, param) is None:
                missing_params.append(param)
        if len(missing_params) > 0:
            raise KeyError(f"Missing required parameters: {', '.join(missing_params)}")

class UserObject:
    requiredParameters = ['gebruikersnaam', 'gebruikersrol', 'weergave_gebruikersnaam']
    
    def __init__(self, **userParameters) -> None:
        # Initialize with default empty values or with provided parameters
        for param in self.requiredParameters:
            setattr(self, param, userParameters.get(param, None))

    def update_parameters(self, **userParameters) -> None:
        for param, value in userParameters.items():
            setattr(self, param, value)

    def validate(self) -> None:
        missing_params = []
        for param in self.requiredParameters:
            if getattr(self, param) is None:
                missing_params.append(param)
        if len(missing_params) > 0:
            raise KeyError(f"Missing required parameters: {', '.join(missing_params)}")
        

class CustomObject:
    def __init__(self, **customParameters) -> None:
        for param in customParameters:
            setattr(self, param, customParameters[param])

if __name__ == '__main__':
    event = EventObject()
    event.update_parameters(aard='test')
    event.update_parameters(identificatortype='test2')
    # event.validate()
    print(event.__dict__)
    pass