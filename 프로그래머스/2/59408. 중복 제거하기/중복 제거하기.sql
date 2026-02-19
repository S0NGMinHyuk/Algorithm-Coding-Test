-- 코드를 입력하세요
SELECT count(*) as count
FROM (
    SELECT name, count(name)
    FROM animal_ins
    WHERE name IS NOT NULL
    GROUP BY name) as x

    # SELECT name, count(name)
    # FROM animal_ins
    # WHERE name is not null
    # GROUP BY name