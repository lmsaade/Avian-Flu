SELECT Incident_Site_Name, DATEDIFF(DAY, Confirmed, Control_Zone_Release), Confirmed, Control_Zone_Release
FROM main_data;
