from modal import Image, Stub, asgi_app

from main import app



image = (
    Image.from_registry(
        'ultralytics/ultralytics'
    ).pip_install_from_requirements('requirements.txt').run_commands(
        "pip install torch --extra-index-url https://download.pytorch.org/whl/cu117"
    )
    )

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
)

stub = Stub(name='detector', image=image)

@stub.function(
    gpu='A10G',    
)
@asgi_app()
def api():
    return app