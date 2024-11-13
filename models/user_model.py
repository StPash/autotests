from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    age: int
    salary: int
    department: str

    def __eq__(self, other):
        if not isinstance(other, UserModel):
            return False
        return (self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.email == other.email and
                self.age == other.age and
                self.salary == other.salary and
                self.department == other.department)
