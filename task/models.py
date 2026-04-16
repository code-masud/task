from django.db import models

MEDIA_TYPE = (
    ('text', 'Text'),
    ('image', 'Image'),
    ('audio', 'Audio'),
    ('video', 'Video'),
    ('youtube', 'YouTube'),
)


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ContentBlock(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='blocks'
    )

    title = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=20, choices=MEDIA_TYPE)

    text = models.TextField(blank=True)
    file = models.FileField(upload_to='media/', blank=True)
    youtube_id = models.CharField(max_length=50, blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.article.title} - {self.type}"

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.type == 'text' and not self.text:
            raise ValidationError("Text content required")

        if self.type in ['image', 'audio', 'video'] and not self.file:
            raise ValidationError("File is required")

        if self.type == 'youtube' and not self.youtube_id:
            raise ValidationError("YouTube ID required")


class Term(models.Model):
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word


class TermContent(models.Model):
    term = models.ForeignKey(
        Term,
        on_delete=models.CASCADE,
        related_name='contents'
    )

    title = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=20, choices=MEDIA_TYPE)

    text = models.TextField(blank=True)
    file = models.FileField(upload_to='terms/', blank=True)
    youtube_id = models.CharField(max_length=50, blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.term.word} - {self.type}"

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.type == 'text' and not self.text:
            raise ValidationError("Text required")

        if self.type in ['image', 'audio', 'video'] and not self.file:
            raise ValidationError("File required")

        if self.type == 'youtube' and not self.youtube_id:
            raise ValidationError("YouTube ID required")
