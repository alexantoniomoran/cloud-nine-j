from braces.views import CsrfExemptMixin
from django.views.generic import TemplateView

from website.api.constants import MAIN_DETECTOR
from website.api.models import Detector


class MainPageView(CsrfExemptMixin, TemplateView):
    template_name = "main_page.html"

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["MAIN_DETECTOR"] = "No."

        main_detector = Detector.objects.filter(name=MAIN_DETECTOR).first()
        if main_detector and main_detector.cloud_nine:
            context["MAIN_DETECTOR"] = "YES!!"

        return context
