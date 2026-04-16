import re
from .models import Term


def highlight_terms(text):
    terms = Term.objects.all()

    for term in terms:
        pattern = r'\b(' + re.escape(term.word) + r')\b'

        text = re.sub(
            pattern,
            f'<span class="term" data-id="{term.id}">\\1</span>',
            text,
            flags=re.IGNORECASE
        )

    return text
