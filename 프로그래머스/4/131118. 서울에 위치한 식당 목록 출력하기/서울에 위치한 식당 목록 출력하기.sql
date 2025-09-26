-- 코드를 입력하세요
SELECT rest_info.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, SCORE
from rest_info
left join (
    select rest_id, round(avg(review_score), 2) as score
    from rest_review
    group by rest_id
) as r
on rest_info.rest_id = r.rest_id
where address like '서울%' and score is not null
order by score desc, favorites desc