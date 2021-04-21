CREATE TABLE CITY (C_ID TEXT PRIMARY KEY, C_NAME TEXT, COUNTRY TEXT);
CREATE TABLE WEATHER_STATUS (S_ID TEXT PRIMARY KEY, STAT TEXT);

CREATE TABLE WEATHER_DAILY (C_ID TEXT, WDATE TEXT, MIN_TEMP REAL, MAX_TEMP REAL,
							S_ID TEXT, PRIMARY KEY (C_ID,WDATE), FOREIGN KEY (C_ID) REFERENCES CITY(C_ID));

INSERT INTO CITY (C_NAME,C_ID, COUNTRY) VALUES
	("HaNoi", "001", "VietNam"), 
	("Sydney", "002", "Australia"), 
	("NewYork", "003", "American"), 
	("Tokyo", "004", "Japan"), 
	("Berlin", "005", "German");

INSERT INTO WEATHER_STATUS (S_ID, STAT) VALUES
	('1', "Rainy"), 
	('2', "Sunny"), 
	('3', "Cloudy"), 
	('4', "Windy"), 
	('5', "Partly cloudy"), 
	('6', "Snowy"), 
	('7', "Lightning"), 
	('8', "Stormy");

INSERT INTO WEATHER_DAILY (C_ID, WDATE, MIN_TEMP, MAX_TEMP, S_ID) VALUES 
	("001", '2021-4-24',30,35,'2'), 
	("001",'2021-4-25',25,30,'3'), 
	("001",'2021-4-26',22,26,'1'), 
	("001",'2021-4-27',23,28,'4'),
	("001",'2021-4-28',25,30,'3'),
	("001",'2021-4-29',20,25,'1'), 
	("001",'2021-4-30',25,29,'4'),
	("002",'2021-4-25',25,30,'3'), 
	("004",'2021-4-26',22,26,'1'), 
	("002",'2021-4-27',23,28,'4'),
	("003",'2021-4-28',25,30,'3'),
	("004",'2021-4-29',20,25,'1'), 
	("005",'2021-4-30',25,29,'4'),
	("001", '2021-4-21',30,35,'2'), 
	("001",'2021-4-22',25,30,'3'), 
	("001",'2021-4-23',22,26,'1'), 
	("002",'2021-4-21',23,28,'4'),
	("002",'2021-4-22',25,30,'3'),
	("002",'2021-4-23',20,25,'1'), 
	("002",'2021-4-24',25,29,'4'),
	("003", '2021-4-21',30,35,'2'), 
	("003",'2021-4-22',25,30,'3'), 
	("003",'2021-4-23',22,26,'1'), 
	("003", '2021-4-24',30,35,'2'), 
	("003",'2021-4-25',25,30,'3'), 
	("003",'2021-4-26',22,26,'1');
