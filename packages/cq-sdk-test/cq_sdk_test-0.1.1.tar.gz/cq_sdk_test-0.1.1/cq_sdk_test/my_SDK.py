# my_sdk.py

class MySDK:
    def __init__(self, api_key):
        self.api_key = api_key

    def greet(self, name):
        return f"Hello, {name}! Welcome to MySDK."

def _fire_entrypoint():
    import fire
    fire.Fire()


if __name__ == "__main__":
    _fire_entrypoint()
