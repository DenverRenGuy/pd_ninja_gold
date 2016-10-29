from django.shortcuts import render, redirect
import re, random
# Create your views here.
def index(request):
    request.session.setdefault('currentGold', 0)
    request.session.setdefault('cheater', '')

    return render(request, 'main/index.html')

def process(request, building):
    rs = request.session
    rm = request.method

    match = re.search(r'\b(farm|cave|house|casino)\b', building)

    if rm == 'POST':
        if not match:
            rs['currentGold'] = 0
            rs['cheater'] = True
            return redirect(request, '/')
        else:
            rs['cheater'] = False
            if building == 'farm':
                rs['currentGold'] += random.randint(10,20)
            elif building == "cave":
                rs['currentGold'] += random.randint(5,10)
            elif building == "house":
                rs['currentGold'] += random.randint(2,5)
            elif building == "casino":
                rs['currentGold'] += random.randint(-50,50)

    return redirect(request,'/')
