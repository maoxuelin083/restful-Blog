from FlaskProject.extendsions import db
from common.BaseModel import BaseModelPrimaryKey


class UserComment(BaseModelPrimaryKey):
    conten = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))




