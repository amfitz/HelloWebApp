from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.template.defaultfilters import slugify
from collection.forms import ReviewForm
from collection.models import Review


def index(request):
    reviews = Review.objects.all()
    return render(request, 'index.html', {"reviews":reviews, },)

def review_detail(request, slug):
    review = Review.objects.get(slug=slug)
    return render(request, 'reviews/review_detail.html', {"review":review,})

@login_required
def edit_review(request, slug):
    review = Review.objects.get(slug=slug)
    if review.user != request.user:
        raise Http404

    form_class = ReviewForm

    if request.method == "POST":
        form = form_class(data=request.POST, instance = review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', slug=review.slug)
    else:
            form = form_class(instance=review)
    return render(request, 'reviews/edit_review.html', {"review":review, "form":form,})

def create_review(request):
    form_class = ReviewForm
    if request.method == 'POST':
        form = form.is_valid
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.slug = sluggify(review.name)
            review.save()
            return redirect('review_detail', slug=review.slug)
    else:
        form = form_class()
    return render(request, 'reviews/create_review.html', {'form': form,})


def browse_by_name(request, initial=None):
    if initial:
        reviews = Review.objects.filter(name__istartswith=initial)
        reviews = reviews.order_by('name')
    else:
        reviews = Review.objects.all().order_by('name')
    return render(request, 'search/search.html', {'reviews':reviews, 'initial':initial,})
