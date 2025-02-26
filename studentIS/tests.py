from django.test import TestCase
from django.utils import timezone
from .models import Student, Course, Classes, Address
from django.core.exceptions import ValidationError

class ModelTests(TestCase):
    def setUp(self):
        # Create test data
        self.class1 = Classes.objects.create(
            subject="Python Programming",
            schedule_start=timezone.now(),
            schedule_end=timezone.now() + timezone.timedelta(hours=1.5)
        )

        self.course = Course.objects.create(
            name="Computer Science",
            start_date="Fall"
        )
        self.course.classes.add(self.class1)

        self.address = Address.objects.create(
            street="123 Test St",
            city="Test City",
            state="CA",
            zip_code="12345",
            country="USA"
        )

        self.student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth=timezone.now(),
            SSN="1234",
            email="john@test.com",
            start_date="Fall 2024",
            program=self.course
        )

    def test_class_creation(self):
        """Test Classes model"""
        self.assertEqual(str(self.class1), "Python Programming")
        self.assertTrue(isinstance(self.class1, Classes))

    def test_course_creation(self):
        """Test Course model"""
        self.assertEqual(str(self.course), "Computer Science")
        self.assertTrue(isinstance(self.course, Course))
        self.assertEqual(self.course.classes.first(), self.class1)

    def test_address_creation(self):
        """Test Address model"""
        self.assertEqual(self.address.city, "Test City")
        self.assertEqual(self.address.state, "CA")
        self.assertEqual(self.address.zip_code, "12345")

    def test_student_creation(self):
        """Test Student model"""
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.email, "john@test.com")
        self.assertEqual(self.student.program, self.course)

    def test_student_email_unique(self):
        """Test that student email must be unique"""
        with self.assertRaises(Exception):
            Student.objects.create(
                first_name="Jane",
                last_name="Doe",
                date_of_birth=timezone.now(),
                SSN="5678",
                email="john@test.com",  # Same email as existing student
                start_date="Fall 2024"
            )

    def test_valid_state_choices(self):
        """Test that only valid states are accepted"""
        with self.assertRaises(ValidationError):
            address = Address.objects.create(
                street="456 Test St",
                city="Test City",
                state="XX",  # Invalid state
                zip_code="12345",
                country="USA"
            )
            address.full_clean()
