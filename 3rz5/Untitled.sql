SELECT * FROM Employee e order by LastName DESC;

SELECT LastName , Email  FROM Employee e WHERE LastName ='Adams';
SELECT LastName , Email  FROM Employee  WHERE LastName LIKE 'p%'; 
SELECT * FROM  Album a ;
SELECT * FROM Album a WHERE Title LIKE 'b%';

SELECT * FROM Employee e order by LastName DESC;
SELECT * from Album a ;
SELECT * from Artist a ;

SELECT * FROM Album  INNER JOIN Artist  ON Album.ArtistId  = Artist.ArtistId  ;


