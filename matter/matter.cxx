#encoding "utf8"

Phone -> AnyWord<kwtype="телефон">;
Laptop -> AnyWord<kwtype="ноутбук">;

S -> Phone interp(Matter.Phone);
S -> Laptop interp(Matter.Notebook);