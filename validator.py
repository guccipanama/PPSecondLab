import re


class validator:
    def __init__(self):
        pass

    def check_telephone(telephone) -> bool:
        if type(telephone) != str:
            return False
        pattern = '\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$'
        if re.match(pattern, telephone):
            return True
        return False

    def check_height(weight: str) -> bool:
        if type(weight) != str:
            return False
        pattern = '[12]\.\d'
        if re.match(pattern, weight):
            return True
        return False

    def check_inn(inn: str) -> bool:
        if type(inn) != str:
            return False
        if len(inn) == 12:
            return True
        return False

    def check_passport(number: int) -> bool:
        if len(str(number)) == 6:
            return True
        return False

    def check_occupation(university: str) -> bool:
        if type(university) != str:
            return False
        return True

    def check_age(age: int) -> bool:
        if type(age) != int:
            return False
        if age < 14 or age > 60:
            return False
        return True

    def check_views(views: str) -> bool:
        if type(views) != str:
            return False
        return True

    def check_worldview(worldview: str) -> bool:
        if type(worldview) != str:
            return False
        return True

    def check_address(address: str) -> bool:
        if type(address) == str:
            pattern = '[а-яА-Я.\s\d-]+\s+[0-9]+$'
            if re.match(pattern, address):
                return True
        return False
