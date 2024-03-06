USE BDDanzas;
/*Tabla Usuario*/
CREATE TABLE Usuario(
    id_usuario INT NOT NULL AUTO_INCREMENT,
    nombre_usuario VARCHAR(50) NOT NULL,
    apellido_usuario VARCHAR(50) NOT NULL,
    email_usuario VARCHAR(50) NOT NULL,
    CONSTRAINT pk_idUsuario PRIMARY KEY (id_usuario)
);

/* Tabla Ciudad */
CREATE TABLE Ciudad(
    id_ciudad INT NOT NULL AUTO_INCREMENT,
    nombre_ciudad VARCHAR(50) NOT NULL,
    CONSTRAINT pk_idCiudad PRIMARY KEY (id_ciudad)
);

/* Tabla Academia */
CREATE TABLE Academia(
    id_academia INT NOT NULL AUTO_INCREMENT,
    nombre_academia VARCHAR(150) NOT NULL,
    direccion_academia VARCHAR(150) NOT NULL,
    email_academia VARCHAR(150) NOT NULL,
    telefono_academia BIGINT NOT NULL,
    id_ciudad INT,
    CONSTRAINT pk_idAcademia PRIMARY KEY (id_academia),
    CONSTRAINT fk_idCiudad FOREIGN KEY (id_ciudad) REFERENCES Ciudad (id_ciudad)
);

/* Tabla Profesor */
CREATE TABLE Profesor(
    id_profesor INT NOT NULL AUTO_INCREMENT,
    nombre_profesor VARCHAR(50) NOT NULL,
    apellido_profesor VARCHAR(50) NOT NULL,
    telefono_profesor BIGINT NOT NULL,
    id_academia1 INT NOT NULL,
    CONSTRAINT pk_idProfesor PRIMARY KEY (id_profesor),
    CONSTRAINT fk_idAcademia1 FOREIGN KEY (id_academia1) REFERENCES Academia (id_academia)
);

/* Tabla Alumno */
CREATE TABLE Alumno(
    id_alumno INT NOT NULL AUTO_INCREMENT,
    nombre_alumno VARCHAR(50) NOT NULL,
    apellido_alumno VARCHAR(50) NOT NULL,
    direccion_alumno VARCHAR(150) NOT NULL,
    email_alumno VARCHAR(150) NOT NULL,
    telefono_alumno BIGINT,
    id_academia2 INT NOT NULL,
    id_ciudad int,
    CONSTRAINT pk_idAlumno PRIMARY KEY (id_alumno),
    CONSTRAINT fk_idAcademia2 FOREIGN KEY (id_academia2) REFERENCES Academia (id_academia),
    CONSTRAINT fk_idCiudad1 FOREIGN KEY (id_ciudad) REFERENCES Ciudad (id_ciudad)
);

/* Tabla Danza */
CREATE TABLE Danza(
    id_danza INT NOT NULL AUTO_INCREMENT,
    nombre_danza VARCHAR(50) NOT NULL,
    CONSTRAINT pk_idDanza PRIMARY KEY (id_danza)
);

/* Tabla Alumno_Danza */
CREATE TABLE Alumno_Danza(
    id_alumno1 INT NOT NULL,
    id_danza1 INT NOT NULL,
    CONSTRAINT fk_idAlumno1 FOREIGN KEY (id_alumno1) REFERENCES Alumno (id_alumno),
    CONSTRAINT fk_idDanza1 FOREIGN KEY (id_danza1) REFERENCES Danza (id_danza)
);

/* Tabla Profesor_Danza */
CREATE TABLE Profesor_Danza(
    id_profesor1 INT NOT NULL,
    id_danza2 INT NOT NULL,
    CONSTRAINT fk_idProfesor1 FOREIGN KEY (id_profesor1) REFERENCES Profesor (id_profesor),
    CONSTRAINT fk_idDanza2 FOREIGN KEY (id_danza2) REFERENCES Danza (id_danza)
);

/* Tabla Evento */
CREATE TABLE Evento(
    id_evento INT NOT NULL AUTO_INCREMENT,
    nombre_evento VARCHAR(50) NOT NULL,
    fecha_evento DATE NOT NULL,
    id_sede INT,
    CONSTRAINT pk_idevento PRIMARY KEY (id_evento),
    CONSTRAINT fk_idSede FOREIGN KEY (id_sede) REFERENCES Sede (id_sede)
);

/* Tabla Sede */
CREATE TABLE Sede(
    id_sede INT NOT NULL AUTO_INCREMENT,
    nombre_sede varchar(50) NOT NULL,
    direccion_sede varchar(50)NOT NULL,
    id_ciudad INT,
    CONSTRAINT pk_idsede PRIMARY KEY (id_sede),
    CONSTRAINT fk_idCiudad2 FOREIGN KEY (id_ciudad) REFERENCES Ciudad (id_ciudad)
);
