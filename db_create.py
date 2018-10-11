from app import db

from models import BlogPost

# create the database and the db tables
db.create_all()


#insert
db.session.add(BlogPost("Good", "Im good."))
db.session.add(BlogPost("Well", "Im well"))
db.session.add(BlogPost("Pin install", "Otherwise, you will not be able topackages from PyPI."))


# commit the changes
db.session.commit()