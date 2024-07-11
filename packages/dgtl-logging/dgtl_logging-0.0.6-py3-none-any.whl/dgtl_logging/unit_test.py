from dgtl_logging.dgtl_logging import CustomObject, EventObject, UserObject

def test_create_event_object_without_req_params():
    try:
        EventObject(test='test')
    except KeyError:
        assert True
    except Exception as e:
        raise(e)

def test_create_event_object_valid():
    event = EventObject(
        gebeurteniscode='geb_test',
        actiecode='test',
        utcisodatetime='test',
        aard='test')
    assert event.gebeurteniscode == 'geb_test'

def test_event_object():
    # Check that the utcisodatetime is not overwritten during initiation

    event = EventObject(utcisodatetime='2023-10-10T00:00:00Z')
    event.update_parameters(gebeurteniscode='code1')
    event.update_parameters(actiecode='action1')
    event.update_parameters(identificatortype='type1', identificator='id1', aard='typeA')
    event.validate()
    
    assert event.utcisodatetime == '2023-10-10T00:00:00Z'
    
def test_user_object():
    user = UserObject(gebruikersnaam='user1')
    user.update_parameters(gebruikersrol='admin')
    user.update_parameters(autorisatieprotocol='protocol1', weergave_gebruikersnaam='User One')
    
    user.validate()

    assert user.autorisatieprotocol == 'protocol1'

def test_overwrite_entry():
    user = UserObject(gebruikersnaam='user1')
    user.update_parameters(gebruikersnaam='user2')

    assert user.gebruikersnaam == 'user2'


if __name__ == '__main__':
    pass
