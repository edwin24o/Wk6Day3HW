CREATE DATABASE Fitapp;

USE Fitapp;

CREATE TABLE Members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(70),
    email VARCHAR(50),
    membership_type VARCHAR(50)
);

CREATE TABLE WorkoutSessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    workout_type VARCHAR(100),
    duration INT,
    FOREIGN KEY (member_id) REFERENCES Members(id)
);