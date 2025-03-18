# Generated by Django 5.1.7 on 2025-03-16 05:41

import Students.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0003_student_created_at_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='student.jpg', upload_to='student_pictures', validators=[Students.models.validate_image_size]),
        ),
    ]
