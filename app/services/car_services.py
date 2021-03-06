from sqlalchemy.sql.expression import true
from app.models.car_model import CarModel
from app.services.helpers import check_incorrect_keys, add_in_db, format_license_plate, commit_current_session, delete_in_db, format_query_car, format_url_car, check_user, transform_to_uppercase, format_phone_number
from app.exc.not_permission import NotPermission
from app.exc.not_found_error import NotFound


def post_car_by_data(data: dict, current_user : dict):
    check_user(data["user_id"], current_user)
    required_keys: list = ["year", "license_plate", "model", "trunk_volume", "insurer", "insurer_number", "review_date", "withdrawal_place", "city", "state", "user_id"]
    check_incorrect_keys(data, required_keys)
    license_plate_to_format = format_license_plate(data)
    insurer_number_to_format = format_phone_number(data["insurer_number"])
    
    data["insurer_number"] = insurer_number_to_format
    data["license_plate"] = license_plate_to_format

    data = transform_to_uppercase(data)

    car: CarModel = CarModel(**data)
    add_in_db(car)
    
    return car

def update_car_by_id(car_id: int, data: dict, current_user: dict):
    check_user(data["user_id"], current_user)
  
    data = transform_to_uppercase(data)
    
    car_to_update: CarModel = CarModel.query.get(car_id)
    
    if data.get("license_plate"): 
        license_plate_to_format = format_license_plate(data)
        car_to_update.license_plate = license_plate_to_format
        
    if data.get("insurer_number"):
        insurer_number_to_format = format_phone_number(data["insurer_number"])
        car_to_update.insurer_number = insurer_number_to_format

    for key, value in data.items():
        setattr(car_to_update, key, value)

    commit_current_session()
    
    return car_to_update

def delete_car_by_id(id, current_user): 
    car_to_delete = CarModel.query.get(id)

    if not car_to_delete:
        raise NotFound
    
    elif car_to_delete.user_id == current_user['user_id']:
        delete_in_db(car_to_delete)
        return ""

    raise NotPermission
    
def get_car_by_filters(**data):
    data = transform_to_uppercase(data)

    cars_list = []
    date_ocupied = []
    avaliations = []
    
    year, model, trunk_volume, withdrawal_place, city, state, page, per_page = format_query_car(data)
   
    cars = CarModel.query.filter(
        (CarModel.year==int(year) or True),
        CarModel.model.like(model),
        (CarModel.trunk_volume==int(trunk_volume) or True),
        CarModel.withdrawal_place.like(withdrawal_place),
        CarModel.city.like(city),
        CarModel.state.like(state)).paginate(int(page), int(per_page),error_out=False)

    next_url, prev_url = format_url_car(cars.has_next, cars.has_prev, cars.next_num, cars.prev_num, per_page, data)
    
    for item in cars.items:
        cars_list.append({"car": item, "date_ocupied": item.date_ocupied, "avaliations": item.record_lessee})
    print(cars_list)
    return  {"info": {"count": cars.total, "pages": cars.pages, "next_page": next_url, "prev_page": prev_url}, "result": cars_list }
    

def get_car_by_id(id):
    car = CarModel.query.get(id)

    if not car:
        raise NotFound


    elif car:
        return {"car": car, "date_ocupied": car.date_ocupied, "avaliations": car.record_lessee }
 
    raise NotFound
