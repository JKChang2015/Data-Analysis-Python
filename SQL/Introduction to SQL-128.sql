## 4. SQLite ##

select Rank,Major from recent_grads;

## 5. Specifying column order ##

select Major,Rank from recent_grads;

## 6. Practice: Select ##

select Rank,Major_code, Major, Major_category, Total from recent_grads;

## 7. Where ##

select Major,ShareWomen from recent_grads where ShareWomen > 0.5;

## 8. Practice: Where ##

select Major, Employed from recent_grads where Employed > 10000

## 9. Limit ##

select Major from recent_grads where Employed > 10000 LIMIT 10;