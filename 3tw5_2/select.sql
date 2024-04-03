SELECT * FROM  Album ;
SELECT Title  FROM  Album ;
SELECT Title  FROM Album  WHERE Title LIKE 'b%';
select * from Employee e ;
select * from Artist a ;
SELECT  *   from Album inner join Artist  on Album.ArtistId = Artist.ArtistId ;
SELECT  Title , name  from Album inner join Artist  on Album.ArtistId = Artist.ArtistId ;
select * from Track  ;
SELECT Name, Title  from Track inner join Album on Track.AlbumId = Album.AlbumId ;

select * from Track inner join MediaType on Track.MediaTypeId = MediaType.MediaTypeId ;

select Track.Name,Track.Composer, MediaType.Name  from Track inner join MediaType on Track.MediaTypeId = MediaType.MediaTypeId ;

SELECT * from Genre g ;
select *  from Track inner join Genre on Track.GenreId  = Genre.GenreId  ;

