SELECT 
    AVG(no_show) * 100 AS no_show_percentage
FROM appointments;


SELECT
    CASE
        WHEN age < 18 THEN 'Child'
        WHEN age BETWEEN 18 AND 35 THEN 'Young Adult'
        WHEN age BETWEEN 36 AND 60 THEN 'Adult'
        ELSE 'Senior'
    END AS age_group,
    AVG(no_show) * 100 AS no_show_rate
FROM appointments
GROUP BY age_group;


SELECT 
    sms_received,
    AVG(no_show) * 100 AS no_show_rate
FROM appointments
GROUP BY sms_received;
