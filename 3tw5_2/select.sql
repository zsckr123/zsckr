SELECT * FROM  Album ;
SELECT Title  FROM  Album ;
SELECT Title  FROM Album  WHERE Title LIKE 'b%';
select * from Employee e ;
select * from Artist a ;
SELECT  *   from Album inner join Artist  on Album.ArtistId = Artist.ArtistId ;
SELECT  Title , name  from Album inner join Artist  on Album.ArtistId = Artist.ArtistId ;