from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    # Add any other fields you want for your projects

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()
    # Add any other fields you want for your photos

    def __str__(self):
        return self.title
    
class SocialLink(models.Model):
# In django shell add those links
# Add a GitHub link
#SocialLink.objects.create(platform='github', url='https://github.com/ddnsd')

# Add a LinkedIn link
#SocialLink.objects.create(platform='linkedin', url='https://www.linkedin.com/in/illia-maksymenko-960935252/')

# Add a Twitter link
#SocialLink.objects.create(platform='twitter', url='https://twitter.com/yourprofile/')
    GITHUB = 'github'
    LINKEDIN = 'linkedin'
    TWITTER = 'twitter'
    # Add any other platform choices you want
    PLATFORM_CHOICES = [
        (GITHUB, 'GitHub'),
        (LINKEDIN, 'LinkedIn'),
        (TWITTER, 'Twitter'),
        # Add any other platform choices you want
        # (PLATFORM_NAME, 'Platform Name')
    ]
    platform = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return f"{self.platform} - {self.url}"
    
