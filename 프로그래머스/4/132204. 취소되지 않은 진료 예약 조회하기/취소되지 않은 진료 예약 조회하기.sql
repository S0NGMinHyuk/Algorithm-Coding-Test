-- 코드를 입력하세요
-- 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회
-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
-- 진료예약일시를 기준으로 오름차순
select apnt_no, pt_name, p.pt_no, mcdp_cd, dr_name, apnt_ymd
from appointment
left join (
    select pt_no, pt_name
    from patient) as p          -- 환자 번호, 환자 이름
on appointment.pt_no = p.pt_no  -- 환자 번호로 매칭
left join (
    select dr_name, dr_id
    from doctor
    where mcdp_cd = 'CS') as d  -- 의사 이름, 의사 번호
on appointment.mddr_id = d.dr_id-- 의사 번호로 매칭
where apnt_ymd like '2022-04-13%'
and mcdp_cd = 'CS'
and apnt_cncl_yn = 'N'
order by apnt_ymd