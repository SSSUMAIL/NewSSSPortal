from django import template
import re

register = template.Library()


@register.filter(name='censor')
def censor(value):
    with open("censor_list.txt") as f:
        fileList = f.read().splitlines()
        for i in fileList:
            value = re.sub(r'\b(?i)'+re.escape(i)+r'\b', i[0] + "*" * (len(i) - 1), value)
        return str(value)
