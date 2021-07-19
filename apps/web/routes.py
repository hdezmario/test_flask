from apps.common.error_handler import ObjectNotFound
from flask import request
from flask_restful import  Resource

from apps.web.schemas import FilmSchema
from apps.web.models import Film, Actor


film_schema = FilmSchema()

from flask_jwt_extended import jwt_required


class FilmListResource(Resource):

    # @jwt_required()
    def get(self):
        films = Film.get_all()
        result = film_schema.dump(films, many=True)
        return result
    def post(self):
        data = request.get_json()
        film_dict = film_schema.load(data)
        film = Film(title=film_dict['title'],
                    length=film_dict['length'],
                    year=film_dict['year'],
                    director=film_dict['director']
        )
        for actor in film_dict['actors']:
            film.actors.append(Actor(actor['name']))
        film.save()
        resp = film_schema.dump(film)
        return resp, 201


class FilmResource(Resource):
    def get(self, film_id):
        film = Film.get_by_id(film_id)
        if film is None:
            raise ObjectNotFound('La película no existe')
        resp = film_schema.dump(film)
        return resp



class FilmListProtectedResource(Resource):

    @jwt_required()
    def get(self):
        films = Film.get_all()
        result = film_schema.dump(films, many=True)
        return result
    

# class LoginApi(Resource):
#     def post(self):
#         data = request.get_json()
#         print(data)
#         return {'none':'none'}

