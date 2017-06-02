from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Owner(Base):
    __tablename__ = "owner"

    owner_id = Column(Integer, primary_key = True)
    owner = Column(String(80), unique=True)
    token = Column(String(200), unique=True)

    def __repr__(self):
        return "<Owner(owner_id= '%s', owner='%s', token='%s')>" % (self.owner_id, self.owner, self.token)

class SocialNetwork(Base):
    __tablename__ = "socialnetwork"

    social_network_id = Column(Integer, primary_key = True)
    social_network = Column(String(80), unique=True)

    def __repr__(self):
        return "<SocialNetwork(social_network_id= '%s', social_network='%s')>" % (self.social_network_id, self.social_network)

class SocialAccount(Base):
    __tablename__ = "socialaccount"

    social_account_id = Column(Integer, primary_key = True)
    social_account = Column(String(80), unique=True)
    owner_id = Column(Integer, ForeignKey("Owner.owner_id"), nullable=False)
    social_network_id = Column(Integer, ForeignKey("SocialNetwork.social_network_id"), nullable = False)


    def __repr__(self):
        return "<SocialAccount(social_account_id= '%s', social_account='%s', owner_id='%s', social_network_id='%s'>" % (self.social_account_id, self.social_account, self.owner_id, self.social_network_id)


class User(Base):
    __tablename__= 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User(id = '%s', username='%s', email='%s')>" % (self.id, self.username, self.email)
