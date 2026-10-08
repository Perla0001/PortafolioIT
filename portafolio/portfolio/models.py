from django.db import models

class Technology(models.Model):
    CATEGORY_CHOICES = [
        ("language", "Lenguaje"),
        ("library", "Librería"),
        ("tool", "Herramienta"),
        ("other", "Otro"),
    ]

    name = models.CharField(max_length=80, unique=True)
    icon = models.ImageField(upload_to="technologies/")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="other")

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "technologies"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    technologies = models.ManyToManyField(Technology, related_name="projects", blank=True)
    repo_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    is_visible = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return self.title


class Certificate(models.Model):
    name = models.CharField(max_length=150)
    issuer = models.CharField(max_length=100)
    image = models.ImageField(upload_to="certificates/")
    issued_date = models.DateField()
    credential_url = models.URLField(blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-issued_date"]

    def __str__(self):
        return f"{self.name} ({self.issuer})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.created_at:%Y-%m-%d}"


class Greeting(models.Model):
    text = models.CharField(max_length=50)
    language = models.CharField(max_length=40, unique=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return f"{self.text} ({self.language})"
