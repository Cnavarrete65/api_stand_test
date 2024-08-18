def delete_long_strings(s):
    if len(s) <= 10:
        return s
    else:
        return('Este string es demasiado largo')

print(delete_long_strings("¡Hola!"))
print(delete_long_strings("Python es increíble"))
print(delete_long_strings("corto"))