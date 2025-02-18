from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,DetailView,DeleteView
from .models import Article
from django.urls import reverse_lazy
class Index(ListView):
    model= Article
    queryset= Article.objects.all().order_by('-date')
    template_name = 'blog/index.html'
    paginate_by = 2

class DetailArticleView(DetailView):
    model= Article
    template_name = 'blog/blog_post.html'

    def get_context_data(self, **kwargs):
        context= super(DetailView,self).get_context_data(**kwargs)
        context['liked_by_user']=False
        article= Article.objects.get(id= self.kwargs.get('pk'))
        if article.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user']=True
        return context

class LikeArticle(View):
    def post(self,request,pk):
        article= Article.objects.get(id=pk)
        if article.likes.filter(pk=self.request.user.id).exists():
            article.likes.remove(request.user.id)
        else:
            article.likes.add(request.user.id)
        article.save()
        return redirect('detail_article',pk=pk)

class Featured(ListView):
    model = Article
    queryset = Article.objects.filter(featured= True).order_by('-date')
    template_name = 'blog/featured.html'
    paginate_by = 1

class DeleteArticle(DeleteView):
    model = Article
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Article.objects.filter(id=self.kwargs['pk'], author=self.request.user)

def Search(request):
    query= request.GET.get('q',' ').strip()
    if query:
        result= Article.objects.filter(title__icontains=query)
        return render(request,'blog/search_results.html', {'results': result, 'query': query})
    else:
        result = []
    return render(request, 'blog/search_results.html', {'results': result, 'query': query})
class About(View):
    def get(self,request):
        return render(request,'blog/about.html')