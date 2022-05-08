from string import Template

etapa_previa_template = Template('<h4>Etapa Previa: $etapa_previa</h4>')
table_template = Template('<td><h5>$stat_name: $stat_value</h5></td>')
tipo_template = Template('<span class="label $color">$tipo</span>')
tipo_especial_template = Template('<span class="label normal">$tipo_especial</span>')
super_efectivo_template = Template('<span class="label $color">$efectivo</span>')
debil_template = Template('<span class="label $color">$debil</span>')
resistente_contra_template = Template('<span class="label $color">$resistente</span>')
poco_eficaz_template = Template('<span class="label $color">$poco_eficaz</span>')
inmune_template = Template('<span class="label $color">$inmune</span>')
ineficaz_template = Template('<span class="label $color">$ineficaz</span>')


build_html = Template('''
<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="mystyle.css">
    </head>
    <body>

    <div class="column2">
    <div class="card">
    <h1>#$id $name</h1>
        <img src="$url" width="150" height="150">
    <div class="container">
        
        <h2>Estadísticas</h2>
        <table>
            <tr>
               $table
            </tr>
        </table>
        <h3><b>Tipo</b></h3> 
            $tipo
            $tipo_especial
            
        <p>$descripcion</p>
        
    <h3>Super efectivo contra:</h3>
        $super_efectivo
    <h3>Débil contra:</h3>
        $debil
    <h3>Resistente contra:</h3>
        $resistente_contra
    <h3>Poco Eficaz contra</h3>
        $poco_eficaz
    <h3>Inmune contra:</h3>
        $inmune
    <h3>Ineficaz contra:</h3>
        $ineficaz
    
    </div>
    </div>

    </body>
</html>
''')

build_html_etapa_previa = Template('''
<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="mystyle.css">
    </head>
    <body>

    <div class="column2">
    <div class="card">
    <h1>#$id $name</h1>
        <img src="$url" width="150" height="150">
    <div class="container">
        $etapa_previa
        <h2>Estadísticas</h2>
        <table>
            <tr>
               $table
            </tr>
        </table>
        <h3><b>Tipo</b></h3> 
            $tipo
            $tipo_especial
            
        <p>$descripcion</p>
        
    <h3>Super efectivo contra:</h3>
        $super_efectivo
    <h3>Débil contra:</h3>
        $debil
    <h3>Resistente contra:</h3>
        $resistente_contra
    <h3>Poco Eficaz contra</h3>
        $poco_eficaz
    <h3>Inmune contra:</h3>
        $inmune
    <h3>Ineficaz contra:</h3>
        $ineficaz
    
    </div>
    </div>

    </body>
</html>
''')
