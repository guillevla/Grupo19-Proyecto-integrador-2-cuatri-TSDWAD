use danza;

/* Tabla Academia */
create table Academia(
id_Academia int not null auto_increment,
nombre_Academia varchar(150) not null,
direccion_Academia varchar(150) not null,
email_Academia varchar(150) not null,
telefono_Academia bigint not null,
constraint pk_idAcademia primary key (id_Academia)
);

/* Tabla Profesor */
create table Profesor(
id_Profesor int not null auto_increment,
nombre_Profesor varchar(50) not null,
apellido_Profesor varchar(50) not null,
telefono_Profesor bigint not null,
id_Academia1 int not null,
constraint pk_idProfesor primary key (id_Profesor),
constraint fk_idAcademia1 foreign key (id_Academia1) references Academia (id_Academia)
);

/* Tabla Alumno*/
create table Alumno(
id_Alumno int not null auto_increment,
nombre_Alumno varchar(50) not null,
apellido_Alumno varchar(50) not null,
direccion_Alumno varchar(150) not null,
email_Alumno varchar(150) not null,
telefono_Alumno bigint,
id_Academia2 int not null,
constraint pk_idAlumno primary key (id_Alumno),
constraint fk_idAcademia2 foreign key (id_Academia2) references Academia (id_Academia)
);

/* Tabla Danza */
create table Danza(
id_Danza int not null auto_increment,
nombre_Danza varchar(50) not null,
constraint pk_idDanza primary key (id_Danza)
);

/* Tabla Alumno-Danza */

create table Alumno_Danza(
id_Alumno1 int not null,
id_Danza1 int not null,
constraint fk_idAlumno1 foreign key (id_Alumno1) references Alumno (id_Alumno),
constraint fk_idDanza1 foreign key (id_Danza1) references Danza (id_Danza)
);

/* Tabla Profesor_Danza */
create table Profesor_Danza(
id_Profesor1 int not null,
id_Danza2 int not null,
constraint fk_idProfesor1 foreign key (id_Profesor1) references Profesor (id_Profesor),
constraint fk_idDanza2 foreign key (id_Danza2) references Danza (id_Danza)
);



