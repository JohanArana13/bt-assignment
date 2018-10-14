# from sqlalchemy import Column, String
# from .entity import Entity, Base

# class Url(Entity, Base):
#     __tablename__ = 'shortener'
    
#     long_url = Column(String)
#     short_url = Column(String)

#     def __init__(self, long_url, short_url, created_by):
#         Entity.__init__(self, created_by)
#         self.long_url = long_url
#         self.short_url = short_url