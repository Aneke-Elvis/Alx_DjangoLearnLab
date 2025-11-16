# django-models/LibraryProject/relationship_app/forms.py

from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    """
    A custom user creation form based on Django's built-in form.
    This can be extended later but is simple enough for this task.
    """
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields