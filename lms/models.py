from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):

    name = models.CharField(max_length=150, unique=True)
    img_preview = models.ImageField(verbose_name='Avatar', **NULLABLE)
    description = models.TextField(verbose_name='Description', **NULLABLE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='courses',
                             verbose_name='User',
                             **NULLABLE)

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
                               verbose_name='Course',
                               **NULLABLE)

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='lessons',
                             verbose_name='User',
                             **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Payment(models.Model):

    PAYMENT_METHOD = [(0, 'cash'), (1, 'non-cash')]

    date = models.DateTimeField(auto_now_add=True, verbose_name='Payment Date')
    status = models.BooleanField(default=False, verbose_name='Payment status')
    amount = models.FloatField(verbose_name='Payment amount')
    stripe_id = models.CharField(verbose_name='Stripe id', **NULLABLE)
    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT_METHOD,
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

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='payments',
                             verbose_name='User')

    last_update = models.DateTimeField(auto_now=True, verbose_name='Last update')

    def __str__(self):
        return f'{self.amount, self.course, self.lesson, self.status, self.stripe_id}'

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'


class Subscription(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='User',
                             related_name='subscriptions',
                             **NULLABLE)

    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               verbose_name='Course',
                               related_name='subscriptions',
                               **NULLABLE)

    def __str__(self):
        return f'{self.pk} {self.user}:{self.course}'

    class Meta:
        unique_together = ('course', 'user')
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

# заменить на many2many field -если нет дополнительных полей