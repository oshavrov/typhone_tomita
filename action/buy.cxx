#encoding "utf-8"

BuyWord -> Word<kwtype="купить_слово">;

BuyAction -> BuyWord interp(Buy.Word);
BuyAction -> BuyWord interp(Buy.Word) AnyWord<wff=/\d{1,2}/> interp(Buy.Number);