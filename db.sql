-- Se crea una base de datos llamada "estaciones_SIATA" si no existe.
DROP DATABASE IF EXISTS estaciones_SIATA;
CREATE DATABASE IF not EXISTS estaciones_SIATA; 

-- Seleccionar base de datos
USE estaciones_SIATA; 

-- Vaciar las tablas
DROP TABLE IF EXISTS estaciones;

-- Crear tablas
CREATE TABLE estaciones	(
	id MEDIUMINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nombre TINYTEXT NOT NULL
);  