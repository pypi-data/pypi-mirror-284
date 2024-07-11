import datetime

class EventObject:
    """
    A class representing an event with required parameters and validation.

    Attributes
    ----------
    gebeurteniscode : Optional[str]
        Code representing the event.
    actiecode : Optional[str]
        Code representing the action.
    utcisodatetime : Optional[str]
        Timestamp in ISO format, defaults to current UTC time if not provided.
    identificatortype : Optional[str]
        Type of the identifier.
    identificator : Optional[str]
        The identifier itself.
    aard : Optional[str]
        Nature or type of the event.

    Methods
    -------
    update_parameters(**eventParameters)
        Update the attributes of the event with provided parameters.
    validate()
        Validate that all required parameters are set.
    """
    
    requiredParameters = ['gebeurteniscode', 'actiecode', 'utcisodatetime', 'identificatortype', 'identificator', 'aard']
    
    def __init__(self, **eventParameters) -> None:
        """
        Initialize an EventObject with optional parameters.

        Parameters
        ----------
        **eventParameters : dict
            An optional dictionary of event parameters.
            Can include 'gebeurteniscode', 'actiecode', 'utcisodatetime',
            'identificatortype', 'identificator', and 'aard'.
        """
        # Initialize with default empty values or with provided parameters
        for param in self.requiredParameters:
            setattr(self, param, eventParameters.get(param, None))
        
        if self.utcisodatetime is None:
            self.utcisodatetime = datetime.datetime.utcnow().isoformat()

    def update_parameters(self, **eventParameters) -> None:
        """
        Update existing event parameters.

        Parameters
        ----------
        **eventParameters : dict
            A dictionary of event parameters to update.
        """
        for param, value in eventParameters.items():
            setattr(self, param, value)

    def validate(self) -> None:
        """
        Validate that all required parameters are set.

        Raises
        ------
        KeyError
            If any required parameter is missing.
        """
        missing_params = []
        for param in self.requiredParameters:
            if getattr(self, param) is None:
                missing_params.append(param)
        if len(missing_params) > 0:
            raise KeyError(f"Missing required parameters: {', '.join(missing_params)}")

class UserObject:
    """
    A class representing a user with required parameters and validation.

    Attributes
    ----------
    gebruikersnaam : Optional[str]
        Username of the user.
    gebruikersrol : Optional[str]
        Role of the user.
    weergave_gebruikersnaam : Optional[str]
        Display name of the user.

    Methods
    -------
    update_parameters(**userParameters)
        Update the attributes of the user with provided parameters.
    validate()
        Validate that all required parameters are set.
    """
    requiredParameters = ['gebruikersnaam', 'gebruikersrol', 'weergave_gebruikersnaam']
    
    def __init__(self, **userParameters) -> None:
        """
        Initialize a UserObject with optional parameters.

        Parameters
        ----------
        **userParameters : dict
            An optional dictionary of user parameters.
            Can include 'gebruikersnaam', 'gebruikersrol',
            and 'weergave_gebruikersnaam'.
        """
        # Initialize with default empty values or with provided parameters
        for param in self.requiredParameters:
            setattr(self, param, userParameters.get(param, None))

    def update_parameters(self, **userParameters) -> None:
        """
        Update existing user parameters.

        Parameters
        ----------
        **userParameters : dict
            A dictionary of user parameters to update.
        """
        for param, value in userParameters.items():
            setattr(self, param, value)

    def validate(self) -> None:
        """
        Validate that all required parameters are set.

        Raises
        ------
        KeyError
            If any required parameter is missing.
        """
        missing_params = []
        for param in self.requiredParameters:
            if getattr(self, param) is None:
                missing_params.append(param)
        if len(missing_params) > 0:
            raise KeyError(f"Missing required parameters: {', '.join(missing_params)}")
        

class CustomObject:
    """
    A class for creating objects with custom parameters.

    Methods
    -------
    None
    """
    
    def __init__(self, **customParameters) -> None:
        """
        Initialize a CustomObject with custom parameters.

        Parameters
        ----------
        **customParameters : dict
            A dictionary of custom parameters.
        """
        for param in customParameters:
            setattr(self, param, customParameters[param])

if __name__ == '__main__':
    event = EventObject()
    event.update_parameters(aard='test')
    event.update_parameters(identificatortype='test2')
    # event.validate()
    print(event.__dict__)
    pass