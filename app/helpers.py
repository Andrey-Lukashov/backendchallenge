import re
import datetime

UK_POSTCODE_PATTERN = r'\b[A-Z]{1,2}[0-9][A-Z0-9]?( )?[0-9][ABD-HJLNP-UW-Z]{2}\b'


def check_missing(format, data, field):
    """
    Checks if specific key is missing from return data

    :param format: either args or list
    :param data: received request data
    :param field: name of field we're looking for
    :return: field value
    :raises Exception: if field is missing
    """
    if format == "args":
        if field in data.args.keys():
            return data.args.get(field)
        else:
            raise Exception({"status_code": 400, "message": "Missing " + field})
    if format == "list":
        if field in data.keys():
            return data[field]
        else:
            raise Exception({"status_code": 400, "message": "Missing " + field})


def validate_year(year):
    """
    Validates if the given int is a correct year number

    :param year: allegedly a year we want to validate
    :return: year as integer
    :raises Exception: if year is invalid
    """
    try:
        int(year)  # try convert it to int
        if len(str(year)) != 4:  # year has to be 4 chars long
            raise Exception({"status_code": 400, "message": "Invalid year"})
        return year
    except Exception:
        raise Exception({"status_code": 400, "message": "Invalid year"})


def validate_int(number, field):
    """
    Checks if given number is an int

    :param number: number we want to validate
    :param field: name of the field we're validating
    :return: int
    :raises Exception: if it's not an int
    """
    try:
        number = int(number)
        return number
    except Exception:
        raise Exception({"status_code": 400, "message": "Invalid " + field})


def validate_string(string, field):
    """
    Checks if given field is a string

    :param string: value we want to validate
    :param field: name of the field we're validating
    :return: string
    :raises Exception: if it's not a string
    """
    if not isinstance(string, str):
        raise Exception({"status_code": 400, "message": "Invalid " + field})
    return string.lower()


def validate_postcode(postcode):
    """
    Validates given string as a postcode

    :param postcode: value we want to validate
    :return: string
    :raises Exception: if it's an invalid postcode
    """
    postcode = str(postcode)
    if len(postcode) > 8:  # postcodes can't be more than 8 digits
        raise Exception({"status_code": 400, "message": "Invalid postcode"})
    pattern = re.compile(UK_POSTCODE_PATTERN)  # check if matches postcode pattern
    if not pattern.match(postcode):
        raise Exception({"status_code": 400, "message": "Invalid postcode"})
    return postcode.lower()


def validate_dob(dob):
    """
    Validates date of birth

    :param dob: value we want to validate
    :return: string date of birth in m/d/Y format
    :raises Exception: if invalid date of birth
    """
    try:
        dob = datetime.datetime.strptime(dob, '%d/%m/%Y')
        min_age = datetime.timedelta(weeks=52 * 18)
        if datetime.datetime.now() - dob < min_age:  # must be 18 or over
            raise Exception({"status_code": 400, "message": "Invalid dob"})
        return dob.strftime('%m/%d/%Y')
    except Exception:
        raise Exception({"status_code": 400, "message": "Invalid dob"})


def validate_assigning(assigned_type, assigned_id):
    """
    Checks if we can assign this type to this id

    :param assigned_type:
    :param assigned_id:
    :return: list with type and id if passed validation
    :raises Exception: either type or id is invalid
    """
    from app.models import Branch, Driver

    # validate both as ints
    assigned_id = validate_int(assigned_id, 'assigned_id')
    assigned_type = validate_int(assigned_type, 'assigned_type')

    # only allow 1 and 2 to get through
    allowed_types = [1, 2]
    if assigned_type not in allowed_types:
        raise Exception({"status_code": 400, "message": "Invalid assigned_type"})

    if assigned_type == 1:  # 1 = driver
        # check if driver exists
        params = {"id": assigned_id}
        driver = Driver.get(params)
        if driver:
            assigned_id = driver.id
            return [assigned_type, assigned_id]
        else:
            raise Exception({"status_code": 404, "message": "Driver not found"})

    if assigned_type == 2:  # 2 = branch
        # check if branch exists
        params = {"id": assigned_id}
        branch = Branch.get(params)
        if branch:
            occupancy = branch.get_assigned_cars_count(assigned_id)
            if branch.capacity > occupancy:
                return [assigned_type, assigned_id]
            else:
                raise Exception({"status_code": 400, "message": "Branch has reached its capacity"})
        else:
            raise Exception({"status_code": 404, "message": "Branch not found"})
