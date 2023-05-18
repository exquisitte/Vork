from BackLogic.settings import workers, vacancies
from bson.objectid import ObjectId

def add_work(employee_email, city, company_name, description, vacancion_name, money, employment_type, needed_experience):
    vacancies.insert_one({
        "employee_email": employee_email,
        "city": city,
        "company_name": company_name,
        "vacancion_name": vacancion_name,
        "money": money,
        "employment_type": employment_type,
        "needed_experience": needed_experience,
        "description": description

    })


def vacancion_aplication(work_id, worker_mail):
    vacancies.update_one({"_id": ObjectId(work_id)}, {"$push": {"employers_suggest": worker_mail}})
