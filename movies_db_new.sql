CREATE DATABASE IF NOT EXISTS movies_db;
USE movies_db;

CREATE TABLE IF NOT EXISTS classifications
(
	rate VARCHAR(3) NOT NULL,
    min_age int NOT NULL,
    PRIMARY KEY(rate)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS genres
(
	id_gen INT NOT NULL auto_increment,
    gen VARCHAR(35) NOT NULL,
    PRIMARY KEY(id_gen)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS directors
(
	id_dir INT NOT NULL auto_increment,
	fn_d VARCHAR(35) NOT NULL,
    ln1_d VARCHAR(35) NOT NULL,
	ln2_d VARCHAR(60),
    d_country VARCHAR(50),
    phone_d VARCHAR(13),
    d_age INT,
    
    PRIMARY KEY(id_dir)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS actors
(
	id_act INT NOT NULL auto_increment,
	fn_a VARCHAR(35) NOT NULL,
    ln1_a VARCHAR(35) NOT NULL,
	ln2_a VARCHAR(60),
    a_country VARCHAR(50),
    phone_a VARCHAR(13),
    a_age INT,
    
    PRIMARY KEY(id_act)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS movies
(
	id_movie INT NOT NULL auto_increment,
    m_title VARCHAR(100) NOT NULL,
    duration TIME,
    premiere_day DATE,
    
    PRIMARY KEY(id_movie)
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS movie_det
(
	id_movie INT NOT NULL,
	id_gen INT NOT NULL,
    id_class VARCHAR(3) NOT NULL,
    
    PRIMARY KEY (id_movie),
	CONSTRAINT fk_movie FOREIGN KEY (id_movie)
    REFERENCES movies(id_movie)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_gen FOREIGN KEY (id_gen)
    REFERENCES genres(id_gen)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_class FOREIGN KEY (id_class)
    REFERENCES classifications(rate)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS casting
(
	id_movie INT NOT NULL,
	id_act INT NOT NULL,
    salary_a FLOAT,
    
    PRIMARY KEY(id_movie, id_act),
    CONSTRAINT fk_movie2 FOREIGN KEY (id_movie)
    REFERENCES movies(id_movie)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_act FOREIGN KEY (id_act)
    REFERENCES actors(id_act)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS movie_dir
(
	id_movie INT NOT NULL,
	id_dir INT NOT NULL,
    salary_d FLOAT,
    
    PRIMARY KEY(id_movie, id_dir),
    CONSTRAINT fk_movie3 FOREIGN KEY (id_movie)
    REFERENCES movies(id_movie)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_dir FOREIGN KEY (id_dir)
    REFERENCES directors(id_dir)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = INNODB;