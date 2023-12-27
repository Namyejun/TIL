-- https://school.programmers.co.kr/learn/courses/30/lessons/151136?language=oracle
-- 코드를 입력하세요
SELECT round(avg(DAILY_FEE), 0) as "AVERAGE_FEE"
from CAR_RENTAL_COMPANY_CAR
where CAR_TYPE = 'SUV';