import os

def upload_image_path(instance, filename):
    """
    Sets the image upload path as the subdirectory
    defined by the user's uuid. Also changes filename 
    to the given image name.
    """
    ext = filename.split('.')[-1]
    n_filename = f'{instance.image_name}.' + ext
        
    return os.path.join(
        'images',
        str(instance.user.id),
        n_filename
    )
