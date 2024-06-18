from kubernetes import client

from .models.module import Module


def main():
    model = client.V1EphemeralContainer
    models = [
        # put models here
    ]

    known_models = set()
    for model in set(models):
        x = Module.from_model(model, known_models)
        x.write()


if __name__ == "__main__":
    main()
