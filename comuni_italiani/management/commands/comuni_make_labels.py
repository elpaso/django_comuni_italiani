# -*- coding: utf-8 -*-
import argparse
import csv
import locale
import os
import sys

from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count

from comuni_italiani.models import *

locale.setlocale( locale.LC_ALL, 'it_IT.UTF-8' )

class NotRunningInTTYException(Exception):
    pass

class Command(BaseCommand):
    help = 'Crea la label Comune (Regione)'


    def handle(self, *args, **options):

        for c in Comune.objects.all():
            c.save()
