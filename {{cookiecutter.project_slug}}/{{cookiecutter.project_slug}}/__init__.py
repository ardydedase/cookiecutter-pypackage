# -*- coding: utf-8 -*-

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

from .{{cookiecutter.project_slug}} import {{(cookiecutter.project_slug.title()).replace('_', '')}}

__all__ = ['{{(cookiecutter.project_slug.title()).replace('_', '')}}']
