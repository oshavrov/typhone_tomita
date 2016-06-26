#encoding "utf8"

Phone -> AnyWord<kwtype="телефон">;
Laptop -> AnyWord<kwtype="ноутбук">;
Tablet -> AnyWord<kwtype="планшет">;
TV -> AnyWord<kwtype="телевизор">;
OtherMatter -> AnyWord<kwtype="другой_предмет">;

S -> Phone interp(Matter.Phone);
S -> Laptop interp(Matter.Notebook);
S -> Tablet interp(Matter.Tablet::not_norm);
S -> TV interp(Matter.TV);
S -> OtherMatter interp(Matter.Other);
