"""
Interável -> srt, rnager, etc (__iter__)
Interador -> quem sabe entregar o valor por vez
netx -> me entregue o proximo valor
inter -> me entregue seu iterador
"""

texto = "Vinicius"
interador = iter(texto)

# while True:
#     try:
#         letra = next(interador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)