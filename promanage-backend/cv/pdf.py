from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .models import CurriculumVitae

def generate_cv_pdf(request, pk):
    cv = CurriculumVitae.objects.get(pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{cv.title}.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Configuration du PDF
    width, height = letter
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, height - 100, cv.title)

    y_position = height - 130
    for entry in cv.entries.all().order_by('order'):
        p.setFont("Helvetica-Bold", 12)
        p.drawString(100, y_position, entry.title)
        p.setFont("Helvetica", 10)
        y_position -= 20
        p.drawString(120, y_position, entry.description)
        y_position -= 30

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
