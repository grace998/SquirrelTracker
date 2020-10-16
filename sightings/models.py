from django.db import models

# Create your models here.

class Squirrels(models.Model):
    Longitude  = models.FloatField(
            help_text = _('Longitude'),)

    Latitude = models.FloatField(
            help_text = _('Latitude'),)

    Unique_Squirrel_Id = models.CharField(
            help_text = _('Unique ID of the squirrell'),
            primary_key = True,
            unique = True,
            max_length = 50,
            )

    AM = 'AM'
    PM = 'PM'
    Shift_choice = (
            (AM,'AM'),
            (PM,'PM'),
            )

    Shift = models.CharField(
            help_text = _('Shift'),
            max_length = 16,
            choices = Shift_choice,
            )

    Date = models.DateField(
            help_text = _('Date'),
            null = True,
            blank = True,
            )

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Unknown = '?'
    Age_choice=(
            (Adult,'Adult'),
            (Juvenile, 'Juvenile'),
            )

    Age = models.CharField(
            help_text = _('Age'),
            max_length = 50,
            choices = AGE_CHOICE,
            null = True,
            blank = True,
            )

    Black = 'Black'
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Color_choice = (
            (Black, 'Black'),
            (Gray, 'Gray'),
            (Cinnamon, 'Cinnamon'),
            )

    Primary_Fur_Color = models.CharField(
            help_text = _('Primary Fur color'),
            max_length=16,
            choices = Color_choice,
            null = True,
            blank = True,
            )

    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    Location_choice = (
            (Ground_Plane, 'Ground Plane'),
            (Above_Ground, 'Above Ground'),
            )
    
    Location =  models.CharField(
            help_text = _('Location'),
            max_length = 250,
            choices = Location_choice,
            null = True,
            blank = True,
            )

    Specific_Location = models.CharField(
            help_text = _('Specific location'),
            max_length = 250,
            null = True,
            blank = True,
            )

    Running = models.NullBooleanField(
            help_text = _('Running'),
            null = True,
            blank = True,
    )
    
    Chasing = models.NullBooleanField(
            help_text = _('Chasing'),
            null = True,
            blank = True,
    ) 

    Climbing = models.NullBooleanField(
            help_text = _('Climbing'),
            null = True,
            blank=True,
    )

    Eating = models.NullBooleanField(
            help_text = _('Eating'),
            null = True,
            blank=True,
    )

    Foraging = models.NullBooleanField(
            help_text = _('Foraging'),
            null = True,
            blank=True,
    )

    Other_Activities = models.CharField(
        help_text = _('Other Activities'),
        max_length = 128,
        null = True,
        blank = True,
    )

    Kuks = models.NullBooleanField(
            help_text = _('Kuks'),
            null = True,
            blank = True,
    )

    Quaas = models.NullBooleanField(
            help_text = _('Quaas'),
            null = True,
            blank = True,
    )

    Moans = models.NullBooleanField(
            help_text = _('Moans'),
            null = True,
            blank = True,
    )

    Tail_Flags = models.NullBooleanField(
            help_text = _('Tail_Flags'),
            null = True,
            blank=True,
    )

    Tail_Twitches = models.NullBooleanField(
            help_text = _('Tail_Twitches'),
            null = True,
            blank=True,
    )

    Approaches = models.NullBooleanField(
            help_text = _('Approaches'),
            null = True,
            blank=True,
    )

    Indifferent = models.NullBooleanField(
            help_text = _('Indifferent'),
            null = True,
            blank=True,
    )
    
    Runs_From = models.NullBooleanField(
            help_text = _('Runs_From'),
            null = True,
            blank=True,
    )