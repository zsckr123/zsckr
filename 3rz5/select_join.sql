SELECT * FROM Employee e order by LastName DESC;

SELECT LastName , Email  FROM Employee e WHERE LastName ='Adams';
SELECT LastName , Email  FROM Employee  WHERE LastName LIKE 'p%'; 
SELECT * FROM  Album a ;
SELECT * FROM Album a WHERE Title LIKE 'b%';

SELECT * FROM Employee e order by LastName DESC;
SELECT * from Album a ;
SELECT * from Artist a ;
# 27.03.2024;
SELECT * FROM Album  INNER JOIN Artist  ON Album.ArtistId  = Artist.ArtistId  ;
SELECT TITLE, Name  FROM Album  INNER JOIN Artist  ON Album.ArtistId  = Artist.ArtistId  ;
SELECT  * from Customer  ;
SELECT * from Invoice  ;
SELECT * FROM Invoice  inner join Customer  on Invoice.CustomerId = Customer.CustomerId ;
SELECT FirstName , LastName , Company , BillingAddress, BillingState FROM Invoice  inner join Customer  on Invoice.CustomerId = Customer.CustomerId ;
SELECT * from Playlist p ;
SELECT * from PlaylistTrack pt ;
select * from Track t ;

SELECT * from Track inner join Album on Track.AlbumId = Album.AlbumId ;
