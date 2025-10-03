-- 코드를 작성해주세요
-- case when then 사용법

select 
    hr_employees.emp_no, emp_name, grade,
    case
        when grade = 'S' then sal*0.2
        when grade = 'A' then sal*0.15
        when grade = 'B' then sal*0.1
        else 0
    end as bonus
from hr_employees
left join (
    select 
        emp_no, 
        case
            when sum(score)/2 >= 96 then 'S'
            when sum(score)/2 >= 90 then 'A'
            when sum(score)/2 >= 80 then 'B'
            else 'C'
        end as grade
    from hr_grade
    group by emp_no) as g
on hr_employees.emp_no = g.emp_no
order by hr_employees.emp_no