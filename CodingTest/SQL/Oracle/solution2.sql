-- https://school.programmers.co.kr/learn/courses/30/lessons/144853?language=oracle
-- 코드를 입력하세요
SELECT "BOOK_ID", to_char("PUBLISHED_DATE", 'YYYY-MM-DD')
from BOOK
where "CATEGORY" = '인문' and to_char("PUBLISHED_DATE", 'YYYY') = '2021'
order by "PUBLISHED_DATE" asc;