-- 코드를 입력하세요
-- Neutered Male, Spayed Female = 중성화 완료
-- Intact Female, Intact Male = 중성화 미완료

select animal_id, animal_type, name
from animal_ins
where sex_upon_intake like 'Intact%'    -- 중성화가 안된 채로 입소한 동물
and animal_id in (                      -- 중성화가 되고 퇴소한 동물 ID
    select animal_id
    from animal_outs
    where sex_upon_outcome not like 'Intact%')
order by animal_id