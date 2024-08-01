from django.db import models
from django.contrib.auth.models import AbstractUser, User, Permission
from phone_field import PhoneField

SEX_CHOICES = [
    ('Male','Male'),
    ('Female','Female'),
    ('Non-Binary','Non-Binary'),
    ('Other','Other')
]

STATES = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming'
}

# Create your models here.
class Classes(models.Model):
    subject = models.CharField(max_length=30, blank=True, null=True)
    schedule_start = models.DateTimeField()
    schedule_end = models.DateTimeField()
    class_duration = models.CharField(max_length=25, default="90 minutes")

class Course(models.Model):
    classes = models.ManyToManyField(Classes)

class Address(models.Model):
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2, choices=STATES)
    zip_code = models.CharField(max_length=5)
    country = models.CharField(max_length=20)

class Student(models.Model):
    first_name = models.CharField(max_length=15, blank=False, null=False, default='John')
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=False, null=False, default='Doe')
    sex = models.CharField(max_length=15, choices=SEX_CHOICES, blank=True, null=True)
    date_of_birth = models.DateTimeField(max_length=8)
    SSN = models.CharField(max_length=4)
    address = models.OneToOneField(Address, blank=True, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=25, unique=True)
    phone_number = PhoneField(blank=True)
    program = models.OneToOneField(Course, blank=True, null=True, on_delete=models.CASCADE, related_name='course')
    start_date = models.DateTimeField(max_length=8)
    reference = models.CharField(max_length=20, blank=True, null=True)


class User(AbstractUser):

    def student(self):
        if self.is_student:
            student_classes = models.ManyToManyField(Course, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=False, default='None')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_picture = models.ImageField(null=True, blank=True, upload_to = 'media/', default='default_profile_picture.jpg')

# class Teacher(User):
#     sex = models.CharField(max_length=20, blank=False, null=False)
    