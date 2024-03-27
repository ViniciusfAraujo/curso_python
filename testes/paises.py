from countryinfo import CountryInfo

paises = CountryInfo(input('Digite o nome do país: '))

print(f'País: {paises.name()}')
print(f'Capital: {paises.capital()}')
print(f'Moeda: {paises.currencies()}')
print(f'Idiomas: {paises.languages()}')
print(f'Fazem fronteiras: {paises.borders()}')
print(f'Código de area: {paises.calling_codes()}')
print(f'População: {paises.population()}')
