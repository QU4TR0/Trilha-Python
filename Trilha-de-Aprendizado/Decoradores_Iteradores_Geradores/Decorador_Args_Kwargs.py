import functools
def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
        
    return envelope

@duplicar
def aprendizado(tech):
    print(f"Estou aprendendo {tech}")
    return tech.upper()

tech =  aprendizado("Python")
print(tech)
print(duplicar.__name__)