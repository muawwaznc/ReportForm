from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from app.models import Muser, ExtraNCPrograms, NC, Report, Block, ProgramsNC, LibraryNDawa, Politics, Alkhidmat, AlkhidmatProjectDetails, UpperProgram, IT, Finance, Arkan, Karkun, Manpower, NCYearlyReport, NCGoals
from app.views import GetMuser, GetNC

def HomePage(request):
    return render(request, "index.html")

def ReportForm(request):
    data={
        "nc": GetNC(),
        "extraNCPrograms": ExtraNCPrograms.objects.all()
    }
    return render(request, "reportForm.html", data)

def AddMember(request):
    karkunList = Karkun.objects.filter(NC = GetNC())
    data = {
        "karkunList": karkunList,
    }
    return render(request, "addMember.html", data)

def AddRukan(request):
    arkanList = Arkan.objects.filter(NC = GetNC(), cetagory = "rukan")
    data = {
        "arkanList": arkanList,
    }
    return render(request, "addRukan.html", data)

def AddUmeedwar(request):
    umeedwarList = Arkan.objects.filter(NC = GetNC(), cetagory = "umeedwar")
    data = {
        "umeedwarList": umeedwarList,
    }
    return render(request, "addUmeedwar.html", data)

def AddBlockCode(request):
    blockList = Block.objects.filter(NC = GetNC())
    data = {
        "blockList": blockList
    }
    return render(request, "addBlockCode.html", data)

def AddNCGoals(request):
    ncGoalsList = NCGoals.objects.filter(NC = GetNC())
    data = {
        "ncGoalsList": ncGoalsList,
    }
    return render(request, "addNCGoals.html", data)




# For Admin
def AdminDashboard(request):
    NCList = NC.objects.all()
    reportsList = Report.objects.all()
    selectedNC = None
    selectedMonth = None
    monthName = None
    report = None
    programNC = None
    libraryNDawa = None
    politics = None
    upperProgram = None
    alkhidmat = None
    alkhidmatProjectDetails = None
    it = None
    finance = None
    manPower = None
    arkanList = None
    umeedwarList = None
    karkunList = None
    ncGoalsList = None
    ncYearlyReport = None

    monthsNameList = [
        'جنوری', 'فروری', 'مارچ', 'اپریل', 'مئی', 'جون', 
        'جولائی', 'اگست', 'ستمبر', 'اکتوبر', 'نومبر', 'دسمبر'
    ]

    if 'NC-id' in request.GET:
        selectedNC = NC.objects.get(pk=request.GET['NC-id'])

        if 'month' in request.GET:
            selectedMonth = request.GET['month']
            monthName = monthsNameList[int(selectedMonth) - 1]
            report = Report.objects.get(NC=selectedNC, month=selectedMonth)
            programNC = ProgramsNC.objects.filter(report=report)
            libraryNDawa = LibraryNDawa.objects.filter(report=report)
            politics = Politics.objects.get(report=report)
            upperProgram = UpperProgram.objects.filter(report=report)
            alkhidmat = Alkhidmat.objects.get(report=report)
            alkhidmatProjectDetails = AlkhidmatProjectDetails.objects.filter(alkhidmat=alkhidmat)
            it = IT.objects.get(report=report)
            finance = Finance.objects.filter(report=report)
            manPower = Manpower.objects.get(report = report)
            karkunList = Karkun.objects.filter(NC = selectedNC)
            arkanList = Arkan.objects.filter(NC = selectedNC, cetagory = "rukan")
            umeedwarList = Arkan.objects.filter(NC = selectedNC, cetagory = "umeedwar")
            ncGoalsList = NCGoals.objects.filter(NC = selectedNC)
            ncYearlyReport = NCYearlyReport.objects.filter(report = report)


    data = {
        "NCList": NCList,
        "selectedNC": selectedNC,
        'selectedMonth': selectedMonth,
        'report': report,
        'reportsList': reportsList,
        "muser": GetMuser(),
        "monthName": monthName,
        "programNC": programNC,
        "libraryNDawa": libraryNDawa,
        "politics": politics,
        "upperProgram": upperProgram,
        "alkhidmat": alkhidmat,
        "alkhidmatProjectDetails": alkhidmatProjectDetails,
        "it": it,
        "finance": finance,
        "manPower": manPower,
        "karkunList": karkunList,
        "arkanList": arkanList,
        "umeedwarList": umeedwarList,
        "ncGoalsList": ncGoalsList,
        "ncYearlyReport": ncYearlyReport,
    }
    return render(request, "adminDashboard.html", data)

def AddNC(request):
    NCList = NC.objects.all()
    data = {
        "NCList": NCList
    }
    return render(request, "addNC.html", data)

def AddExtraNCProgram(request):
    extraNCProgramList = ExtraNCPrograms.objects.all()
    data = {
        "extraNCProgramList": extraNCProgramList,
    }
    return render(request, "addExtraNCProgram.html", data)
