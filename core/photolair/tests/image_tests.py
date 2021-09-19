import sys, os
from io import BytesIO
from PIL import Image as Pil_Image
from django.core.files import File
from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth import get_user_model

from ..models import Image

User = get_user_model()


class ImageTestCase(TestCase):
    """
    Performs tests on the Image model such as image instance creation and
    error checking. 
    """

    def _get_image_path(self, image_name):
        """
        Gets an image from the test images folder
        """
        test_image_rel_dir_path = 'photolair/tests/test_images/'

        script_dir = sys.path[0]
        img_path = os.path.join(
            script_dir, 
            test_image_rel_dir_path,
            image_name
        )

        return img_path
    

    def _get_image_io_stream(self, image_name):
        """
        First gets absolute path of the image, load its into a form
        django can upload (i.e. byte stream)
        """
        img_path = self._get_image_path(image_name)

        image_file = Pil_Image.open(img_path)
        img_io = BytesIO()
        image_file.save(img_io, format='jpeg')

        return File(img_io, name=image_name)


    def setUp(self):
        """
        Create a single user needed for uploading images
        """
        username = 'harjiggly'
        password = 'testpass123'

        User.objects.create_user(
          username=username,
          password=password
        )
    

    def test_create_image(self):
        """
        Creates an image instance. 

        img_choice can be changed according to the full names of 
        images in the ./test_images folder.
        """
        # Open an image from the test folder
        img_choice = 'sunsets.jpeg'
        image_file = self._get_image_io_stream(img_choice)
        
        # Set image properties
        image_name = img_choice.split('.')[0]
        inventory = 10
        price = 5
        new_user = User.objects.get(username='harjiggly')
        
        new_image = Image.objects.create(
            user=new_user,
            image_name=image_name,
            image=image_file,
            inventory=inventory,
            price=price,
        )

        self.assertEqual(
            new_image.image_name,
            image_name
        )

        self.assertEqual(
            new_image.user.id,
            new_user.id
        )

        self.assertEqual(
            new_image.inventory,
            inventory
        )

        self.assertEqual(
            new_image.price,
            price
        )
    

    def test_image_no_user(self):
        """
        Try to upload an image without a user.
        """
        with self.assertRaises(IntegrityError):
            img_choice = 'sunsets.jpeg'
            image_file = self._get_image_io_stream(img_choice)
            image_name = img_choice.split('.')[0]
            inventory = 5
            price = 5

            new_image = Image.objects.create(
                image_name=image_name,
                image=image_file,
                inventory=inventory,
                price=price,
            )
  
  
    def test_image_non_integer_price(self):
        """
        Create an image instance with non-integer price
        """ 
        with self.assertRaises(ValueError):
            img_choice = 'sunsets.jpeg'
            image_file = self._get_image_io_stream(img_choice)
            image_name = img_choice.split('.')[0]
            inventory = 5
            price = 'abc'
            new_user = User.objects.get(username='harjiggly')

            new_image = Image.objects.create(
                user=new_user,
                image_name=image_name,
                image=image_file,
                inventory=inventory,
                price=price,
            )


    def test_image_non_integer_inventory(self):
        """
        Create an image instance with non-integer inventory
        """ 
        with self.assertRaises(ValueError):
            img_choice = 'sunsets.jpeg'
            image_file = self._get_image_io_stream(img_choice)
            image_name = img_choice.split('.')[0]
            inventory = 'abc'
            price = 10
            new_user = User.objects.get(username='harjiggly')

            new_image = Image.objects.create(
                user=new_user,
                image_name=image_name,
                image=image_file,
                inventory=inventory,
                price=price,
            )


    def test_image_negative_integer_price(self):
        """
        Create an image instance with non-integer price
        """ 
        with self.assertRaises(IntegrityError):
          img_choice = 'sunsets.jpeg'
          image_file = self._get_image_io_stream(img_choice)
          image_name = img_choice.split('.')[0]
          inventory = 5
          price = -10
          new_user = User.objects.get(username='harjiggly')

          new_image = Image.objects.create(
              user=new_user,
              image_name=image_name,
              image=image_file,
              inventory=inventory,
              price=price,
          )


    def test_image_negative_integer_inventory(self):
        """
        Create an image instance with non-integer inventory
        """ 
        with self.assertRaises(IntegrityError):
          img_choice = 'sunsets.jpeg'
          image_file = self._get_image_io_stream(img_choice)
          image_name = img_choice.split('.')[0]
          inventory = -5
          price = 10
          new_user = User.objects.get(username='harjiggly')

          new_image = Image.objects.create(
              user=new_user,
              image_name=image_name,
              image=image_file,
              inventory=inventory,
              price=price,
          )
       