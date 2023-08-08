from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Muser, ExtraNCPrograms, NC, Report, Block, ProgramsNC, LibraryNDawa, Politics, Alkhidmat, AlkhidmatProjectDetails, UpperProgram, IT, Finance, Arkan, Karkun, Manpower, NCYearlyReport, NCGoals

# Create your views here.

def Login(request):
    if request.method == 'POST':
        if Muser.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            data = Muser.objects.get(username=request.POST['username'], password=request.POST['password'])
            global muser
            muser = data
            return HttpResponseRedirect('/admin-dashboard')
        elif NC.objects.filter(number=request.POST['username'], password=request.POST['password']).exists():
            data = NC.objects.get(number=request.POST['username'], password=request.POST['password'])
            global nc
            nc = data
            return HttpResponseRedirect('/report-form')
        else:
            return HttpResponseRedirect('/')

def GetMuser():
    return muser

def GetNC():
    return nc


def AddNCToModel(request):
    if request.method == 'POST':
        president = request.POST.get('president')
        password = request.POST.get('password')
        nameNC = request.POST.get('nc-name')
        NCNumber = int(request.POST.get('nc-number'))

        data = NC(president=president, password=password, name=nameNC, number=NCNumber)
        data.save()
    return HttpResponseRedirect('/add-nc')

def AddOrganizationSection(request):
    nc = GetNC()
    nc.vicePresident = request.POST.get('vice-president')
    nc.secretory = request.POST.get('secretory')
    nc.viceSecretory = request.POST.get('vice-secretory')
    nc.finance = request.POST.get('finance')
    nc.publicity = request.POST.get('publicity')
    nc.womenContacts = request.POST.get('women-contacts')
    nc.studyCircle = request.POST.get('study-circle')
    nc.youth = request.POST.get('youth')
    nc.politicalCouncil = request.POST.get('political-council')
    nc.save()

def AddReport(request):
    date = request.POST.get('date')
    month = date.split('-')[1]
    year = date.split('-')[0]
    dawaProgramCount = int(request.POST.get('dawa-program-count'))
    extraProgramCount = int(request.POST.get('extra-count'))
    nc = GetNC()
    data = Report(month=month, year=year, NC=nc, dawaProgramCount=dawaProgramCount, extraProgramCount = extraProgramCount)
    data.save()
    return data

def AddManpower(request, report):
    arkanInitial = request.POST.get('rukan-initial')
    arkanAdded = request.POST.get('rukan-added')
    arkanMinus = request.POST.get('rukan-minus')
    arkanNow = request.POST.get('rukan-now')
    active = request.POST.get('rukan-active')
    retired = request.POST.get('rukan-retired')
    passive = request.POST.get('rukan-passive')
    umeerwarInitial = request.POST.get('umeedwar-initial')
    umeerwarAdded = request.POST.get('umeedwar-added')
    umeerwarMinus = request.POST.get('umeedwar-minus')
    umeerwarNow = request.POST.get('umeedwar-now')
    arkanRwabit = request.POST.get('rukan-rwabit')
    arkanRwabitNumber = request.POST.get('rukan-rwabit-number')
    umeedwarRwabit = request.POST.get('umeedwar-rwabit')
    umeedwarRwabitNumber = request.POST.get('umeedwar-rwabit-number')
    karkun = request.POST.get('karkun')
    voters = request.POST.get('voters')
    data = Manpower(arkanInitial = arkanInitial, arkanAdded = arkanAdded, arkanMinus = arkanMinus, arkanNow = arkanNow, active = active, retired = retired, passive = passive, umeerwarInitial = umeerwarInitial, umeerwarAdded = umeerwarAdded, umeerwarMinus = umeerwarMinus, umeerwarNow = umeerwarNow, arkanRwabit = arkanRwabit, arkanRwabitNumber = arkanRwabitNumber, umeedwarRwabit = umeedwarRwabit, umeedwarRwabitNumber = umeedwarRwabitNumber, karkun = karkun, voters = voters, report = report)
    data.save()

def AddNCProgram(request, report):
    programName = ["tanzeemi-ijtama", "dars", "dawati-ijtama", "ahl-khana"]
    for x in programName:
        target = int(request.POST.get(x+'-target'))
        held = int(request.POST.get(x+'-held'))
        attendence = int(request.POST.get(x+'-attendence'))
        data = ProgramsNC(name=x, target=target, held=held, attendence=attendence, report=report)
        data.save()
    extraProgramCount = int(request.POST.get('extra-count'))
    if extraProgramCount > 1:
        for x in range(1, extraProgramCount):
            name = request.POST.get('extra-name'+str(x))
            target = int(request.POST.get('extra-target'+str(x)))
            held = int(request.POST.get('extra-held'+str(x)))
            attendence = int(request.POST.get('extra-attendence'+str(x)))
            data = ProgramsNC(name=name, target=target, held=held, attendence=attendence, report=report)
            data.save()

def AddLibrary(request, report):
    libraryName = ["trjaman", "asia", "btool", "JI-library", "personal-library", "issue-books"]
    category = "Library"
    for x in libraryName:
        number = int(request.POST.get(x))
        data = LibraryNDawa(name=x, number=number, category=category, report=report)
        data.save()

def AddDawaProgram(request, report):
    dawaName = ["total-block-code", "permenent-dawa", "held-dawa", "total-meetings", "no-of-houses", "books-distribution", "individual-meetings", "voters"]
    category = "Dawa"
    for x in dawaName:
        number = int(request.POST.get(x))
        data = LibraryNDawa(name=x, number=number, category=category, report=report)
        data.save()

def AddPoliticsSection(request, report):
    isPublicSecretariat = request.POST.get('public-secretariat')
    activity = request.POST.get('political-activity')
    tryOnCitizenIssue = request.POST.get('public-issue')
    data = Politics(isPublicSecretariat = isPublicSecretariat, activity = activity, tryOnCitizenIssue = tryOnCitizenIssue, report = report)
    data.save()

def AddAlkhidmatSection(request, report):
    isProject = request.POST.get('is-alkhidmat-project')
    isFutureProject = request.POST.get('is-alkhidmat-future-project')
    projectDetailsCount = int(request.POST.get('alkhidmat-project-count'))
    data = Alkhidmat(isProject = isProject, isFutureProject = isFutureProject, projectDetailsCount = projectDetailsCount, report = report)
    data.save()
    if isProject == "ہاں":
        for x in range(1, projectDetailsCount):
            name = "alkhidmat-project-detail" + str(x)
            detail = request.POST.get(name)
            data1 = AlkhidmatProjectDetails(detail = detail, alkhidmat = data)
            data1.save()

def AddUpperProgram(request, report):
    names = ["zone-org-program", "zone-tarbiyya-program", "zone-study-circle"]
    for x in names:
        target = int(request.POST.get(x+'-target'))
        attendence = int(request.POST.get(x+'-attendence'))
        data = UpperProgram(name = x, target = target, attendence = attendence, report = report)
        data.save()

def AddIT(request, report):
    facebook = request.POST.get('facebook-page')
    whatsapp = request.POST.get('whatsapp-number')
    email = request.POST.get('email')
    youtube = request.POST.get('youtube-channel')
    data = IT(facebook = facebook, whatsapp = whatsapp, email = email, youtube = youtube, report = report)
    data.save()

def AddFinance(request, report):
    names = ['monthly', 'zakat', 'social-welfare', 'extra', 'total']
    for x in names:
        previousBalance = int(request.POST.get(x+'-balance'))
        amount = int(request.POST.get(x+'-amount'))
        total = int(request.POST.get(x+'-total'))
        expenses = int(request.POST.get(x+'-expenses'))
        upper = int(request.POST.get(x+'-upper'))
        currentBalance = int(request.POST.get(x+'-current'))
        data = Finance(name = x, previousBalance = previousBalance, amount = amount, total = total, expenses = expenses, upper = upper, currentBalance = currentBalance, report = report)
        data.save()

def AddNCYearlyReport(request, report):
    for x in range(1, 10):
        sentence = request.POST.get('sentence-' + str(x))
        start = request.POST.get('start-' + str(x))
        goal = request.POST.get('goal-' + str(x))
        monthlyAdded = request.POST.get('monthly-added-' + str(x))
        addedFromStart = request.POST.get('added-from-start-' + str(x))
        data = NCYearlyReport(sentence = sentence, start = start, goal = goal, monthlyAdded = monthlyAdded, addedFromStart = addedFromStart, report = report)
        data.save()

def AddMonthlyReport(request):
    if request.method == 'POST':
        AddOrganizationSection(request)
        report = AddReport(request)
        AddManpower(request, report)
        AddNCProgram(request, report)
        AddLibrary(request, report)
        AddDawaProgram(request, report)
        AddPoliticsSection(request, report)
        AddAlkhidmatSection(request, report)
        AddUpperProgram(request, report)
        AddIT(request, report)
        AddFinance(request, report)
        AddNCYearlyReport(request, report)
    return HttpResponseRedirect('/report-form')

def AddBlockCodeToModel(request):
    if request.method == 'POST':
        code = request.POST.get('block-code')
        name = request.POST.get('block-name')
        president = request.POST.get('block-president')
        secretory = request.POST.get('block-secretory')
        data = Block(code = code, name = name, president = president, secretory = secretory, NC = GetNC())
        data.save()
    return HttpResponseRedirect('/add-block-code')

def AddRukanIntoModel(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cetagory = "rukan"
        rbt1 = request.POST.get('rbt-1')
        rbt2 = request.POST.get('rbt-2')
        rbt3 = request.POST.get('rbt-3')
        rbt4 = request.POST.get('rbt-4')
        rbt5 = request.POST.get('rbt-5')
        rbt6 = request.POST.get('rbt-6')
        data = Arkan(name = name, cetagory = cetagory, rbt1 = rbt1, rbt2 = rbt2, rbt3 = rbt3, rbt4 = rbt4, rbt5 = rbt5, rbt6 = rbt6, NC = GetNC())
        data.save()
    return HttpResponseRedirect('/add-rukan')

def AddUmeedwarIntoModel(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cetagory = "umeedwar"
        rbt1 = request.POST.get('rbt-1')
        rbt2 = request.POST.get('rbt-2')
        rbt3 = request.POST.get('rbt-3')
        rbt4 = request.POST.get('rbt-4')
        rbt5 = request.POST.get('rbt-5')
        rbt6 = request.POST.get('rbt-6')
        data = Arkan(name = name, cetagory = cetagory, rbt1 = rbt1, rbt2 = rbt2, rbt3 = rbt3, rbt4 = rbt4, rbt5 = rbt5, rbt6 = rbt6, NC = GetNC())
        data.save()
    return HttpResponseRedirect('/add-umeedwar')

def AddMemberIntoModel(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        data = Karkun(name = name, NC = GetNC())
        data.save()
    return HttpResponseRedirect('/add-member')

def AddNCGoalIntoModel(request):
    if request.method == 'POST':
        detail = request.POST.get('detail')
        data = NCGoals(detail = detail, NC = GetNC())
        data.save()
    return HttpResponseRedirect('/add-nc-goals')

def AddExtraNCProgramIntoModel(request):
    if request.method == "POST":
        name = request.POST.get('name')
        data = ExtraNCPrograms(name = name)
        data.save()
    return HttpResponseRedirect('/add-extra-nc-program')