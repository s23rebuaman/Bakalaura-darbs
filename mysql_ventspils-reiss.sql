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

-- noslogotākais maršruts 2025.gada 29.decembrī pulkstens 22:10
select Marsruta_nr, Reisa_nosaukums, Datums_un_laiks, count(Bilesu_sk)
from info
where year(Datums_un_laiks) = 2025
and month(Datums_un_laiks) = 12
and day(Datums_un_laiks) = 29
and time(Datums_un_laiks) = 2210
and Bilesu_sk=(select max(Bilesu_sk))
