import json


def are_vital_signs_normal(blood_pressure, oxygen_level, body_temperature):
    temperature = is_body_temperature_normal(body_temperature)
    pressure = is_blood_pressure_normal(blood_pressure)
    level = is_oxygen_level_normal(oxygen_level)

    if temperature and pressure and level:
        return True
    else:
        return False


def is_body_temperature_normal(temperature):
    if temperature >= 36 and temperature <= 37:
        return True
    else:
        return False


def is_blood_pressure_normal(pressure):
    pressure = json.loads(pressure)

    if (int(pressure[0]) >= 100 and int(pressure[1]) > 60 and
            int(pressure[0]) <= 130 and int(pressure[1]) < 85):
        return True
    else:
        return False


def is_oxygen_level_normal(level):
    if level > 89:
        return True
    else:
        return False
