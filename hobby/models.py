from FlaskProject.extendsions import db
from common.BaseModel import BaseModelPrimaryKey


class HobbyBlog(BaseModelPrimaryKey):
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer, db.ForeignKey("user_blog.id"))


