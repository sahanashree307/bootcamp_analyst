Use task2;
select * from cell_phones_final;
select * from pop_final;
select c.country,c.Year,p.country,p.Pop,(c.Cell_phones/p.Pop) as cell_phone_per_person from cell_phones_final as c join Pop_final as p on c.country=p.country and c.Year=p.Year;