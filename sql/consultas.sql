--Canciones que salieron el año 2018:
-- God Is a Woman, I Like It, Havanna, Train food, One Minute
select distinct(titulo_cancion) from cancion left join album on album.titulo_album = cancion.album and album.artista = cancion.artista where album.anio=2018;

-- albums y la nacionalidad de su artista
select titulo_cancion, album, nacionalidad from cancion left join album on album.titulo_album = cancion.album and album.artista = cancion.artista left join artista on artista.nombre_artista = cancion.artista where album.anio=2018;

-- numero de track, cancion, album, año de lanzamiento
-- y artista donde las canciones deberan estar ordenadas
-- por año del lanzamiento del album, album y artista
-- correspondiente
select numero_del_track, titulo_cancion, album, anio, artista from cancion left join album on album.titulo_album = cancion.album left join artista on artista.nombre_artista = cancion.artista order by anio, album, artista;