from poke_validation import validate
import data as d
from get_base_info import get_base_pokemon
from get_species_info import get_species
from get_types import get_types_info
from build_pokemon_html import build_html, build_html_etapa_previa, etapa_previa_template
from show import show_pics


# solicitamos al usuario ingresar el nombre de un Pokémon
# nos hacemos cargo de la limpieza del nombre
pokemon = input("Ingrese el nombre de un Pokémon. Nota: Si el pokémon tiene espacios reemplace por '-'. No coloque ningún tipo de signo de puntuación adicional: ").lower()

# verificamos la existencia de puntuación o espacios en el nombre ingresado
while '.' in pokemon or ' ' in pokemon:
    pokemon = input("El nombre ingresado no es válido. Ingrese nuevamente el nombre de un Pokémon: ")

# validar nombre(existencia)
pokemon = validate(pokemon)

#for key, url in d.key_url_dict.items()[0]: ---> EXTENSION TO RUN ALL??????
#    pass

# obtenemos datos desde endpoints: pokemon, species, types
base_pokemon = get_base_pokemon(name=pokemon)
base_species = get_species(name=pokemon)

species_etapa_previa = base_species['etapa_previa'][0]

# como un pokemon puede tener mas de un tipo, y la consulta sobre las fortalezas y debilidades se ejecuta de forma
# individual para cada tipo, entonces sumamos los valores de las llaves identicas (listas), identificamos unicos,
# y guardamos la informacion en un diccionario global sobre fortalezas y debilidades (considerando ambos tipos)
base_types_en = {}
base_types = {}
if len(base_pokemon['types']) > 1:
    types_1_en, types_1 = get_types_info(base_pokemon['types'][0])
    types_2_en, types_2 = get_types_info(base_pokemon['types'][1])
    for key in types_1_en.keys():
        key_val = list(set(types_1_en[key] + types_2_en[key]))
        base_types_en.update({key: key_val})
    base_types_en.update({'type_en': [types_1_en['type_en'], types_2_en['type_en']]})
    for key in types_1.keys():
        key_val = list(set(types_1[key] + types_2[key]))
        base_types.update({key: key_val})
    base_types.update({'type_es': [types_1['type_es'], types_2['type_es']]})
else:
    base_types_en, base_types = get_types_info(base_pokemon['types'][0])

# funcion que permite rellenar todos los templates para el archivo html
dict_with_templates = d.template_fill(base_pokemon, base_species, base_types_en, base_types)

# sustitucion de variables en template html
# reemplazo en html de acuerdo a existencia de variable etapa previa
if base_species['etapa_previa'][0] == False:
    html_ = build_html.substitute(id=base_pokemon['id'], name=base_pokemon['name'].title(), url=base_pokemon['image'],
                table=dict_with_templates['texto_stats'], tipo=dict_with_templates['texto_tipo'], 
                tipo_especial=dict_with_templates['texto_especial'], descripcion=base_species['flavor_text_entries'],
                super_efectivo=dict_with_templates['texto_super_efectivo'], debil=dict_with_templates['texto_debil'], 
                resistente_contra=dict_with_templates['texto_resistente_contra'], poco_eficaz=dict_with_templates['texto_poco_eficaz'], 
                inmune=dict_with_templates['texto_inmune'], ineficaz=dict_with_templates['texto_ineficaz'])
else:
    html_ = build_html_etapa_previa.substitute(id=base_pokemon['id'], name=base_pokemon['name'].title(), url=base_pokemon['image'],
                etapa_previa=etapa_previa_template.substitute(etapa_previa=species_etapa_previa.title()), table=dict_with_templates['texto_stats'], tipo=dict_with_templates['texto_tipo'], 
                tipo_especial=dict_with_templates['texto_especial'], descripcion=base_species['flavor_text_entries'],
                super_efectivo=dict_with_templates['texto_super_efectivo'], debil=dict_with_templates['texto_debil'], 
                resistente_contra=dict_with_templates['texto_resistente_contra'], poco_eficaz=dict_with_templates['texto_poco_eficaz'], 
                inmune=dict_with_templates['texto_inmune'], ineficaz=dict_with_templates['texto_ineficaz'])

# apertura web del html para el pokemon en especifico
show_pics(html=html_, nombre=pokemon)



