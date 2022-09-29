create table artista (
    nombre_artista varchar(50),
    fecha_de_nacimiento varchar(20),
    nacionalidad varchar(50),
    primary key (nombre_artista)
);

create table album (
    titulo_album varchar(50),
    artista varchar(50),
    anio int,
    primary key (titulo_album),
    foreign key (artista) references artista(nombre_artista)
);

create table cancion (
    titulo_cancion varchar(100),
    artista varchar(50),
    album varchar(50),
    numero_del_track int,
    primary key (titulo_cancion),
    foreign key (artista) references artista(nombre_artista),
    foreign key (album) references album(titulo_album)
);