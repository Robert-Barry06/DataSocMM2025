SELECT word FROM mystery_words
WHERE ID_number > 9500 AND CAST(ID_number AS TEXT) NOT LIKE '%8%'
ORDER BY ID_number;
