from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.timezone import localdate
from .models import DailyWorkbook
from .utils import create_header_only_workbook

@login_required
def dashboard(request):
    return render(request, "excelhub/dashboard.html")

@login_required
def excel_home(request):
    today = localdate()
    wb_today = DailyWorkbook.objects.filter(date=today).first()
    if not wb_today:
        header_file = create_header_only_workbook(today)
        wb_today = DailyWorkbook.objects.create(date=today, file=header_file)
        request.session["excel_notice"] = "Fichier du jour créé avec l’entête uniquement."
    return redirect(f"/excel/{today.isoformat()}/")

@login_required
def excel_by_date(request, yyyy_mm_dd):
    wb = DailyWorkbook.objects.filter(date=yyyy_mm_dd).first()
    notice = request.session.pop("excel_notice", None)
    if not wb:
        dates = DailyWorkbook.objects.order_by("-date").values_list("date", flat=True)
        return render(request, "excelhub/not_found.html", {
            "date_requested": yyyy_mm_dd,
            "dates": dates,
        })
    return render(request, "excelhub/detail.html", {"workbook": wb, "notice": notice})
