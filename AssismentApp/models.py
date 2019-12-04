from django.db import models

class ReviewData(models.Model):
    product_id=models.CharField(max_length=100,primary_key=True)
    review_title=models.CharField(max_length=200)
    review_ratings=models.IntegerField()
    review_content=models.TextField(max_length=1000)
