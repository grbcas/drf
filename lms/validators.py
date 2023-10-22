import re
from rest_framework.validators import ValidationError


class OnlyYoutubeUrl:

    def __call__(self, value) -> bool:
        if not bool(re.match(r'https://www.youtube.com', value, flags=0)):
            raise ValidationError(f'The url must be youtube')
