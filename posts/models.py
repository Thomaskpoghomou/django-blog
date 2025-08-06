from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.db import models
from django.urls import reverse

User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=200,unique=True, verbose_name='Titre')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name='Publié')
    content = models.TextField(blank=True, verbose_name='Contenu')
    thumbnail = models.ImageField(upload_to='blog/', null=True, blank=True, )


    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Article'

    # Cette methode nous permet de retourner tout simplement le titre le l'article de notre blog
    def __str__(self):
        return self.title
    
    # La fonction slugify permet de transformer le titre en slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # Cette methode nous permet de retourne une article si l'auteur n'est pas défini.
    @property
    def author_or_default(self):
        if self.author:
            return self.author.username
        return "L'auteur inconnu"
    
    # Cette fonction nous permet de recuperer une url à partir de son nom
    def get_absolute_url(self):
        return reverse('posts:home')
    