USE project_2;
--
INSERT INTO Platformtypes (id, type) VALUES
    (1, 'PC'),
    (2, 'Xbox Series X'),
    (3, 'PlayStation 4'),
    (4, 'PlayStation 5'),
    (5, 'Fallout 4 - table game'),
    (6, 'Civilization V - table game');
--
INSERT INTO Platforms (price, type_id) VALUES
    (69, 1),
    (79, 1),
    (129, 4),
    (109, 2),
    (89, 3),
    (69, 3),
    (199, 5),
    (199, 6);
--
INSERT INTO Customers (login_name, added_date) VALUES
    ('some_guy', NOW()),
    ('Vlad Charul', NOW()),
    ('Dmytro Karpov', NOW()),
    ('nighthunetr2000', NOW()),
    ('Ninja', NOW()),
    ('Pewdiepie', NOW()),
    ('zloi_shkolnik', NOW()),
    ('4eknbItu`', NOW());
--
INSERT INTO Orders (added_time, play_time, customer_id, platform_id) VALUES
    (NOW(), 2, 1, 3),
    (NOW(), 1, 4, 4),
    (NOW(), 3, 3, 5),
    (NOW(), 4, 5, 6),
    (NOW(), 5, 6, 1),
    (NOW(), 4, 8, 7),
    (NOW(), 5, 6, 2);
--
UPDATE Orders AS O JOIN Platforms AS P ON O.platform_id = P.id
    SET O.price = O.play_time * P.price;