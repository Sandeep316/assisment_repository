from django.shortcuts import render
from.models import ReviewData
from .forms import ReviewForm
from django.http.response import HttpResponse

def Review_view(request):
    if request.method=="POST":
        ffrom=ReviewForm(request.POST)
        if ffrom.is_valid():
            product_id=request.POST.get('product_id','')
            review_title=request.POST.get('review_title','')
            review_ratings=request.POST.get('review_ratings','')
            review_content=request.POST.get('review_content','')
            data=ReviewData(
                product_id=product_id,
                review_title=review_title.capitalize(),
                review_ratings=review_ratings,
                review_content=review_content
            )
            data.save()
            ffrom=ReviewForm()
            review=ReviewData.objects.all()
            return render(request,"review.html",{'fform':ffrom,'review':review})
        else:
            return HttpResponse("Invalid User Data")
    else:
        review=ReviewData.objects.all()
        fform=ReviewForm()
        return render(request,"review.html",{'fform':fform,'review':review})
