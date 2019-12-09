from FlaskProject.extendsions import db
from common.BaseModel import BaseModelPrimaryKey


class UserBlog(BaseModelPrimaryKey):
    title = db.Column(db.String(32), nullable=False)
    content = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))