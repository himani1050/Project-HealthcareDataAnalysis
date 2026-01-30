CREATE DATABASE healthcare_analytics;
USE healthcare_analytics;

CREATE TABLE appointments (
    appointment_id BIGINT PRIMARY KEY,
    patient_id BIGINT,
    gender VARCHAR(10),
    age INT,
    neighbourhood VARCHAR(100),
    scholarship TINYINT,
    hypertension TINYINT,
    diabetes TINYINT,
    alcoholism TINYINT,
    handicap TINYINT,
    sms_received TINYINT,
    scheduled_day DATETIME,
    appointment_day DATE,
    no_show TINYINT
);

SELECT * FROM appointments;

USE healthcare_analytics;
DROP TABLE IF EXISTS appointments;

CREATE TABLE appointments (
    appointment_id BIGINT PRIMARY KEY,
    patient_id BIGINT,
    gender CHAR(1),
    scheduled_day DATETIME,
    appointment_day DATE,
    age INT,
    neighbourhood VARCHAR(100),
    scholarship TINYINT,
    hypertension TINYINT,
    diabetes TINYINT,
    alcoholism TINYINT,
    handicap TINYINT,
    sms_received TINYINT,
    no_show TINYINT
);

SELECT COUNT(*) FROM appointments;

DESCRIBE appointments;


