#encoding "utf8"

Phone -> Word<kwtype="телефон">;
Laptop -> Word<kwtype="ноутбук">;

S -> Phone interp(Matter.Phone) | Laptop interp(Matter.Notebook);