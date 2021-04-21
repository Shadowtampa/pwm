from django.db import models

# Create your models here.
class Game(models.Model):

    # Campos
    name = models.CharField(max_length=100, help_text='Name of the game')
    

    def __str__(self):
        """ String para representar o objeto MyModelName (no site Admin)."""
        return self.name