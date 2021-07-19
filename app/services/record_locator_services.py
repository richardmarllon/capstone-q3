from http import HTTPStatus
from app.models.record_locator_model import RecordLocatorModel
from app.models.user_locator_model import UserLocatorModel
from app.services.helpers import check_incorrect_keys, check_missing_keys, add_in_db
from http import HTTPStatus


def to_asses_locator(data:dict):

    required_keys = ["comment", "user_locator_id", "user_lessee_id", "date", "avaliation"]
    
    check_missing_keys(data, required_keys)
    check_incorrect_keys(data, required_keys)

    assess_locator = RecordLocatorModel(**data)
    add_in_db(assess_locator)
    resp = assess_locator

    return resp, HTTPStatus.CREATED



def get_avaliation_locator(user_id:int):
    # name_locator = UserLocatorModel.query.get(user_id)
    user_locator = RecordLocatorModel.query.get(user_id)

    return user_locator

def update_record_locator(data:dict, record_id:int):
    record_locator_updt = RecordLocatorModel.query.get(record_id)

    for key, value in data.items():
        setattr(record_locator_updt, key, value)
    
    add_in_db(record_locator_updt)

    return record_locator_updt, HTTPStatus.OK