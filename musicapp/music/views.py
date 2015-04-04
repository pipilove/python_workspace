import datetime

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from scipy.io import mmread
from scipy.sparse import csr_matrix
from algorithm.Similar_recommend import get_item_item_sparse_dict, user_based_rec_sparse, get_final_rec_item_list
from algorithm.Models import UserClass
from algorithm.Similar_recommend import get_new_user_item_dict
from algorithm.Similar_recommend import item_based_rec
from music.models import Item1,Login,Hotmusic,User,Recmusic
from forms import SignupForm,LoginForm
from django.core.exceptions import ObjectDoesNotExist

global times1,times2, click_flag, item_item_sparse_dict, user_item_sparse_mat
times1 = 0
times2 = 0
click_flag = False
item_item_sparse_dict = dict()
# user_item_sparse_mat

def home(request, num='1'):
    curr_page = num
    all_page = 100
    int_currpage = int(curr_page)
    start_pos = (int_currpage-1)*5
    end_pos = start_pos + 5
    music_list = Hotmusic.objects.all()[start_pos:end_pos]
    # music_list = Item1.objects.all()[start_pos:end_pos]
    if int_currpage == 1:
        has_previous = False
    else:
        has_previous = True
    if int_currpage == all_page :
        has_next = False
    else:
        has_next = True
    previous_page = int_currpage - 1
    next_page = int_currpage + 1
    # music_list = Item1.objects.all().order_by('item_id')
    username = request.session.get('username', False)
    sf = SignupForm()
    lf = LoginForm()
    Context = {'music_list':music_list,'sf':sf,'lf':lf,'username':username,
               'cur_page':curr_page,'has_previous':has_previous,'has_next':has_next,
               'previous_page':previous_page,'next_page':next_page,
               }
    return render(request, 'home.html', Context)

def explore(request):
    username = request.session.get('username', False)
    sf = SignupForm()
    lf = LoginForm()
    Context = {'username':username, 'sf':sf, 'lf':lf}
    return render(request, 'explore.html',Context)

def guess(request):
    username = request.session.get('username', False)
    sf = SignupForm()
    lf = LoginForm()
    if username:
        user_id = Login.objects.get(user_name = username).user_id
        musics = Recmusic.objects.filter(user_id = user_id)
        Context = {'username':username, 'musics':musics,'sf':sf,'lf':lf}
        return render(request, 'guess.html',Context)
    else:
        return render(request, 'guess.html', {'username':username,'sf':sf,'lf':lf})

def search(request, num='1'):
    text = ''
    error = False
    if 'q' in request.GET :
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            username = request.session.get('username', False)
            musics = Item1.objects.filter(item_name__icontains=q)
            curr_page = num
            count = musics.count()
            if count%20 == 0:
                all_page = count / 20
            else:
                all_page = count /20 + 1
            int_currpage = int(curr_page)
            start_pos = (int_currpage-1)*20
            end_pos = start_pos + 20
            music_list = musics[start_pos:end_pos]
            if int_currpage == 1:
                has_previous = False
            else:
                has_previous = True
            if int_currpage == all_page :
                has_next = False
            else:
                has_next = True
            previous_page = int_currpage - 1
            next_page = int_currpage + 1
            sf = SignupForm()
            lf = LoginForm()
            text = q
            Context = {'musics':music_list,'query':q,'all_page':all_page,'count':count,
                       'cur_page':curr_page,'has_previous':has_previous,'has_next':has_next,'sf':sf,'lf':lf,
                        'previous_page':previous_page,'next_page':next_page,'username':username
                       }
            return render(request,'search_results.html',Context)
    elif int(num)>1:
        username = request.session.get('username', False)
        musics = Item1.objects.filter(item_name__icontains=text)
        curr_page = num
        count = musics.count()
        if count%20 == 0:
            all_page = count / 20
        else:
            all_page = count /20 + 1
        int_currpage = int(curr_page)
        start_pos = (int_currpage-1)*20
        end_pos = start_pos + 20
        music_list = musics[start_pos:end_pos]
        if int_currpage == 1:
            has_previous = False
        else:
            has_previous = True
        if int_currpage == all_page :
            has_next = False
        else:
            has_next = True
        previous_page = int_currpage - 1
        next_page = int_currpage + 1
        sf = SignupForm()
        lf = LoginForm()
        Context = {'musics':music_list,'query':text,'all_page':all_page,'count':count,
                   'cur_page':curr_page,'has_previous':has_previous,'has_next':has_next,'sf':sf,'lf':lf,
                    'previous_page':previous_page,'next_page':next_page,'username':username
                   }
        return render(request,'search_results.html',Context)
    return HttpResponse("Please submit a search term 20 characters or shorter.")

def signup(request):
    all_page = 100
    curr_page = 1
    has_previous = False
    has_next = True
    previous_page = 0
    next_page = 2
    music_list = Hotmusic.objects.all()[0:5]
    # sf = SignupForm()
    # music_list = Item1.objects.all().order_by('item_id')
    lf = LoginForm()
    if request.method == "POST":
        sf = SignupForm(request.POST)
        if sf.is_valid():
            username = sf.cleaned_data['username']
            email = sf.cleaned_data['email']
            passwd = sf.cleaned_data['passwd']
            user = Login()
            user.user_name = username
            user.passwd = passwd
            user.email = email
            id = Login.objects.order_by('user_id').reverse()[0].user_id
            user.user_id = id + 1
            user.save()
            request.session['username'] = username
            state = True
            # Context = {'music_list':music_list,'sf':sf,'lf':lf,'state':True,'username':username}
            Context = {'music_list':music_list,'sf':sf,'lf':lf,'username':username,
               'cur_page':curr_page,'has_previous':has_previous,'has_next':has_next,
               'previous_page':previous_page,'next_page':next_page,
               }
            return render(request,'home.html',Context)
    else:
        # state = False
        sf = SignupForm()
        # Context = {'music_list':music_list,'sf':sf,'lf':lf,'state':state}
    return render(request,'home.html',{'music_list':music_list,'sf':sf,'lf':lf,'state':False})

def login(request):
    all_page = 100
    curr_page = 1
    has_previous = False
    has_next = True
    previous_page = 0
    next_page = 2
    music_list = Hotmusic.objects.all()[0:5]
    sf = SignupForm()
    if request.method == "POST":
        lf = LoginForm(request.POST)
        if lf.is_valid():
            username = lf.cleaned_data['username']
            passwd = lf.cleaned_data['passwd']
            user = Login.objects.filter(user_name__exact = username,passwd__exact=passwd)
            if user:
                request.session['username'] = username
                Context = {'music_list':music_list,'sf':sf,'lf':lf,'username':username,
               'cur_page':curr_page,'has_previous':has_previous,'has_next':has_next,
               'previous_page':previous_page,'next_page':next_page,
               }
                return render(request,'home.html',Context)
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/music')
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def main(user_id, items_dict):
    s = datetime.datetime.now()
    user_item_sparse_mat_filename = r'.\data\user_item_sparse_mat3.mtx'
    item_item_csr_mat_filename = r'.\data\item_item_csr_mat3.mtx'

    global click_flag, item_item_sparse_dict, user_item_sparse_mat
    if not click_flag:
        user_item_sparse_mat = mmread(user_item_sparse_mat_filename)
        user_item_sparse_mat = csr_matrix(user_item_sparse_mat)
        print("user_item_sparse_mat read done!", datetime.datetime.now() - s)

        item_item_sparse_dict = get_item_item_sparse_dict(item_item_csr_mat_filename)
        print("item_item_sparse_dict read done!", datetime.datetime.now() - s)
    click_flag = True

    new_user = UserClass(user_id=user_id, items_dict=items_dict)
    new_user_item_dict = get_new_user_item_dict(new_user)

    rec_item_dict = user_based_rec_sparse(new_user, user_item_sparse_mat)
    print("rec_item_dict done!", datetime.datetime.now() - s)

    final_rec_list = get_final_rec_item_list(new_user_item_dict, rec_item_dict, item_item_sparse_dict)
    # final_item_based_rec_list = item_based_rec(new_user_item_dict, item_item_sparse_dict)
    print(datetime.datetime.now() - s)

    Recmusic.objects.filter(user_id=user_id).delete()
    for id in final_rec_list:
    # for id in final_item_based_rec_list:
        rec = Recmusic()
        rec.user_id = user_id
        rec.item_id=id
        item = Item1.objects.get(item_id=id)
        rec.item_name = item.item_name
        rec.art_name = item.art_name
        rec.save()
    print(datetime.datetime.now() - s)

def play(request, id):
    global times1,times2
    times1 = 0
    times2 = 0
    item_id = int(id)
    item_name = Item1.objects.get(item_id = item_id) .item_name
    username = request.session.get('username', False)
    if username:
        user_id = Login.objects.get(user_name = username).user_id
        try:
            u = User.objects.get(item_id=item_id,user_id=user_id)
            if u.preference == -4:
                u.count += 1
            else:
                u.count += 1
                if u.count>1 and u.count<4 :
                    u.preference = 2
                elif u.count<8:
                    u.preference = 3
                else:
                    u.preference = 4
                u.save()
        except ObjectDoesNotExist:
            user = User()
            user.user_id = Login.objects.get(user_name = username).user_id
            user.item_id = item_id
            # user.timestamp = datetime.datetime.now()
            user.preference = 1
            user.count = 1
            user.save()

        q = User.objects.filter(user_id=user_id)
        items_dict = dict()
        for qi in q:
            items_dict[qi.item_id] = (None, qi.preference)
        main(user_id, items_dict)
    Context = {'item_name':item_name,'item_id':item_id,'flag1':True,'flag2':True}
    return render(request,'play.html',Context)

def hate(request, id):
    global times2
    item_id = int(id)
    item_name = Item1.objects.get(item_id = item_id) .item_name
    username = request.session.get('username', False)
    time = times2 % 2
    if username:
        user_id = Login.objects.get(user_name = username).user_id
        u = User.objects.get(item_id=item_id,user_id=user_id)
        if time==0:
            flag2 = False
            u.preference = -4
            u.save()
        else:
            flag2 = True
            if u.count>1 and u.count<4 :
                u.preference = 2
            elif u.count>=4 and u.count<8:
                u.preference = 3
            else:
                u.preference = 4
            u.save()
    else:
        if time == 0:
            flag2 = False
        else:
            flag2 = True
    times2 += 1
    q = User.objects.filter(user_id=user_id)
    items_dict = dict()
    for qi in q:
        items_dict[qi.item_id] = (None, qi.preference)
    main(user_id, items_dict)
    Context = {'item_name':item_name,'item_id':item_id,'flag1':True,'flag2':flag2}
    return render(request,'play.html',Context)

def love(request, id):
    global times1
    item_id = int(id)
    item_name = Item1.objects.get(item_id = item_id) .item_name
    username = request.session.get('username', False)
    time = times1 % 2
    if username:
        user_id = Login.objects.get(user_name = username).user_id
        u = User.objects.get(item_id=item_id,user_id=user_id)
        if time==0:
            flag1 = False
            u.preference = 4
            u.save()
        else:
            flag1 = True
            if u.count>1 and u.count<4 :
                u.preference = 2
            elif u.count>=4 and u.count<8:
                u.preference = 3
            else:
                u.preference = 4
            u.save()
    else:
        if time == 0:
            flag1 = False
        else:
            flag1 = True
    times1 += 1
    q = User.objects.filter(user_id=user_id)
    items_dict = dict()
    for qi in q:
        items_dict[qi.item_id] = (None, qi.preference)
    main(user_id, items_dict)
    Context = {'item_name':item_name,'item_id':item_id,'flag1':flag1,'flag2':True}
    return render(request,'play.html',Context)