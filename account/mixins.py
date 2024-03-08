from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404 , redirect
from article.models import Article

class FieldMixin():
    def dispatch(self , request , *args , **kwargs):
        self.fields = [
                'title','slug' ,'category' ,'description'
                ,'image','is_special' ,'status'
                    ]
        if request.user.is_superuser :
            self.fields.append("auther")
        return super().dispatch(request , *args , **kwargs)

class FormValidMixin():
    def form_valid(self , form):
        if self.request.user.is_superuser:
            form.save()
        else :
            self.obj = form.save(commit=False)
            self.obj.auther = self.request.user
            if not self.obj.status == "i":
                self.obj.status == "d"
        return super().form_valid(form)


class AuthorAccessMixin():
    def dispatch(self , request, pk, *args , **kwargs):
        article = get_object_or_404(Article , pk=pk)
        if article.auther == request.user and article.status in ['b','d'] or request.user.is_superuser:
            return super().dispatch(request , *args , **kwargs)
        else :
            raise Http404("You can't see this page")
        
class AuthorsAccessMixin():
    def dispatch(self , request, *args , **kwargs):
        if request.user.is_authenticated :
            if request.user.is_superuser or request.user.is_author :
                return super().dispatch(request , *args , **kwargs)
            else :
                return redirect("account:profile")
        else :
            return redirect("account:login")
class SuperUserMixin():
    def dispatch(self , request,*args , **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request , *args , **kwargs)
        else :
            raise Http404("You can't see this page")

