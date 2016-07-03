from django.shortcuts import render, redirect
from collection.forms import ReviewForm
from collection.models import Review


def index(request):
    reviews = Review.objects.all()
    return render(request, 'index.html', {"reviews":reviews, },)

def review_detail(request, slug):
    review = Review.objects.get(slug=slug)
    return render(request, 'reviews/review_detail.html', {"review":review,})

def edit_review(request, slug):
    review = Review.objects.get(slug=slug)
    form_class = ReviewForm

    if request.method == "POST":
        form = form_class(data=request.POST, instance = review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', slug=review.slug)
    else:
            form = form_class(instance=review)
    return render(request, 'reviews/edit_review.html', {"review":review, "form":form,})
