import httpx

class Mailbit:
    def __init__(self, api_key, base_url='https://public-api.mailbit.io'):
        if not api_key:
            raise ValueError("API key is required")
        self.api_key = api_key
        self.base_url = base_url
        self.client = httpx.Client(
            headers={'token': self.api_key},
            timeout=httpx.Timeout(30.0),
            transport=httpx.HTTPTransport(retries=3)
        )

    @staticmethod
    def generate_error_message(code, message):
        return {'code': code, 'message': message}

    def send_email(self, email_data):
        url = f'{self.base_url}/send-email'

        try:
            response = self.client.post(url, json=email_data)
            response.raise_for_status()
            data = response.json()
            return data
        except httpx.HTTPStatusError as err:
            if err.response:
                try:
                    error_data = err.response.json()
                    if isinstance(error_data, list):
                        error_messages = [f"Code: {error.get('code', 'Unknown')}, Message: {error.get('message', 'No error message provided')}" for error in error_data]
                        message = " | ".join(error_messages)
                    else:
                        code = error_data.get('code', 'Unknown')
                        message = error_data.get('message', 'No error message provided')
                    raise ValueError(Mailbit.generate_error_message(code, message))
                except ValueError:
                    code = err.response.status_code
                    message = err.response.text
                    raise ValueError(Mailbit.generate_error_message(code, message))
            else:
                raise ValueError(str(err))

    def close(self):
        self.client.close()
