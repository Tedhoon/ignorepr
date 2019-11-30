from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from .forms import BlogForms
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    blog = Blog.objects.all

    return render(request,'home.html', {'blog_all' : blog})

def detail(request,blog_id):
    details = get_object_or_404(Blog, pk = blog_id) 
                                      #primary key    

    return render(request, 'detail.html', {'details':details})

@login_required
def edit(request):
    if request.method == 'POST':
        forms = BlogForms(request.POST)

        if forms.is_valid:
            forms.save()
            return redirect('home')

    forms = BlogForms() 
    return render(request,'edit.html',{'forms': forms})
        
@login_required  
def update(request,blog_id):
    #객체를 가져올 방법 : get ob or 404
        blog_update = get_object_or_404(Blog, pk = blog_id)
        if request.method == 'POST': 
                blogform = BlogForms(request.POST,instance=blog_update) 
                if blogform.is_valid:              
                        blogform.save()     
                return redirect('home')       
        #이게 말은 수정인데 그냥 작성중인거 저장하는 거임
        blogform = BlogForms(instance=blog_update)         # 얘도 보면 new에서는 빈 form이 뜨는게 당연하지만 우리는 edit을 해주려면 

        return render(request,'edit.html',{'blogform':blogform})

@login_required
def delete(request,blog_id):
        blog_delete = get_object_or_404(Blog, pk = blog_id)
        blog_delete.delete()
        

        return redirect('home')


    


