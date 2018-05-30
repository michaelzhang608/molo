from os import walk
from os.path import join, dirname

from glob import glob

from django.test import TestCase
from django.conf import settings
from molo.core.scripts.utils import lint_template_file
from molo.core.scripts.template_lint import log_error


class TestMoloProfileTemplates(TestCase):
    def test_lint_profile_templates(self):
        app_template_dir = join(
            dirname(settings.PROJECT_ROOT), "molo", "profiles", "templates")

        html_templates = []
        template_directories = [
            walk_result[0] for walk_result in
            walk(app_template_dir)]

        for directory in template_directories:
            html_templates += glob(join(directory, '*.html'))

        errors = [lint_template_file(filename) for filename in html_templates]
        if any(errors):
            log_error(*[error for error in errors if error])
        self.assertFalse(any(errors))