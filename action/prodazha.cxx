#encoding "utf-8"

BuyOutWord -> Word<kwtype="купить_слово">;

BuyOutAction -> BuyOutWord interp(BuyOut.Word);
BuyOutAction -> BuyOutWord interp(BuyOut.Word) AnyWord<wff=/\d{1,2}/> interp(BuyOut.NumberInPrice);