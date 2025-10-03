-- 코드를 입력하세요

with info as (
    select member_id, count(*) as cnt
    from rest_review
    group by member_id
),
best as (
    select max(cnt) as m
    from info
),
member as (
    select member_id
    from info
    join best
    on info.cnt = best.m
)

select member_name, review_text, 
    date_format(review_date, '%Y-%m-%d') as review_date
from rest_review
inner join member
on rest_review.member_id = member.member_id
inner join member_profile
on rest_review.member_id = member_profile.member_id
order by review_date, review_text