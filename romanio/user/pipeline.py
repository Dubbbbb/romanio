from .models import CustomUser

def save_profile(backend, user, response, *args, **kwargs):

    CustomUser.objects.create(
        phone_number=response['phone_number']
    )