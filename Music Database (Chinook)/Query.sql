-- Membuat tabel baru bernama combined_data yang berisi 
-- gabungan data dari beberapa tabel

CREATE TABLE combined_data AS
SELECT 

-- Mengambil kolom dari tabel track 
t.TrackId,
t.Name AS TrackName,
t.AlbumId,
t.Composer,
t.Milliseconds,
t.Bytes,
t.UnitPrice,
    
-- Mengambil kolom dari tabel album
al.Title AS AlbumTitle,
al.ArtistId,
    
-- Mengambil kolom dari tabel artist
ar.Name AS ArtistName,
    
-- Mengambil kolom dari tabel media_type
t.MediaTypeId,
mt.Name AS MediaTypeName,
    
-- Mengambil kolom dari tabel genre
t.GenreId,
g.Name AS GenreName,
       
-- Mengambil kolom dari tabel invoice_line dengan alias il
il.InvoiceId,
    
-- Mengambil kolom dari tabel invoice dengan alias i
i.CustomerId,
i.InvoiceDate,
i.BillingAddress,
i.BillingCity,
i.BillingState,
i.BillingCountry,
i.BillingPostalCode,
i.Total AS InvoiceTotal,
    
-- Mengambil kolom dari tabel customer
c.FirstName AS CustomerFirstName,
c.LastName AS CustomerLastName,
c.Address AS CustomerAddress,
c.City AS CustomerCity,
c.State AS CustomerState,
c.Country AS CustomerCountry,
    
-- Kolom tambahan dari tabel invoice_line
il.Quantity AS InvoiceLineQuantity,
il.UnitPrice AS InvoiceLineUnitPrice

FROM 
    -- Bergabung dengan tabel track sebagai t
    track t
JOIN 
    -- Bergabung dengan tabel album sebagai al berdasarkan AlbumId
    album al ON t.AlbumId = al.AlbumId
JOIN 
    -- Bergabung dengan tabel artist sebagai ar berdasarkan ArtistId
    artist ar ON al.ArtistId = ar.ArtistId

JOIN 
    -- Bergabung dengan tabel genre sebagai g berdasarkan GenreId
    genre g ON t.GenreId = g.GenreId
JOIN 
    -- Bergabung dengan tabel media_type sebagai mt berdasarkan MediaTypeId
    mediatype mt ON t.MediaTypeId = mt.MediaTypeId
JOIN 
    -- Bergabung dengan tabel invoice_line sebagai il berdasarkan TrackId
    invoiceline il ON t.TrackId = il.TrackId
JOIN 
    -- Bergabung dengan tabel invoice sebagai i berdasarkan InvoiceId
    invoice i ON il.InvoiceId = i.InvoiceId
JOIN 
    -- Bergabung dengan tabel customer sebagai c berdasarkan CustomerId
    customer c ON i.CustomerId = c.CustomerId;