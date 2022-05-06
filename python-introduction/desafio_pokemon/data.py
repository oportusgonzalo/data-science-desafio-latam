import data as d
from build_pokemon_html import table_template, tipo_template, tipo_especial_template, super_efectivo_template, debil_template, resistente_contra_template, poco_eficaz_template, inmune_template, ineficaz_template


validacion_pokemon = "El Pokémon ingresado no existe. Ingrese un nombre de Pokémon válido: "

stats_name = ['HP', 'Ataque', 'Defensa', 'Ataque Especial', 'Defensa Especial', 'Velocidad']

special_dict = {
    'is_baby': 'Bebe', 
    'is_legendary': 'Legendario', 
    'is_mythical': 'Místico'
    }

def template_fill(base_pokemon, base_species, base_types):

    # template stats
    lista_stats = [elemento for elemento in base_pokemon['stats']]
    texto_stats = ''
    for ele in range(0, len(lista_stats)):
        texto_stats += table_template.substitute(stat_name=d.stats_name[ele], stat_value=lista_stats[ele])

    # template types
    texto_tipo = ''
    if len(base_types['type_es']) > 2:
        texto_tipo += tipo_template.substitute(tipo=base_types['type_es']) + ''
    else:
        lista_tipo = [elemento for elemento in base_types['type_es']]
        for ele in range(0, len(lista_tipo)):
            texto_tipo += tipo_template.substitute(tipo=lista_tipo[ele]) + ''

    # template types_especial
    lista_especial = []
    for key in ['is_baby', 'is_legendary', 'is_mythical']:
        if base_species[key] != False:
            lista_especial.append(key.replace(key, special_dict[key]))
    texto_especial = ''
    for ele in range(0, len(lista_especial)):
        texto_especial += tipo_especial_template.substitute(tipo_especial=lista_especial[ele]) + ''

    # template super efectivo
    lista_super_efectivo = [elemento for elemento in base_types['double_damage_to']]
    texto_super_efectivo = ''
    for ele in range(0, len(lista_super_efectivo)):
        texto_super_efectivo += super_efectivo_template.substitute(efectivo=lista_super_efectivo[ele]) + ''

    # template debil
    lista_debil = [elemento for elemento in base_types['double_damage_from']]
    texto_debil = ''
    for ele in range(0, len(lista_debil)):
        texto_debil += debil_template.substitute(debil=lista_debil[ele]) + ''

    # template resistente contra
    lista_resistente_contra = [elemento for elemento in base_types['half_damage_from']]
    texto_resistente_contra = ''
    for ele in range(0, len(lista_resistente_contra)):
        texto_resistente_contra += resistente_contra_template.substitute(resistente=lista_resistente_contra[ele]) + ''

    # template poco eficaz
    lista_poco_eficaz = [elemento for elemento in base_types['half_damage_to']]
    texto_poco_eficaz = ''
    for ele in range(0, len(lista_poco_eficaz)):
        texto_poco_eficaz += poco_eficaz_template.substitute(poco_eficaz=lista_poco_eficaz[ele]) + ''
    
    # template inmune
    lista_inmune = [elemento for elemento in base_types['no_damage_from']]
    texto_inmune = ''
    for ele in range(0, len(lista_inmune)):
        texto_inmune += inmune_template.substitute(inmune=lista_inmune[ele]) + ''
    
    # template ineficaz
    lista_ineficaz = [elemento for elemento in base_types['no_damage_to']]
    texto_ineficaz = ''
    for ele in range(0, len(lista_ineficaz)):
        texto_ineficaz += ineficaz_template.substitute(ineficaz=lista_ineficaz[ele]) + ''
    
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