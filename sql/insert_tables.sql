--Insertando valores en tabla: Artista
\copy artista(nombre_artista, fecha_de_nacimiento, nacionalidad) from '/Users/gonzalooportus/Documents/CODE/data-science-desafio-latam/sql/Artista.csv' delimiter ',' csv header;

--Insertando valores en tabla: album
\copy album(titulo_album, artista, anio) from '/Users/gonzalooportus/Documents/CODE/data-science-desafio-latam/sql/Album.csv' delimiter ',' csv header;

--Insertando valores en tabla: cancion
\copy cancion(titulo_cancion, artista, album, numero_del_track) from '/Users/gonzalooportus/Documents/CODE/data-science-desafio-latam/sql/Cancion.csv' delimiter ',' csv header;