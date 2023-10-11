from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course:

    name = models.CharField(max_length=150, unique=True)
    img_preview = models.ImageField(verbose_name='avatar', **NULLABLE)
    description = models.TextField(verbose_name='description', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson:

    name = models.CharField(max_length=150, **NULLABLE)
    img_preview = models.ImageField(verbose_name='avatar', **NULLABLE)
    description = models.TextField(verbose_name='description', **NULLABLE)
    link_video = models.URLField(verbose_name='link_video', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
