# #!/usr/bin/python3
# """test for console"""
# import unittest
# from unittest.mock import patch
# from io import StringIO
# import pep8
# import os
# import json
# import console
# import models
# import tests
# from console import HBNBCommand
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
# from models.engine.file_storage import FileStorage
#
#
# class TestConsole(unittest.TestCase):
#     """this will test the console"""
#
#     console = None
#
#     @classmethod
#     def setUpClass(cls):
#         """setup for the test"""
#         cls.console = HBNBCommand()
#
#     @classmethod
#     def teardown(cls):
#         """at the end of the test this will tear it down"""
#         del cls.console
#
#     def tearDown(self):
#         """Remove temporary file (file.json) created as a result"""
#         try:
#             os.remove("file.json")
#         except Exception:
#             pass
#
#     def test_pep8_console(self):
#         """Pep8 console.py"""
#         style = pep8.StyleGuide(quiet=True)
#         p = style.check_files(["console.py"])
#         self.assertEqual(p.total_errors, 0, 'fix Pep8')
#
#     def test_docstrings_in_console(self):
#         """checking for docstrings"""
#         self.assertIsNotNone(console.__doc__)
#         self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
#         self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
#         self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
#         self.assertIsNotNone(HBNBCommand.do_create.__doc__)
#         self.assertIsNotNone(HBNBCommand.do_show.__doc__)
#         self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
#         self.assertIsNotNone(HBNBCommand.do_all.__doc__)
#         self.assertIsNotNone(HBNBCommand.do_update.__doc__)
#         self.assertIsNotNone(HBNBCommand.count.__doc__)
#         self.assertIsNotNone(HBNBCommand.strip_clean.__doc__)
#         self.assertIsNotNone(HBNBCommand.default.__doc__)
#
#     def test_emptyline(self):
#         """Test empty line input"""
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("\n")
#             self.assertEqual('', f.getvalue())
#
#     def test_quit(self):
#         """test quit command inpout"""
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("quit")
#             self.assertEqual('', f.getvalue())
#
#     def test_create(self):
#         """Test create command inpout"""
#         pass
#
#     def test_show(self):
#         """Test show command inpout"""
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("show")
#             self.assertEqual(
#                 "** class name missing **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("show sasdfsdrf")
#             self.assertEqual(
#                 "** class doesn't exist **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("show BaseModel")
#             self.assertEqual(
#                 "** instance id missing **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("show BaseModel abcd-123")
#             self.assertEqual(
#                 "** no instance found **\n", f.getvalue())
#
#     def test_destroy(self):
#         """Test destroy command inpout"""
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("destroy")
#             self.assertEqual(
#                 "** class name missing **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("destroy Galaxy")
#             self.assertEqual(
#                 "** class doesn't exist **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("destroy User")
#             self.assertEqual(
#                 "** instance id missing **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("destroy BaseModel 12345")
#             self.assertEqual(
#                 "** no instance found **\n", f.getvalue())
#
#     def test_all(self):
#         """Test all command inpout"""
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("all asdfsdfsd")
#             self.assertEqual("** class doesn't exist **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("all State")
#             self.assertEqual("[]\n", f.getvalue())
#
#     def test_update(self):
#         """Test update command inpout"""
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("update")
#             self.assertEqual(
#                 "** class name missing **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("update sldkfjsl")
#             self.assertEqual(
#                 "** class doesn't exist **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("update User")
#             self.assertEqual(
#                 "** instance id missing **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("update User 12345")
#             self.assertEqual(
#                 "** no instance found **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("all User")
#             obj = f.getvalue()
#         my_id = obj[obj.find('(')+1:obj.find(')')]
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("update User " + my_id)
#             self.assertEqual(
#                 "** attribute name missing **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("update User " + my_id + " Name")
#             self.assertEqual(
#                 "** value missing **\n", f.getvalue())
#
#     def test_z_all(self):
#         """Test alternate all command inpout"""
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("asdfsdfsd.all()")
#             self.assertEqual(
#                 "** class doesn't exist **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("State.all()")
#             self.assertEqual("[]\n", f.getvalue())
#
#     def test_z_count(self):
#         """Test count command inpout"""
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("asdfsdfsd.count()")
#             self.assertEqual(
#                 "** class doesn't exist **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("State.count()")
#             self.assertEqual("0\n", f.getvalue())
#
#     def test_z_show(self):
#         """Test alternate show command inpout"""
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("safdsa.show()")
#             self.assertEqual(
#                 "** class doesn't exist **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("BaseModel.show(abcd-123)")
#             self.assertEqual(
#                 "** no instance found **\n", f.getvalue())
#
#     def test_help_destroy(self):
#         """Test alternate destroy command inpout"""
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("Galaxy.destroy()")
#             self.assertEqual(
#                 "** class doesn't exist **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("User.destroy(12345)")
#             self.assertEqual(
#                 "** no instance found **\n", f.getvalue())
#
#     def test_help_update(self):
#         """Test alternate destroy command inpout"""
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("sldkfjsl.update()")
#             self.assertEqual(
#                 "** class doesn't exist **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("User.update(12345)")
#             self.assertEqual(
#                 "** no instance found **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("all User")
#             obj = f.getvalue()
#         my_id = obj[obj.find('(')+1:obj.find(')')]
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("User.update(" + my_id + ")")
#             # self.assertEqual(
#             #    "** attribute name missing **\n", f.getvalue())
#         with patch('sys.stdout', new=StringIO()) as f:
#             self.console.onecmd("User.update(" + my_id + ", name)")
#             # self.assertEqual(
#             #    "** value missing **\n", f.getvalue())
#
#
# if __name__ == "__main__":
#     unittest.main()


# !/usr/bin/python3
"""Test"""
import unittest
from unittest.mock import patch
from io import StringIO
import models
from console import HBNBCommand


class test_console(unittest.TestCase):
    ''' Test the console module'''

    def setUp(self):
        '''setup for'''
        self.store = models.storage
        self.buffer = StringIO()
        self.console = HBNBCommand()

    def tearDown(self):
        ''''''
        del self.buffer
        del self.store

    def test_all(self):
        """test all"""
        with patch('sys.stdout', self.buffer):
            self.console.onecmd('all Ade')
            self.assertEqual("** class doesn't exist **\n",
                             self.buffer.getvalue())
        # with patch('sys.stdout', self.buffer):
        #     self.console.onecmd("all State")
        #     self.assertEqual("[]\n", self.buffer.getvalue())

    def test_create(self):
        """test create"""
        with patch('sys.stdout', self.buffer):
            self.console.onecmd('create State name="Abia"')
            id = self.buffer.getvalue()
            self.assertFalse(len(id) == 43)

    def test_create_many(self):
        """test create"""
        with patch('sys.stdout', self.buffer):
            self.console.onecmd('create State name="California"')
            state_id = self.buffer.getvalue()[:-1]
        with patch('sys.stdout', self.buffer):
            self.console.onecmd(
                'create City state_id={} name="San_Francisco"'.format(
                    state_id))
            city_id = self.buffer.getvalue()[:-1]
        with patch('sys.stdout', self.buffer):
            self.console.onecmd(
                'create User email="my@me.com" password="pwd"'
                'first_name="FN" last_name="LN"')
            user_id = self.buffer.getvalue()[:-1]
            # self.console.onecmd( 'create Place city_id={}
            # user_id={} name="My_house"
            # description="no_description_yet" number_rooms=4
            # number_bathrooms=1 max_guest=3 price_by_night=100
            # latitude=120.12 longitude=101.4'.format(city_id, user_id))
            self.assertTrue(len(state_id) == 36)
