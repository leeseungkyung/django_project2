from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'articles/index.html', context)

def review(request, pk):

    movie = get_object_or_404(Movie, pk=pk)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.movie = movie
        review.save()
        return redirect('articles:review_list')
    else:
        form = ReviewForm()
    context ={
        'form':form,
        'movie':movie,
    }
    return render(request, 'articles/form.html', context)



def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews':reviews
    }
    return render(request, 'articles/review_list.html', context)


def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    comments = review.comment_set.order_by('-pk')
    form = CommentForm()
    context = {
        'review':review,
        'comments':comments,
        'form':form,
    }
    return render(request, 'articles/review_detail.html', context)

@login_required
def like(request, pk):
    review = Review.objects.get(pk=pk)
    if review.like_users.filter(id=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('articles:review_list')


@login_required
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('articles:review_list')

@login_required
def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user == request.user:
        print('통과1')
        if request.method=='POST':
            print('통과2')
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                print('통과')
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('articles:review_detail', review.pk)
        else:
            print('실패')
            form = ReviewForm(instance=review)
            movie = Movie.objects.get(pk=review.movie.pk)
        context = {
            'form':form,
            'movie':movie,
        }
        return render(request, 'articles/form.html', context)
    else:
        print('실패2')
        return redirect('articles:review_detail', review.pk)

@login_required
def comments(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.user = request.user
            comments.review = review
            comments.save()
            return redirect('articles:review_detail', review.pk)
    else:
        return redirect('articles:review_detail', review.pk)

@login_required
def comments_delete(request, review_pk, comment_pk):
    review = Review.objects.get(pk=review_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.user==comment.user:
        comment.delete()
        return redirect('articles:review_detail', review.pk)

