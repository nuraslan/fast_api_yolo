from modal import Image, Stub, asgi_app

from main import app



image = (
    Image.from_registry(
        'ultralytics/ultralytics'
    ).pip_install_from_requirements('requirements.txt')
)

stub = Stub(name='detector', image=image)

@stub.function(
    gpu='A10G',    
)
@asgi_app()
def api():
    return app