import data as d
from build_pokemon_html import table_template, tipo_template, tipo_especial_template, super_efectivo_template, debil_template, resistente_contra_template, poco_eficaz_template, inmune_template, ineficaz_template
from translate import translate


# mensaje de error al ingresar el nombre de un pokemon
validacion_pokemon = "El Pokémon ingresado no existe. Ingrese un nombre de Pokémon válido: "

# lista con nombre de stats en español
stats_name = ['HP', 'Ataque', 'Defensa', 'Ataque Especial', 'Defensa Especial', 'Velocidad']

# diccionario que permite hacer un reemplazo de tipos especiales a palabras comprensibles
special_dict = {
    'is_baby': 'Bebe', 
    'is_legendary': 'Legendario', 
    'is_mythical': 'Místico'
    }

# url base para hacer traducciones al español de tipos
base_url = 'https://pokeapi.co/api/v2/type/'

# funcion que completa los templates de variables con los valores de las mismas
# recibe diccionarios con todos los atributos a mostrar en el pokedex
# los tipos, fortalezas, y debilidades; son traducidos al español haciendo uso de la funcion translate
def template_fill(base_pokemon, base_species, base_types_en, base_types):

    # template stats
    lista_stats = [elemento for elemento in base_pokemon['stats']]
    texto_stats = ''
    for ele in range(0, len(lista_stats)):
        texto_stats += table_template.substitute(stat_name=d.stats_name[ele], stat_value=lista_stats[ele])

    # template types
    '''Cuando existe mas de un tipo, dado que no es una lista, entonces el numero de caracteres sera mayor a 2'''
    texto_tipo = ''
    if len(base_types_en['type_en']) > 2:
        texto_tipo += tipo_template.substitute(color=base_types_en['type_en'], tipo=translate(url=base_url+base_types_en['type_en'])) + ''
    else:
        lista_tipo_en = [elemento for elemento in base_types_en['type_en']]
        for ele in range(0, len(lista_tipo_en)):
            texto_tipo += tipo_template.substitute(color=lista_tipo_en[ele], tipo=translate(url=base_url+lista_tipo_en[ele])) + ''

    # template types_especial
    lista_especial = []
    for key in ['is_baby', 'is_legendary', 'is_mythical']:
        if base_species[key] != False:
            lista_especial.append(key.replace(key, special_dict[key]))
    texto_especial = ''
    for ele in range(0, len(lista_especial)):
        texto_especial += tipo_especial_template.substitute(tipo_especial=lista_especial[ele]) + ''

    # template super efectivo
    lista_super_efectivo_en = [elemento for elemento in base_types_en['double_damage_to']]
    texto_super_efectivo = ''
    for ele in range(0, len(lista_super_efectivo_en)):
        texto_super_efectivo += super_efectivo_template.substitute(color=lista_super_efectivo_en[ele], efectivo=translate(url=base_url+lista_super_efectivo_en[ele])) + ''

    # template debil
    lista_debil_en = [elemento for elemento in base_types_en['double_damage_from']]
    texto_debil = ''
    for ele in range(0, len(lista_debil_en)):
        texto_debil += debil_template.substitute(color=lista_debil_en[ele], debil=translate(url=base_url+lista_debil_en[ele])) + ''

    # template resistente contra
    lista_resistente_contra_en = [elemento for elemento in base_types_en['half_damage_from']]
    texto_resistente_contra = ''
    for ele in range(0, len(lista_resistente_contra_en)):
        texto_resistente_contra += resistente_contra_template.substitute(color=lista_resistente_contra_en[ele], resistente=translate(url=base_url+lista_resistente_contra_en[ele])) + ''

    # template poco eficaz
    lista_poco_eficaz_en = [elemento for elemento in base_types_en['half_damage_to']]
    texto_poco_eficaz = ''
    for ele in range(0, len(lista_poco_eficaz_en)):
        texto_poco_eficaz += poco_eficaz_template.substitute(color=lista_poco_eficaz_en[ele], poco_eficaz=translate(url=base_url+lista_poco_eficaz_en[ele])) + ''
    
    # template inmune
    lista_inmune_en = [elemento for elemento in base_types_en['no_damage_from']]
    texto_inmune = ''
    for ele in range(0, len(lista_inmune_en)):
        texto_inmune += inmune_template.substitute(color=lista_inmune_en[ele], inmune=translate(url=base_url+lista_inmune_en[ele])) + ''
    
    # template ineficaz
    lista_ineficaz_en = [elemento for elemento in base_types_en['no_damage_to']]
    texto_ineficaz = ''
    for ele in range(0, len(lista_ineficaz_en)):
        texto_ineficaz += ineficaz_template.substitute(color=lista_ineficaz_en[ele], ineficaz=translate(url=base_url+lista_ineficaz_en[ele])) + ''
    
    # diccionario con todos los templates
    dict_with_templates = {
        'texto_stats': texto_stats,
        'texto_tipo': texto_tipo,
        'texto_especial': texto_especial,
        'texto_super_efectivo': texto_super_efectivo,
        'texto_debil': texto_debil,
        'texto_resistente_contra': texto_resistente_contra,
        'texto_poco_eficaz': texto_poco_eficaz,
        'texto_inmune': texto_inmune,
        'texto_ineficaz': texto_ineficaz
        }
    
    return dict_with_templates