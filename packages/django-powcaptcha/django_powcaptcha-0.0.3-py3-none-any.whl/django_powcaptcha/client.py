from django.core.cache import cache
import json
from urllib.error import HTTPError
from urllib.request import Request, build_opener

from django.conf import settings


class PowCaptchaValidationException(Exception):
    pass


def powcaptcha_request(path, params):
    domain = getattr(settings, 'POWCAPTCHA_API_URL')
    token = getattr(settings, 'POWCAPTCHA_API_TOKEN')

    request_object = Request(
        url=f'{domain}/{path}',
        data=params,
        headers={
            'Authorization': f'Bearer {token}',
        },
    )

    opener_args = []
    opener = build_opener(*opener_args)

    return opener.open(
        request_object,
        timeout=5
    )


def get_challenge():
    challenges = cache.get('powcaptcha_challenges')

    if not challenges or len(challenges) == 0:
        path = 'GetChallenges?difficultyLevel=5'
        response = powcaptcha_request(path, [])
        challenges = json.loads(response.read().decode('utf-8'))

    challenge = challenges[0]
    challenges.pop(0)
    cache.set('powcaptcha_challenges', challenges, 3600)

    return challenge


def validate_captcha(challenge: str, nonce: str):
    path = f'Verify?challenge={challenge}&nonce={nonce}'

    try:
        powcaptcha_request(path, [])
    except HTTPError as error:
        raise PowCaptchaValidationException(error.code)
