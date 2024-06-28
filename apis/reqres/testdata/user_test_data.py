from apis.reqres.models.requests.user_request import CreateUserRequest, User
from faker import Faker
import random
data_generator = Faker()


def create_user_request_payload() -> dict:
    random_num = random.randint(100,9999999)
    first_name = data_generator.first_name()
    last_name = data_generator.last_name()
    email_id = f"{first_name}{last_name}_{random_num}@rqimail.laerdalblr.in"

    create_user_request = CreateUserRequest(

        user=User(
            firstName=first_name,
            lastName=last_name,
            emailId=email_id,
            isTermsAccepted=True
        )
    )

    return create_user_request.dict()
