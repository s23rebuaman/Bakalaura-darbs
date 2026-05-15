-- delete from ventspils_reiss_dati
-- ALTER TABLE ventspils_reiss_dati AUTO_INCREMENT = 0;

-- marsrutu tabula
/*
create table marsruti as
select distinct marsruta_nr, reisa_nosaukums from ventspils_reiss_dati
order by Marsruta_nr
*/

-- autobusu tabula
/*
create table autobusi as
select distinct Gar_nr, Autobusa_nr, Kases_aparats from ventspils_reiss_dati
order by Gar_nr
*/

-- vaditaju tabula
 /*
create table vaditaji as
select distinct Tab_nr, Autobusa_vaditajs from ventspils_reiss_dati
order by Autobusa_vaditajs
*/

-- info tabula
/*
create table info as
select Marsruta_nr, Reisa_nosaukums, Datums_un_laiks, Bilesu_sk from ventspils_reiss_dati
order by Datums_un_laiks
*/

-- bilesu skaits katram marsrutam kopa 2023 gada
/*
select Marsruta_nr, count(bilesu_sk) as "bilesu skaits marsrutiem 2023 gada"
from ventspils_reiss_dati
where year(Datums_un_laiks) = "2023"
group by Marsruta_nr
order by count(Bilesu_sk) desc
*/

-- noslogotākais maršruts 2023.gada 2.februārī
/*
select Marsruta_nr, Reisa_nosaukums, Datums_un_laiks, count(Bilesu_sk)
from info
where year(Datums_un_laiks) = 2023
and month(Datums_un_laiks) = 2
and day(Datums_un_laiks) = 2
and Bilesu_sk=(select max(Bilesu_sk))
*/

-- noslogotākais maršruts 2025.gada 29.decembrī pulkstens 18:55
/*
select Marsruta_nr, Reisa_nosaukums, Datums_un_laiks, max(Bilesu_sk)
from info
where year(Datums_un_laiks) = 2025
and month(Datums_un_laiks) = 12
and day(Datums_un_laiks) = 29
and time(Datums_un_laiks) = 185500
*/

-- maršruti 2024.gada 13.augustā no pulkstens 10:00 līdz 12:00
/*
select Marsruta_nr, Reisa_nosaukums, Datums_un_laiks, Bilesu_sk
from info
where year(Datums_un_laiks) = 2024
and month(Datums_un_laiks) = 8
and day(Datums_un_laiks) = 13
and (time(Datums_un_laiks) > 100000 and time(Datums_un_laiks) < 120000)
order by Bilesu_sk desc
*/

-- noslogotākais maršruts 2024.gada 13.augustā no pulkstens 10:00 līdz 12:00
/*
select Marsruta_nr, Reisa_nosaukums, Datums_un_laiks, max(Bilesu_sk)
from info
where year(Datums_un_laiks) = 2024
and month(Datums_un_laiks) = 8
and day(Datums_un_laiks) = 13
and (time(Datums_un_laiks) > 100000 and time(Datums_un_laiks) < 120000)
*/

-- distinct laiki (718 - 2023, 777 - 2024, 767 - 2025)
/*
select distinct time(Datums_un_laiks) from ventspils_reiss_dati
where year(Datums_un_laiks) = 2025
*/

-- select latest time value
-- select max(time(Datums_un_laiks)) from ventspils_reiss_dati

-- select earliest time value
-- select min(time(Datums_un_laiks)) from ventspils_reiss_dati

-- select time from 22:00 till 06:00
/*
select distinct time(Datums_un_laiks) from ventspils_reiss_dati
-- WHERE (time(Datums_un_laiks) >= '22:00:00' 
-- AND time(Datums_un_laiks) <= '23:59:59')
where (time(Datums_un_laiks) >= '00:00:00' 
AND time(Datums_un_laiks) <= '05:59:59')
order by time(Datums_un_laiks) desc
*/