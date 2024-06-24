from pydantic import BaseModel


class User(BaseModel):
    firstName: str
    lastName: str
    emailId: str
    isTermsAccepted: bool


class CreateUserRequest(BaseModel):
    user: User
