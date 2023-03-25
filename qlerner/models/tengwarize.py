from jinja2.filters import do_mark_safe

_tengwar_beginning = '<span class="tengwar">'
_tengwar_ending = '</span>'

def tengwarize(value):
    # Transforms <...> into <span class="tengwar">...</span>
    return do_mark_safe(value.replace('$<', _tengwar_beginning).replace('$>', _tengwar_ending))