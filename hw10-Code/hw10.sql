.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name,size FROM dogs, sizes WHERE height > min AND height <= max ;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.child As name FROM parents AS a, dogs AS b WHERE a.parent = b.name ORDER BY height DESC;

CREATE TABLE sentential_helper AS
  SELECT a.child AS s1, b.child AS s2 FROM parents AS a, parents AS b WHERE a.parent = b.parent AND a.child < b.child;
-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT 'The two siblings, '|| s1 ||' plus '|| s2 || ' have the same size: ' ||a.size as sentence
  FROM sentential_helper ,size_of_dogs as a,size_of_dogs as b WHERE a.size = b.size and a.name=s1 and b.name=s2 and s1 < s2;
