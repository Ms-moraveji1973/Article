from django.http import Http404

class FieldMixin():
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_superuser:
            self.fields = [
                'title','slug' ,'category' ,'description'
                ,'image' ,'status' ,'auther'
                          ]
        elif request.user.is_author:
            self.fields = [
                'title','slug' ,'category'
                ,'description' ,'image'
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
            self.obj.status = False
        return super().form_valid(form)


