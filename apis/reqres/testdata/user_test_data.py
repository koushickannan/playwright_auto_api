from apis.reqres.models.requests.user_request import CreateUserRequest, User
from faker import Faker

data_generator = Faker()


def create_user_request_payload() -> dict:
    first_name = data_generator.first_name()
    # print("First name : ", first_name)
    last_name = data_generator.last_name()
    # print("Last name : ", last_name)
    email_id = f"{first_name}.{last_name}@rqimail.laerdalblr.in"
    # print("Email : ", email_id)

    create_user_request = CreateUserRequest(

        user=User(
            firstName=first_name,
            lastName=last_name,
            emailId=email_id,
            isTermsAccepted=True
        )
    )

    return create_user_request.dict()
