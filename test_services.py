import unittest
import os
import json
from apps import create_app
from apps.db import db
from flask import jsonify

class PeliculasTestFilms(unittest.TestCase):
    """This class represents the bucketlist test case"""

    json_films= {
                    "title": "La Liga de la Justicia de Zack Snyder (2021)",
                    "length": 304720,
                    "year": 2021,
                    "director": "Zack Snyder",
                    "actors": [
                        { "name": "Henry Cavill"},
                        { "name": "Ben Affleck"},
                        { "name": "Gal Gadot"},
                        { "name": "Jason Momoa"},
                        { "name": "Ezra Miller"},
                        { "name": "Jesse Eisenberg"},
                        { "name": "Jared Leto"}
                    ]
                }

    def setUp(self):

        self.app = create_app(settings_module="config.test.Configuracion")
        self.app.testing = True
        self.client = self.app.test_client()
        # Crea un contexto de aplicación
        with self.app.app_context():
            # Crea las tablas de la base de datos
            db.create_all()
 
    def test_get_films(self):        
        res = self.client.get('/api/v1/films/')
        self.assertEqual(200, res.status_code)      

    def test_get_films_protected(self):        
        res = self.client.get('/api/v1/films/protected')
        self.assertEqual(401, res.status_code)      
        print(res.data)

    def test_add_films(self):        
        
        
        res = self.client.post('/api/v1/films/', json=self.json_films)
        self.assertEqual(201, res.status_code)   
        json_data = res.get_json()
        
   
    def test_get_film_by_id(self):    


        res = self.client.post('/api/v1/films/', json=self.json_films)
        self.assertEqual(201, res.status_code)   
        json_data = res.get_json()    
        
        
        res = self.client.get(f'/api/v1/films/{json_data["id"]}')
        self.assertEqual(200, res.status_code)   
        json_data = res.get_json()
        # print(json_data)
        
        
    # def test_fims_creacion(self):
    #     """Test API can create a bucketlist (POST request)"""
    #     res = self.client().post('/api/v1/films/', data=self.bucketlist)
    #     print(res.data)
        # self.assertEqual(res.status_code, 201)
        # self.assertIn('Resultados', str(res.data))

    # def test_api_can_get_all_bucketlists(self):
    #     """Test API can get a bucketlist (GET request)."""
    #     res = self.client().post('/bucketlists/', data=self.bucketlist)
    #     self.assertEqual(res.status_code, 201)
    #     res = self.client().get('/bucketlists/')
    #     self.assertEqual(res.status_code, 200)
    #     self.assertIn('Go to Borabora', str(res.data))

    # def test_api_can_get_bucketlist_by_id(self):
    #     """Test API can get a single bucketlist by using it's id."""
    #     rv = self.client().post('/bucketlists/', data=self.bucketlist)
    #     self.assertEqual(rv.status_code, 201)
    #     result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
    #     result = self.client().get(
    #         '/bucketlists/{}'.format(result_in_json['id']))
    #     self.assertEqual(result.status_code, 200)
    #     self.assertIn('Go to Borabora', str(result.data))

    # def test_bucketlist_can_be_edited(self):
    #     """Test API can edit an existing bucketlist. (PUT request)"""
    #     rv = self.client().post(
    #         '/bucketlists/',
    #         data={'name': 'Eat, pray and love'})
    #     self.assertEqual(rv.status_code, 201)
    #     rv = self.client().put(
    #         '/bucketlists/1',
    #         data={
    #             "name": "Dont just eat, but also pray and love :-)"
    #         })
    #     self.assertEqual(rv.status_code, 200)
    #     results = self.client().get('/bucketlists/1')
    #     self.assertIn('Dont just eat', str(results.data))

    # def test_bucketlist_deletion(self):
    #     """Test API can delete an existing bucketlist. (DELETE request)."""
    #     rv = self.client().post(
    #         '/bucketlists/',
    #         data={'name': 'Eat, pray and love'})
    #     self.assertEqual(rv.status_code, 201)
    #     res = self.client().delete('/bucketlists/1')
    #     self.assertEqual(res.status_code, 200)
    #     # Test to see if it exists, should return a 404
    #     result = self.client().get('/bucketlists/1')
    #     self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables."""
        pass
        # with self.app.app_context():
        #     # drop all tables
        #     db.session.remove()
        #     db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()