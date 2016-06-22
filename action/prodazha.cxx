#encoding "utf-8"

BuyOutWord -> Word<kwtype="купить_слово">;

BuyOutAction -> BuyOutWord interp(Buy.Word);
BuyOutAction -> BuyOutWord interp(Buy.Word) AnyWord<wff=/\d{1,2}/> interp(Buy.NumberInPrice);