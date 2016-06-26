#encoding "utf8"

Phone -> AnyWord<kwtype="телефон">;
Laptop -> AnyWord<kwtype="ноутбук">;
Tablet -> AnyWord<kwtype="планшет">;
TV -> AnyWord<kwtype="телевизор">;

S -> Phone interp(Matter.Phone);
S -> Laptop interp(Matter.Notebook);
S -> Tablet interp(Matter.Tablet::not_norm);
S -> TV interp(Matter.TV);