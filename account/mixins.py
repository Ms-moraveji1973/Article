from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404
from article.models import Article
class FieldMixin():
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_superuser:
            self.fields = [
                'title','slug' ,'category' ,'description'
                ,'image','is_special' ,'status' ,'auther'
                          ]
        elif request.user.is_author:
            self.fields = [
                'title','slug' ,'category'
                ,'description','is_special','image'
                ]
        else :
            raise Http404("You can't see this page")
        return super().dispatch(request , *args , **kwargs)

class FormValidMixin():
    def form_valid(self , form):
        if self.request.user.is_superuser:
            form.save()
        else :
            self.obj = form.save(commit=False)
            self.obj.auther = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)


class AuthorAccessMixin():
    def dispatch(self , request, pk, *args , **kwargs):
        article = get_object_or_404(Article , pk=pk)
        if article.auther == request.user and article.status in ['b','d'] or request.user.is_superuser:
            return super().dispatch(request , *args , **kwargs)
        else :
            raise Http404("You can't see this page")
        

class SuperUserMixin():
    def dispatch(self , request,*args , **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request , *args , **kwargs)
        else :
            raise Http404("You can't see this page")

