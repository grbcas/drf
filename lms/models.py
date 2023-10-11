from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):

    name = models.CharField(max_length=150, unique=True)
    img_preview = models.ImageField(verbose_name='avatar', **NULLABLE)
    description = models.TextField(verbose_name='description', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):

    name = models.CharField(max_length=150, **NULLABLE)
    img_preview = models.ImageField(verbose_name='avatar', **NULLABLE)
    description = models.TextField(verbose_name='description', **NULLABLE)
    link_video = models.URLField(verbose_name='link_video', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='lessons',
                               verbose_name='Course', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Payment(models.Model):

    # PAYMENT_METHOD = {0: 'cash', 1: 'non-cash'}
    PAYMENT_METHOD = [(0, 'cash'), (1, 'non-cash')]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Payment Date')
    status = models.BooleanField(default=True, verbose_name='Payment status')
    payment_amount = models.FloatField(verbose_name='Payment amount')
    # payment_method = models.PositiveSmallIntegerField(default=PAYMENT_METHOD[0], verbose_name='payment method')
    payment_method = models.PositiveSmallIntegerField(max_length=2,
                                                      choices=PAYMENT_METHOD,
                                                      default='cash',
                                                      verbose_name='payment method')

    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name='payments',
                               verbose_name='Course',
                               **NULLABLE)

    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               related_name='payments',
                               verbose_name='Lesson',
                               **NULLABLE)

    def __str__(self):
        return f'{self.payment_amount, self.course, self.lesson}'

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
