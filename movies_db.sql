#Movies Data Base 

CREATE DATABASE IF NOT EXISTS movies_db;
USE movies_db;

CREATE TABLE IF NOT EXISTS classifications
(
	class VARCHAR(3) NOT NULL,
    min_age int NOT NULL,
    PRIMARY KEY(class)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS genres
(
	id_gen VARCHAR(35) NOT NULL,
    PRIMARY KEY(id_gen)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS directors
(
	id_dir INT NOT NULL auto_increment,
	fn_d VARCHAR(35) NOT NULL,
	sn1_d VARCHAR(35),
    sn2_d VARCHAR(35),
    d_country VARCHAR(50),
    d_age INT,
    PRIMARY KEY(id_dir)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS actors
(
	id_act INT NOT NULL auto_increment,
	fn_a VARCHAR(35),
	sn1_a VARCHAR(35),
    sn2_a VARCHAR(35),
    a_country VARCHAR(50),
    a_age INT,
    PRIMARY KEY(id_act)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS movies
(
	id_movie INT NOT NULL auto_increment,
    m_title VARCHAR(100) NOT NULL,
    PRIMARY KEY(id_movie)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS movie_det
(
	id_movie INT,
	id_gen VARCHAR(35),
    id_class VARCHAR(3),
    
	CONSTRAINT fk_movie FOREIGN KEY (id_movie)
    REFERENCES movies(id_movie)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
    CONSTRAINT fk_gen FOREIGN KEY (id_gen)
    REFERENCES genres(id_gen)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
    CONSTRAINT fk_class FOREIGN KEY (id_class)
    REFERENCES classifications(class)
    ON DELETE SET NULL
    ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS casting
(
	id_movie INT,
	id_act INT,
    
    CONSTRAINT fk_movie2 FOREIGN KEY (id_movie)
    REFERENCES movies(id_movie)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
    CONSTRAINT fk_act FOREIGN KEY (id_act)
    REFERENCES actors(id_act)
    ON DELETE SET NULL
    ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS film_dir
(
	id_movie INT,
	id_dir INT,
    
    CONSTRAINT fk_movie3 FOREIGN KEY (id_movie)
    REFERENCES movies(id_movie)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
    CONSTRAINT fk_dir FOREIGN KEY (id_dir)
    REFERENCES directors(id_dir)
    ON DELETE SET NULL
    ON UPDATE CASCADE
)ENGINE = INNODB;
