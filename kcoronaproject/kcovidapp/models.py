from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

#admin 페이지에서 blog 클래스에서 title을 보여줍니다
    def __str__(self):
        return self.title
#summary함수를 만들어 body를 처음부터 10글자만 보여줍니다.
    def summary(self):
        return self.body[:10]