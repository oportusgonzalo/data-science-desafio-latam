--Insertando valores en tabla: Artista
\copy artista from '/Users/gonzalooportus/Documents/CODE/data-science-desafio-latam/sql/Artista.csv' delimiter ',';

--Insertando valores en tabla: album
\copy album from '/Users/gonzalooportus/Documents/CODE/data-science-desafio-latam/sql/Album.csv' delimiter ',';

--Insertando valores en tabla: cancion
\copy cancion from '/Users/gonzalooportus/Documents/CODE/data-science-desafio-latam/sql/Cancion.csv' delimiter ',';