## 2. Select and Limit ##

select College_jobs, Median, Unemployment_rate from recent_grads LIMIT 20;

## 3. Where ##

Select Major from recent_grads where Major_category = "Arts" LIMIT 5;

## 4. Operators ##

select Major,Total,Median,Unemployment_rate from recent_grads 
where (Major_category != 'Engineering') and (Unemployment_rate > 0.065 or Median <= 50000);

## 5. Ordering ##

select major
from recent_grads
where Major_category!='Engineering'
order by major desc
limit 20;