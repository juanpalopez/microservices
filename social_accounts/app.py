from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Owner, SocialAccount, SocialNetwork, User

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
api = Api(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Orign','*')
    return response

social_account_fields = {
        # 'social_network': fields.String,
        # 'social_account': fields.String,
        'owner_id': fields.Integer,
        'owner': fields.String,
        'token': fields.String,
        'social_account_id' : fields.Integer,
        'social_account' : fields.String,
        'social_network_id' : fields.Integer,

        }

class SocialAccountList(Resource):
    @marshal_with(social_account_fields)
    def get(self):
        print(session.query(SocialAccount).all() )
        return session.query(SocialAccount).join(SocialNetwork).all()
    #   return session.query(Owner).all()

api.add_resource(SocialAccountList, '/accounts')

if __name__ == '__main__':
    # print(session.query(Owner).all())
    app.run()
